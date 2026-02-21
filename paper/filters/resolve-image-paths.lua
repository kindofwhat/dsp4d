--- resolve-image-paths.lua
--- Pandoc Lua filter that normalizes image paths for the build.
---
--- Markdown files use paths relative to themselves (e.g. ../../assets/foo.png)
--- so images render in local markdown viewers. Pandoc runs from paper/, so
--- this filter strips leading ../../ to resolve correctly.

function Image(img)
  img.src = img.src:gsub("^%.%./%.\\.//", "")
  -- Handle ../../assets/ -> assets/ (chapters are 2 levels deep)
  img.src = img.src:gsub("^%.%./%.%./", "")
  return img
end
