---
type: Architecture Decision Record
title: "One spec file per feature in specs/, the how in a plan next to it"
description: "One spec file per feature in specs/, the how in a plan next to it."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# One spec file per feature in specs/, the how in a plan next to it

Agents build what they are told, so the cheapest review is of what a change must do, before any code exists. We write one spec per feature as `specs/NNNN-slug.md` in a fixed format (intent, user scenarios with Given/When/Then, numbered requirements in RFC 2119 language, success criteria, out of scope) and keep implementation and testing decisions in `NNNN-slug.plan.md` next to it. The format is built from parts older than any spec tool, and the what/how split is the one every spec framework makes, so a spec survives a later move to spec-kit, OpenSpec or Kiro.

## Considered options

- Specs only in the issue tracker: invisible to an agent working from the repository, and lost when the tracker changes.
- A spec framework from the start: a tool-owned folder and command set before the team knows it needs one.

## Consequences

A spec is done when every acceptance scenario has a passing test named after it and the pull request links the spec. Spec and code change in the same pull request. `tools/check_repo.py` checks the sections and the requirement numbering.
