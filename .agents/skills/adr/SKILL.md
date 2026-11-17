---
name: adr
description: Write or supersede an architecture decision record in docs/adr. Use when a decision is hard to reverse, would surprise a future reader, or resolved a real trade-off, and when the user says "record this decision" or "write an ADR".
---
# ADR

The format, the three-part test for whether a decision deserves an ADR, and the rules for superseding live in `docs/adr/README.md`. Read it first; this skill is the procedure, not the format.

1. Apply the three-part test from the README. If it fails, tell the user why and stop.
2. Take the next free number in `docs/adr/` and create `NNNN-short-slug.md` in the README's format, with frontmatter (`type: Architecture Decision Record`, `title`, `description`, `generated`, `status`).
3. Add one entry to `docs/adr/index.md` and one to `docs/log.md` with `tools/log_add.py`; `make check` fails without them.
4. Never rewrite an accepted ADR. To change a decision, write a new one and set the old one's `status` to `deprecated` and add `superseded_by: NNNN`.
5. If the decision introduces or changes a term, update `CONTEXT.md` in the same change.
6. Link the ADR from the pull request description.
