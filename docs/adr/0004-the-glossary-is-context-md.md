---
type: Architecture Decision Record
title: "The glossary is CONTEXT.md at the repository root"
description: "The glossary is CONTEXT.md at the repository root."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# The glossary is CONTEXT.md at the repository root

Public domain-modeling skills, Matt Pocock's among them, look for the glossary in `CONTEXT.md` at the root and for decisions in `docs/adr/`, with no way to configure other paths. We keep those names so the skills work unmodified, although "context" is an overloaded word in agent tooling. The file's header says that only terms belong in it.

## Consequences

If the tooling renames the convention (a rename to `GLOSSARY.md` has been proposed upstream), the file is renamed in the same change as the skills are updated.
