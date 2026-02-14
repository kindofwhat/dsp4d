import re
import os
import platform
import subprocess
import time
import urllib.request
import urllib.error
import urllib.parse
from urllib.parse import urlparse

BIB_FILE = 'references.bib'
OUT_DIR = 'references'

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

def strip_quarantine(filepath):
    """Remove macOS quarantine/provenance attributes so PDF viewers can open linked files."""
    if platform.system() == 'Darwin':
        subprocess.run(['xattr', '-c', filepath], capture_output=True)

def get_references(bib_content):
    # simple state machine to parse bib entries
    references = []
    entry = {}
    lines = bib_content.split('\n')
    current_key = None
    
    for line in lines:
        line = line.strip()
        if line.startswith('@'):
            # New entry
            if current_key:
                references.append(entry)
            
            # extract key
            match = re.search(r'@\w+\{([^,]+),', line)
            if match:
                current_key = match.group(1).strip()
                entry = {'key': current_key, 'raw': ''}
            else:
                current_key = None
        
        if current_key:
            entry['raw'] += line + '\n'
            
            # extract fields (simple regex, multiline support is weak here but sufficient for one-liners)
            # Check for arXiv in journal field or elsewhere
            arxiv_match = re.search(r'arXiv[:\s]+(\d+\.\d+)', line, re.IGNORECASE)
            if arxiv_match:
                entry['arxiv_id'] = arxiv_match.group(1)
            
            url_match = re.search(r'url\s*=\s*\{([^}]+)\}', line, re.IGNORECASE)
            if url_match:
                entry['url'] = url_match.group(1)

    if current_key:
        references.append(entry)
        
    return references

def download_file(url, filepath):
    try:
        print(f"Downloading {url} to {filepath}...")
        # Add a User-Agent to avoid being blocked by some sites
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        strip_quarantine(filepath)
        print(f"Success: {filepath}")
        return True
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    return False


def download_iospress_pdf(pdf_id, filepath):
    try:
        url = 'https://ebooks.iospress.nl/Download/Pdf'
        print(f"Downloading {url} (id={pdf_id}) to {filepath}...")
        data = urllib.parse.urlencode({'id': str(pdf_id)}).encode('ascii')
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            method='POST'
        )
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        strip_quarantine(filepath)
        print(f"Success: {filepath}")
        return True
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: iospress id={pdf_id}")
    except Exception as e:
        print(f"Error downloading iospress id={pdf_id}: {e}")
    return False

def main():
    with open(BIB_FILE, 'r') as f:
        content = f.read()
    
    refs = get_references(content)
    print(f"Found {len(refs)} references.")
    
    # Manual mapping for papers not easily parsed or missing URLs in bib
    MANUAL_MAPPING = {
        'brown2020language': 'https://arxiv.org/pdf/2005.14165.pdf',
        'lin2022truthfulqa': 'https://arxiv.org/pdf/2109.07958.pdf',
        'chang2024survey': 'https://arxiv.org/pdf/2307.03109.pdf',
        'kim2024prometheus': 'https://arxiv.org/pdf/2310.08491.pdf',
        'es2024ragas': 'https://arxiv.org/pdf/2309.15217.pdf',
        'liu2023geval': 'https://arxiv.org/pdf/2303.16634.pdf',
        'fu2024gptscore': 'https://arxiv.org/pdf/2302.04166.pdf',
        'zhang2020bertscore': 'https://arxiv.org/pdf/1904.09675.pdf',
        'sellam2020bleurt': 'https://arxiv.org/pdf/2004.04696.pdf',
        'zhao2019moverscore': 'https://aclanthology.org/D19-1053.pdf',
        'papineni2002bleu': 'https://aclanthology.org/P02-1040.pdf',
        'lin2004rouge': 'https://aclanthology.org/W04-1013.pdf',
        'banerjee2005meteor': 'https://aclanthology.org/W05-0909.pdf',
        'clark2019sentence': 'https://aclanthology.org/P19-1264.pdf',
        'carlini2021extracting': 'https://arxiv.org/pdf/2012.07805.pdf',
        'zhao2021calibrate': 'https://arxiv.org/pdf/2102.09690.pdf',
        'kusner2015word': 'http://proceedings.mlr.press/v37/kusnerb15.pdf',
        'modersohn2022grascco': {
            'type': 'iospress',
            'id': '60437'
        }
    }
    
    for ref in refs:
        key = ref.get('key')
        if not key:
            continue
            
        filename = os.path.join(OUT_DIR, f"{key}.pdf")
        if os.path.exists(filename):
            print(f"Skipping {key} (already exists)")
            continue
            
        url = None
        manual_strategy = None
        
        # Strategy 0: Manual Mapping
        if key in MANUAL_MAPPING:
            manual_strategy = MANUAL_MAPPING[key]
            if isinstance(manual_strategy, str):
                url = manual_strategy
        
        # Strategy 1: arXiv ID
        if 'arxiv_id' in ref:
            url = f"https://arxiv.org/pdf/{ref['arxiv_id']}.pdf"
        
        # Strategy 2: Explicit URL (only if it looks like a PDF or we are desperate)
        elif 'url' in ref:
            # Check if likely a PDF or specific repository that serves PDFs
            u = ref['url']
            parsed = urlparse(u)
            path_lower = parsed.path.lower()
            if path_lower.endswith('.pdf') or path_lower.endswith('/pdf'):
                url = u
            elif 'arxiv.org' in u and 'abs' in u:
                url = u.replace('abs', 'pdf') + '.pdf'

        # Strategy 3: Manual special strategies
        if url is None and isinstance(manual_strategy, dict):
            if manual_strategy.get('type') == 'iospress' and manual_strategy.get('id'):
                success = download_iospress_pdf(manual_strategy['id'], filename)
                if success:
                    time.sleep(1)
                continue
        
        if url:
            success = download_file(url, filename)
            if success:
                time.sleep(1) # Be nice to servers
        else:
            print(f"No download strategy for {key}")

if __name__ == "__main__":
    main()
