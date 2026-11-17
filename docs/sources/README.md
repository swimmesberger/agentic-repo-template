---
type: Guide
title: "Sources"
description: "Raw material stored as received, with a frontmatter envelope."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Sources

Raw material as received: meeting notes, mails, requirements from outside, research reports. One file per source, named `YYYY-MM-DD-topic.md`, with frontmatter (`type: Source`, `title`, `description` saying where it came from) and the body exactly as it arrived. Never edited. Files that cannot carry frontmatter go to `../../raw/` with a source page here that points to them. Rules in [../guide.md](../guide.md).
