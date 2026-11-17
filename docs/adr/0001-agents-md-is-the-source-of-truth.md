---
type: Architecture Decision Record
title: "AGENTS.md is the source of truth for agent instructions; CLAUDE.md is a one-line router"
description: "AGENTS.md is the source of truth for agent instructions; CLAUDE.md is a one-line router."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# AGENTS.md is the source of truth for agent instructions; CLAUDE.md is a one-line router

Every harness reads its own instruction file, and text copied between them drifts within weeks. We keep every always-on instruction in `AGENTS.md`, at the root and per directory, the format most harnesses read natively. Next to each one sits a `CLAUDE.md` that contains only `@AGENTS.md`. Claude Code reads `AGENTS.md` itself since version 2.1.277 (September 2026), but only when no `CLAUDE.md` is in the tree and not in every environment (Bedrock, Vertex and Foundry sessions, telemetry or hooks disabled, the setting is user or managed scope and cannot be committed); an import is never loaded twice, so the router is free insurance.

## Considered options

- No routers: one file less, but a Claude Code session where the feature is off silently gets no project instructions.
- Content in `CLAUDE.md`: Claude Code then stops reading `AGENTS.md`, and every other harness misses that content.

## Consequences

A router must hold nothing but the import; `tools/check_repo.py` fails otherwise. Any other file that carries instruction text is a pointer or a mirror, never a copy. Revisit when the setting can be committed with a repository.
