---
type: Architecture Decision Record
title: "Commit messages and pull request titles follow Conventional Commits"
description: "Commit messages and pull request titles follow Conventional Commits."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Commit messages and pull request titles follow Conventional Commits

When agents write most commits, free-form messages turn into a history nobody can scan and no tool can use. We follow Conventional Commits 1.0.0 for every commit message and for pull request titles, which become the commit on a squash merge: a type, an optional scope, `!` for breaking changes, an imperative description. The format is the one agents already know best, it is checkable with a few lines of code, and it lets changelogs and version numbers be derived from history (release-please, semantic-release) when a team wants that.

## Considered options

- Free-form messages: nothing to check, nothing to derive.
- Gitmoji or a house format: less widely known, so agents and new colleagues get it wrong more often.

## Consequences

`tools/check_commits.py` checks every commit of a pull request and its title in CI, and `tools/hooks/commit-msg` checks locally when enabled with `git config core.hooksPath tools/hooks`. Merge commits are skipped; `fixup!`, `squash!` and `amend!` commits pass locally and fail in CI, so they get squashed before merge.
