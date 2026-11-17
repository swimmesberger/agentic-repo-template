---
type: Glossary
title: "Glossary"
description: "The project's own terms, opinionated, with the words to avoid."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: draft
---
# TODO: project name

TODO: one sentence on the domain.

This file is the glossary and nothing else: the project's own terms, one or two sentences each, opinionated, with the words to avoid. No general programming concepts, project facts, instructions or decisions; those live in `AGENTS.md`, `docs/`, `specs/` and `docs/adr/`. The name `GLOSSARY.md` is the one public domain-modeling skills look for (ADR 0004).

## Language

**Spec**:
The file in `specs/` that states what a feature must do: user scenarios, numbered requirements, success criteria. The source the code is built from.
_Avoid_: requirements doc, story, ticket

**Plan**:
The `.plan.md` file next to a spec that states how the feature is built.
_Avoid_: design, technical spec

**Bundle**:
The `docs/` folder as an Open Knowledge Format bundle: every page with frontmatter, an index, a log.
_Avoid_: wiki, knowledge base

**Router**:
A `CLAUDE.md` whose only content is `@AGENTS.md`.
_Avoid_: stub, link file
