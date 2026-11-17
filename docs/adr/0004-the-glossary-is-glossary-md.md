---
type: Architecture Decision Record
title: "The glossary is GLOSSARY.md at the repository root"
description: "The glossary is GLOSSARY.md at the repository root."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# The glossary is GLOSSARY.md at the repository root

Public domain-modeling skills, Matt Pocock's among them, look for the glossary in `GLOSSARY.md` at the root (`GLOSSARY-MAP.md` when a repository has several contexts, one `GLOSSARY.md` per context) and for decisions in `docs/adr/`, with no way to configure other paths. We use exactly those names so the skills work unmodified. The file's header says that only terms belong in it.

## Consequences

Repositories set up before September 2026 may still have the earlier name `CONTEXT.md`, which the skills renamed on 17 September 2026; rename it with `git mv` and update the references in the same change.
