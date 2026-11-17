---
type: Architecture Decision Record
title: "Skills and the Cursor MCP file are symlinks, with copies as the Windows fallback"
description: "Skills and the Cursor MCP file are symlinks, with copies as the Windows fallback."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Skills and the Cursor MCP file are symlinks, with copies as the Windows fallback

Skills live in `.agents/skills/`, which Codex, Copilot and Cursor read; `.claude/skills` is a symlink to it. `.mcp.json` is the MCP source under the `mcpServers` key, read by Claude Code, Copilot CLI and VS Code; `.cursor/mcp.json` is a symlink because the shape is identical. Symlinks keep one copy wherever they work.

## Consequences

Windows checkouts need `core.symlinks=true` and symlink rights, or the two links replaced by copies; the checker accepts identical copies. Our own skills use only the `name` and `description` fields so every harness loads them; vendored skills may carry harness-specific fields such as `disable-model-invocation`, which harnesses that do not know them ignore.
