---
type: Architecture Decision Record
title: "Pattern-scoped rules have one source and one mirror"
description: "Pattern-scoped rules have one source and one mirror."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Pattern-scoped rules have one source and one mirror

There is no cross-tool format for rules scoped by file pattern: Copilot reads `applyTo`, Claude Code `paths`, Cursor `globs`. We write each pattern rule once in `.github/instructions/`, because every Copilot surface including code review reads it, and mirror it into `.claude/rules/` with identical globs and a one-sentence body that points at the source. Symlinks fail because the frontmatter keys differ; `@` imports fail because Claude Code loads them regardless of `paths`.

## Consequences

The globs exist twice and must stay identical; `tools/check_repo.py` fails when they differ or a mirror grows a body. Cursor gets directory scoping through nested `AGENTS.md` files only.
