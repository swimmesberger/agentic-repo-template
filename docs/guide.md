---
type: Guide
title: "How this knowledge folder is kept"
description: "What lives where, and the rules for sources, compiled pages, the index and the log."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# How this knowledge folder is kept

This folder is what an agent knows about the project beyond the code. It is an Open Knowledge Format bundle (OKF 0.2), kept the way Karpathy's LLM wiki is kept: raw material stays as received, compiled pages synthesise it, an index lists every page, and every change is logged. Agents read the index and follow pointers; they do not load the folder.

`index.md` holds only headings and entries, because OKF 0.2 section 8 defines an index that way; everything that explains the folder is on this page.

## What lives where

| Kind of knowledge | Lives in | Kind | Loaded |
|---|---|---|---|
| Terms and their meaning, and only that | `../GLOSSARY.md` | primary | on demand, pointed to from `AGENTS.md` |
| Decisions that are hard to reverse | `adr/` | primary | on demand |
| What a feature must do, and how it is built | `../specs/` | primary | per feature |
| How the system is shaped and why | `architecture.md` and other compiled pages | secondary, compiled from code, ADRs and sources | on demand |
| How the engineering skills find the tracker and the domain docs | `agents/` | primary, seeded from the skills' setup | by the skills |
| How we work: steps, practices, skills | `workflow.md` | secondary | on demand, pointed to from `AGENTS.md` |
| Raw material as received: notes, mails, research, requirements from outside | `sources/` | primary, never edited | when a compiled page needs checking |
| What changed in this folder and why | `log.md` | newest first, entries never edited | on demand |
| Files that cannot carry frontmatter (PDF, HTML, office files) | `../raw/`, outside the bundle | primary, never edited | when a source page points there |
| Working notes for one task, handoffs between sessions | `../.scratch/`, ignored by git | ephemeral | per task |

## Frontmatter

Every page except `index.md` and `log.md` starts with OKF frontmatter:

```yaml
---
type: Architecture page          # required, free text: Guide, Source, Architecture Decision Record, ...
title: "Architecture"
description: "One sentence on what the page is for."
generated: { by: claude-code/<model>, at: 2026-11-17T12:00:00Z }   # or human:<id>
verified: [{ by: human:<id>, at: 2026-11-18 }]                      # only once a person has read it
status: draft                    # draft | stable | deprecated
stale_after: 2027-06-30          # optional: date after which the page must be re-checked
---
```

A page without `verified` counts as unverified, which is the honest default for what an agent wrote. A page with only machine actors under `verified` is machine-confirmed; one with any `human:` actor is human-reviewed.

## Rules

- **A source enters with an envelope.** A file under `sources/` gets frontmatter (`type: Source`, where it came from, when) and its body stays exactly as it arrived. Name it by date and topic: `sources/2026-11-17-kickoff-notes.md`.
- **Sources are never edited.** When a compiled page and a source disagree, the source wins and the page gets fixed.
- **Compiled pages cite their sources** under a `Sources` heading at the bottom.
- **Update in the same change.** A pull request that changes behaviour updates the page that describes it. A page nobody updates is deleted: stale knowledge is loaded with the same confidence as fresh knowledge.
- **Every page is in its index.** A page not listed does not exist for the agent. Adding, renaming or removing a page means editing the index in the same change.
- **One log entry per change**, added with `tools/log_add.py`: `* **Operation**: what changed and why, with a [link](page.md)` under a `## YYYY-MM-DD` heading, newest day and newest entry first. Link the one to three pages that carry the change.
- **No harness memory.** What an agent would have remembered goes into one of the files above (ADR 0006).

## Sources

- [Open Knowledge Format, specification 0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [Andrej Karpathy, LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
