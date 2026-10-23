# Shopizer Code Journey (immutable source snapshot)

Source: https://github.com/shopizer-ecommerce/shopizer at `6a4a0a65a3408ee8f62597b51d1b3aac24b77dee`.

Walk through the parent TXT files in **numeric sequence order**, not lexicographic filename order.
Each parent is a distinct, contiguous, exact range of the original source file; only parents should be used when reconstructing. Children are up-to-eight-line exact duplicates of a parent, for teaching purposes. Some tasks are only one line.

Filenames explain code-specific operations, identifiers, keys and values wherever extractable.
They are machine-generated and should be reviewed against source; refer to the source and index for exact intent. Some original code fragments are not standalone compilable until subsequent tasks are applied.

## Rebuild and verification

Use `python rebuild.py --journey path/to/code-journey --output rebuilt` after unzipping. This sorts parent ranges by original source line and verifies each text file SHA256. Original binary assets are stored under `original-binaries/` in the ZIP when available. No TXT headers, changed whitespace, or extra newlines.

The historical task/edit order is **not** recoverable from a snapshot; the task sequence is a modeled educational development journey.

Data files: `MASTER_INDEX.csv`, `SOURCE_MANIFEST.csv`, `AUDIT.json`.

## Filename quality audit

All generated TXT basenames and sequence identifiers are unique, and the old generic description templates are rejected. Source bytes are never rewritten by renaming.
