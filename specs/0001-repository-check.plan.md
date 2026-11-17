---
type: Plan
title: "Plan 0001: repository consistency check"
description: "How the checker of spec 0001 is built and tested."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Plan 0001: repository consistency check

## Shape

- One script, `tools/check_repo.py`, Python 3.12 standard library only (FR-009). A `check(root)` function returns the list of findings; `main()` prints them and sets the exit code (FR-001, FR-002).
- One function per convention: routers, pattern mirrors, links, skills, MCP file, bundle, specs. Each appends findings that start with the file path (FR-003).
- Frontmatter is parsed with a minimal reader for the YAML subset the repository uses (scalars, flow maps kept as strings, dash lists), so no YAML library is needed.

## Test seams

- Tests in `tests/test_check_repo.py` build a small repository in a temporary folder, change one thing, and call `check(root)`. The public seam is `check(root)`; no test reaches into the per-convention functions.
- One test per acceptance scenario, named after it.
