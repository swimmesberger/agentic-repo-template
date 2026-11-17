---
type: Architecture Decision Record
title: "Harness memory is off; the repository is the memory"
description: "Harness memory is off; the repository is the memory."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Harness memory is off; the repository is the memory

Claude Code, Copilot, Codex and Cursor each offer a memory that stores notes on one machine or account and reloads them at session start. Those notes drift (a fact from March is loaded with the same confidence in June), bloat (they load whole), and do not travel (unreviewed, unversioned, invisible to the team and the next harness). We switch memory off in the committed settings and route what it would capture into files: corrections into rules in `AGENTS.md`, decisions into ADRs, terms into `GLOSSARY.md`, intent into specs, history into `docs/log.md`, working notes into the ignored `.scratch/`.

## Consequences

`.claude/settings.json` sets `autoMemoryEnabled: false`, `.vscode/settings.json` sets `chat.tools.memory.enabled: false`. GitHub's server-side Copilot Memory cannot be switched off from a file; repository admins turn it off in the repository's Copilot settings. Personal working preferences stay in each person's user-level instruction file, outside the repository.
