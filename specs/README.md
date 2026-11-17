---
type: Format
title: "Specification format"
description: "How specs and plans are written in this repository."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Specifications

A spec says what a change must do before anyone, human or agent, writes code for it. The code is derived from the spec; the spec is the source and changes with the code (ADR 0007).

## Files

- `NNNN-slug.md`: the spec, four digits, sequential, never renumbered. One per feature or bounded change.
- `NNNN-slug.plan.md`: the plan, how the spec is built. Optional for small specs.

Both carry Open Knowledge Format frontmatter (`type: Specification` and `type: Plan`), like every page under `docs/`, so one checker and one reader handle all of them.

## Spec format

Sections in this order, headings as written:

- `## Intent`: one paragraph, in the terms of `../CONTEXT.md`, on what the user gets and why.
- `## User scenarios`: one `###` subsection per user story, highest priority first, marked `(P1)`, `(P2)`, each with acceptance scenarios in Given/When/Then form. Every story is testable on its own.
- `## Requirements`: numbered `FR-001`, `FR-002`, one testable sentence each, with the RFC 2119 keywords in capitals: MUST and MUST NOT for hard requirements, SHOULD and SHOULD NOT for strong defaults that need a reason to deviate, MAY for options. Nothing else in the spec uses these words in capitals. Write `[NEEDS CLARIFICATION: ...]` instead of guessing.
- `## Success criteria`: numbered `SC-001`, measurable outcomes that do not mention technology.
- `## Out of scope`: what this spec deliberately does not cover, so nobody builds it.
- Optional `## Decisions`: links to ADRs the spec depends on or creates.

A MUST is a test that has to pass before the spec is done, a SHOULD is a review question, a MAY is the implementer's choice. Acceptance scenarios may use EARS (`WHEN <event> THE SYSTEM SHALL <behaviour>`) instead of Given/When/Then when a story has many conditions; keep one form per spec.

A spec contains no implementation detail: no technology choices, no code references, no architecture.

## Plan format

Free-form, but it answers: which modules change, which interfaces appear, what data moves, at which seams the tests sit, and which ADRs it relies on or creates. Tasks for the tracker are cut from the plan, each naming the FR numbers it covers.

## Done

A spec is done when every acceptance scenario has a passing test named after it, every open `[NEEDS CLARIFICATION]` is resolved, and the pull request links the spec. `tools/check_repo.py` checks the sections, the numbering and the open clarifications of every spec whose `status` is `stable`.

## Why this format

Three families of documents exist. An RFC or design doc is a proposal under review for a change that affects several teams; its outcome is recorded here as an ADR. A feature spec, user stories with acceptance criteria, says what the user gets; that is what `specs/` holds. Generated specs (a skill such as Pocock's `to-spec`, or a framework such as spec-kit, Kiro or OpenSpec) carry the same content in a tool's layout. The format above uses parts older than any of these tools (user stories with Given/When/Then, numbered testable requirements, RFC 2119 keywords); the FR and SC numbering and the clarification marker come from spec-kit's public template. Because it keeps the what apart from the how, a skill can write it and any framework can take it over.

## Sources

- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174), requirement key words
- [spec-kit specification template](https://github.com/github/spec-kit/blob/main/templates/spec-template.md)
- [Kiro specs](https://kiro.dev/docs/specs/), EARS notation
- [Gergely Orosz, RFCs and design docs](https://blog.pragmaticengineer.com/rfcs-and-design-docs/)
