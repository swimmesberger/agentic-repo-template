---
type: Architecture Decision Record
title: "docs/ is the OKF bundle; glossary, specs and raw files live outside it and are linked from the index"
description: "docs/ is the OKF bundle; glossary, specs and raw files live outside it and are linked from the index."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# docs/ is the OKF bundle; glossary, specs and raw files live outside it and are linked from the index

The Open Knowledge Format wants frontmatter, an index and a log on everything in its bundle; domain-modeling skills want `CONTEXT.md` at the root; spec frameworks own folders such as `specs/`, `openspec/` or `.kiro/`. We make `docs/` the bundle and keep it strictly conformant, leave the glossary and the specs where their tools look for them, link both from `docs/index.md` so an agent finds everything through one map, and keep files that cannot carry frontmatter in `raw/`.

## Considered options

- The repository root as the bundle: every Markdown file, including skills and subproject READMEs, would need frontmatter.
- Glossary and specs inside `docs/`: the skills and the spec frameworks would stop finding them.
- An exemption for raw files inside `docs/`: OKF has no way to exclude a subtree, so the bundle would no longer be conformant.

## Consequences

A skill that creates a file under `docs/` does not know the format. The rule in `AGENTS.md` and `make check` close the gap: frontmatter, an index entry and a log entry in the same change. The log is newest first, as OKF 0.2 section 9 requires, while ADR and spec numbers count upwards; that is intended.
