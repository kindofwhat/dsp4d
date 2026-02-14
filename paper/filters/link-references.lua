--- link-references.lua
--- Pandoc Lua filter that makes citations clickable (runs AFTER citeproc).
---
--- Requires defaults-with-links.yaml which:
---   1. Sets link-citations: true (citeproc generates #ref-<key> links)
---   2. Orders filters: citeproc first, then this filter
---
--- This filter rewrites #ref-<key> link targets to actual paper URLs/files.
---
--- Link resolution priority (web URLs preferred — sandboxed PDF viewers
--- like Preview.app cannot follow relative file links):
---   1. URL field from .bib entry
---   2. arXiv ID -> https://arxiv.org/pdf/<id>
---   3. DOI -> https://doi.org/<doi>

local bib_entries = {}

--- Simple .bib parser: extracts url, doi, and arXiv ID per entry key.
local function parse_bib(path)
  local f = io.open(path, "r")
  if not f then
    io.stderr:write("[link-references] cannot open " .. path .. "\n")
    return
  end
  local content = f:read("*a")
  f:close()

  local current_key = nil
  local entry = {}

  for line in content:gmatch("[^\r\n]+") do
    local new_key = line:match("^%s*@%w+{%s*([^,%s]+)")
    if new_key then
      if current_key then
        bib_entries[current_key] = entry
      end
      current_key = new_key
      entry = {}
    end

    if current_key then
      local url = line:match("[Uu][Rr][Ll]%s*=%s*{([^}]+)}")
      if url then entry.url = url end

      local doi = line:match("[Dd][Oo][Ii]%s*=%s*{([^}]+)}")
      if doi then entry.doi = doi end

      local arxiv = line:match("arXiv:(%d+%.%d+)")
      if arxiv then entry.arxiv = arxiv end
    end
  end

  if current_key then
    bib_entries[current_key] = entry
  end
end

--- Resolve the best available URL for a citation key.
--- Prefers web URLs since sandboxed PDF viewers (e.g. Preview.app) cannot
--- follow relative file links due to macOS App Sandbox restrictions.
local function resolve_link(key)
  local entry = bib_entries[key]
  if not entry then return nil end

  if entry.url then return entry.url end
  if entry.arxiv then return "https://arxiv.org/pdf/" .. entry.arxiv end
  if entry.doi then return "https://doi.org/" .. entry.doi end

  return nil
end

--- Read bibliography path from document metadata and parse the .bib file.
function Meta(meta)
  local bib = meta.bibliography
  if bib then
    local path
    if type(bib) == "table" and bib[1] then
      path = pandoc.utils.stringify(bib[1])
    else
      path = pandoc.utils.stringify(bib)
    end
    parse_bib(path)
  else
    parse_bib("references.bib")
  end
end

--- Rewrite citeproc's #ref-<key> links to point to actual papers.
function Link(link)
  local key = link.target:match("^#ref%-(.+)$")
  if not key then return nil end

  local url = resolve_link(key)
  if not url then return nil end

  link.target = url
  return link
end

-- Meta must run first to populate bib_entries before Link processing.
return {
  { Meta = Meta },
  { Link = Link },
}
