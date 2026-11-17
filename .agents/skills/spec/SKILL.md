---
name: spec
description: Write or update a feature specification in specs/ and its companion plan. Use before implementing a feature or behaviour change, when the user asks for a spec, requirements or acceptance criteria, or after a clarifying interview.
---
# Spec

The format lives in `specs/README.md`. Read it first; this skill is the procedure.

1. Read `CONTEXT.md` and the ADRs the feature touches. Use the glossary's terms; propose new ones instead of inventing synonyms.
2. If the intent is unclear, ask the user one question at a time until you can state it in one paragraph. Do not guess: write `[NEEDS CLARIFICATION: ...]` for what stays open.
3. Take the next free number and create `specs/NNNN-slug.md` with the sections from the README, in order. Requirements are numbered `FR-NNN`, one testable sentence each, RFC 2119 keywords in capitals.
4. Keep the how out. Modules, interfaces, data, test seams and technology go into `specs/NNNN-slug.plan.md`; anything hard to reverse becomes an ADR through the `adr` skill.
5. Run `make check`; it validates the sections and the numbering.
6. Stop and ask the user to approve the spec before any code is written. When an issue tracker is in use, link the spec from the issue.
