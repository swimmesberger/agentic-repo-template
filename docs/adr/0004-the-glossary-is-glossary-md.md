---
type: Architecture Decision Record
title: "The glossary is GLOSSARY.md at the repository root"
description: "The glossary is GLOSSARY.md at the repository root."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# The glossary is GLOSSARY.md at the repository root

Public domain-modeling skills, Matt Pocock's among them, look for the glossary in `GLOSSARY.md` at the root (`GLOSSARY-MAP.md` when a repository has several contexts, one `GLOSSARY.md` per context) and for decisions in `docs/adr/`, with no way to configure other paths. We use exactly those names so the skills work unmodified. The file's header says that only terms belong in it.

## Why the name changed

The skills used `CONTEXT.md` until their release 1.3.0 (4 October 2026). The upstream FAQ gives the reason: the file is a glossary and nothing else, so its name should say so, and with agents "everything is context". The rename also targets the problem the FAQ calls the most reported one, across several models: told to write to `CONTEXT.md`, models persisted every answer of a grilling session there until the file became a running spec. A name that says glossary invites less of that.

## Consequences

The skills look only for `GLOSSARY.md` (and `GLOSSARY-MAP.md`). A repository that still has `CONTEXT.md` renames it with `git mv` and updates the references in the same change; `setup-matt-pocock-skills` offers to do it. The rule that only terms go in still needs enforcing in review: the rename makes misuse less likely, not impossible.

## Sources

- [mattpocock/skills changelog, 1.3.0](https://github.com/mattpocock/skills/blob/main/CHANGELOG.md) and the [domain-modeling FAQ](https://github.com/mattpocock/skills/blob/main/docs/engineering/domain-modeling.md)
- [mattpocock/skills#130](https://github.com/mattpocock/skills/issues/130): the glossary used as a plan document during grilling
