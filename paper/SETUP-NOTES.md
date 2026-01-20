# LaTeX Setup Notes

## Issue Resolution (January 20, 2026)

### Problem
The `task setup-latex` command was failing with:
```
sudo: /Library/TeX/texbin/tlmgr: command not found
```

### Root Cause
When BasicTeX is installed via Homebrew (`brew install --cask basictex`), the PKG file is downloaded but **not automatically installed**. The PKG installer must be run separately to actually install the TeX distribution to the system.

### Solution Applied

1. **Downloaded BasicTeX** via Homebrew:
   ```bash
   brew install --cask basictex
   ```

2. **Manually installed the PKG** file:
   ```bash
   sudo installer -pkg /opt/homebrew/Caskroom/basictex/2025.0308/mactex-basictex-20250308.pkg -target /
   ```

3. **Verified installation**:
   ```bash
   /Library/TeX/texbin/tlmgr --version
   ```

4. **Ran setup-latex**:
   ```bash
   cd paper && task setup-latex
   ```

### Taskfile Improvements

The `paper/Taskfile.yml` was updated to:
- Search for `tlmgr` in multiple common locations (not just hardcoded path)
- Add precondition checks to provide better error messages
- Make the setup more robust across different TeX installations

### Current Installation Location
- TeX Live: `/usr/local/texlive/2025basic`
- Binaries: `/Library/TeX/texbin/` (symlink to actual location)
- tlmgr: `/Library/TeX/texbin/tlmgr`

### Verification
The PDF build now works correctly:
```bash
cd paper && task build
# Output: PDF created output/dsp4d-paper.pdf
```

## Future Setup (Clean Install)

If setting up on a new machine:

1. Install dependencies:
   ```bash
   cd paper
   task setup
   ```

2. **Important**: If the automatic installation doesn't work, manually run:
   ```bash
   sudo installer -pkg /opt/homebrew/Caskroom/basictex/*/mactex-basictex-*.pkg -target /
   ```

3. Restart terminal or reload PATH:
   ```bash
   eval "$(/usr/libexec/path_helper)"
   ```

4. Install LaTeX packages:
   ```bash
   task setup-latex
   ```

5. Build the paper:
   ```bash
   task build
   ```

## Notes

- BasicTeX is a minimal TeX distribution (~120MB vs 7GB for full MacTeX)
- The setup-latex task installs only the required packages for the paper
- The Taskfile now handles different TeX installation paths automatically
