---
type: Format
title: "ADR format"
description: "When to write an architecture decision record and how."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Architecture decision records

An ADR records one decision that shaped this system: what we decided, in what context, and why. The folder is the memory the code cannot carry, for people and for agents. The format follows Michael Nygard's original proposal, kept deliberately short. The decisions 0001 to 0007 come with the template; keep them, or supersede them with your own.

## When to write one

All three must hold:

1. **Hard to reverse.** Changing your mind later costs real effort.
2. **Surprising without context.** A future reader would look at the code and ask why.
3. **A real trade-off.** There were genuine alternatives and one was chosen for reasons.

If any fails, do not write an ADR. Easy to reverse: you will just reverse it. Not surprising: nobody will ask. No alternative: there is nothing to record beyond "we did the obvious thing".

What qualifies: architectural shape, integration patterns between parts, technology choices with lock-in, ownership and boundary decisions, deliberate deviations from the obvious path, constraints not visible in the code, and rejected alternatives whose rejection is non-obvious.

## Format

File name: `NNNN-short-slug.md`, four digits, sequential, next free number. Never renumber.

```markdown
---
type: Architecture Decision Record
title: "Short title stating the decision"
description: "Short title stating the decision."
generated: { by: <actor>, at: <timestamp> }
status: stable
---
# Short title stating the decision

One to three sentences: the context, the decision, and why.
```

That is a complete ADR. The frontmatter is the Open Knowledge Format envelope every page under `docs/` carries (see `../guide.md`). Optional sections, only when they add something a reader would otherwise miss:

- `## Considered options`: the alternatives, one line each, and why they lost.
- `## Consequences`: downstream effects that are not obvious, good and bad.

The OKF `status` field is the ADR's state: `draft` while proposed, `stable` once accepted, `deprecated` when superseded, with `superseded_by: NNNN` next to it.

## Rules

- ADRs are immutable once accepted. A changed decision gets a new ADR that supersedes the old one; the old one gets `status: deprecated` and `superseded_by: NNNN`, and nothing else changes.
- Write in the terms of `../../CONTEXT.md` at the repository root. If a decision changes a term, update the glossary in the same change.
- Link the ADR from the pull request that implements it.
- Agents write ADRs through the `adr` skill, which follows this file.

## Sources

- Nygard, Documenting architecture decisions (2011): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- https://adr.github.io/, the community collection of formats and tools, including MADR for teams that want a fuller template.
