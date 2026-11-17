---
type: Specification
title: "Spec 0001: repository consistency check"
description: "What the repository checker must detect, so that the layout cannot drift unnoticed."
generated: { by: claude-code/claude-opus-5-5, at: 2026-11-17T12:00:00Z }
status: stable
---
# Spec 0001: repository consistency check

This spec describes the checker that ships with the template. It is a real spec for real code, kept as the worked example of the format. The checker's tests build their own fixture repository, so this file can be deleted or replaced without breaking them.

## Intent

Every convention of this repository (routers, mirrors, skills, the bundle, specs) is only worth something while it holds. A maintainer runs one command and learns every place where the layout has drifted, so drift is caught in the pull request that causes it and not by an agent that silently reads the wrong instructions.

## User scenarios

### A consistent repository passes (P1)

- Given a repository in which every convention holds, when the check runs, then it reports that the repository is consistent and exits with success.
- Given a repository with several kinds of drift, when the check runs, then it reports all of them in one run.
- Given a Markdown file without frontmatter in a raw or scratch folder, when the check runs, then it is not reported.

### Instruction drift is reported (P1)

- Given a `CLAUDE.md` with content beyond `@AGENTS.md`, when the check runs, then it names that router and fails.
- Given an `AGENTS.md` without a `CLAUDE.md` next to it, when the check runs, then it names the missing router and fails.
- Given a pattern rule whose mirror lists different globs, when the check runs, then it names the mirror and fails.
- Given a mirror whose body repeats the rule instead of pointing at it, when the check runs, then it names the mirror and fails.
- Given a mirror without a pattern rule as its source, when the check runs, then it names the mirror and fails.

### Skill and tool drift is reported (P1)

- Given a skill whose `name` differs from its folder, when the check runs, then it names the skill and fails.
- Given a missing link from a harness-specific path to the shared file, when the check runs, then it names the path and fails.
- Given an MCP server without a URL or command, when the check runs, then it names the server and fails.

### Bundle drift is reported (P1)

- Given a page under `docs/` that its index does not list, when the check runs, then it names the page and fails.
- Given a page without a frontmatter `type`, when the check runs, then it names the page and fails.
- Given a page whose `status` is not an OKF value, when the check runs, then it names the page and the value and fails.
- Given an index with a line that is neither a heading nor an entry, when the check runs, then it names the index and fails.
- Given a log whose dates are not newest first, when the check runs, then it names the log and fails.

### Spec drift is reported (P2)

- Given a spec without a status, when the check runs, then it names the spec and fails.
- Given an approved spec without a required section, when the check runs, then it names the spec and the section and fails.
- Given an approved spec with a duplicated requirement number, when the check runs, then it names the spec and the number and fails.
- Given a draft spec with an open clarification, when the check runs, then it does not fail on it.

## Requirements

The key words MUST, SHOULD and MAY are to be interpreted as described in RFC 2119 and RFC 8174.

- FR-001: The check MUST report every finding of a run, not only the first.
- FR-002: The check MUST fail when any finding exists and succeed when none does.
- FR-003: Each finding MUST name the file it concerns and SHOULD say what to do about it.
- FR-004: The check MUST verify that every `AGENTS.md` has a `CLAUDE.md` next to it whose only content is `@AGENTS.md`.
- FR-005: The check MUST verify that every pattern rule has a mirror with identical globs and a body of at most 60 words that names the rule's file, and that every mirror has a rule.
- FR-006: The check MUST verify that the shared skills folder and the shared MCP file are linked, or identically copied, for the harnesses that need their own path.
- FR-007: The check MUST verify that every skill has a `SKILL.md` with a `description` and a `name` equal to its folder, in lowercase letters, digits and single hyphens.
- FR-008: The check MUST verify that the MCP file uses the `mcpServers` key and that every server has a known type and the URL or command that type needs.
- FR-009: The check MUST verify that every page of the bundle, the glossary and every spec carry frontmatter with a `type` and, when set, a `status` of draft, stable or deprecated; that every page is listed in its nearest index; that indexes hold only headings and entries whose local links resolve; and that the log is newest first with a linked page in every entry.
- FR-010: The check MUST verify that every spec has a status, and that every approved spec has the required sections in order, unique requirement and success-criterion numbers, and no open clarification.
- FR-011: The check MUST skip dependency, cache, scratch and raw folders.
- FR-012: The check MUST NOT need anything beyond the language runtime to run.

## Success criteria

- SC-001: Every acceptance scenario above has a passing test named after it.
- SC-002: The check finishes in under one second on this repository.

## Out of scope

Fixing findings automatically; checking the content or quality of pages; validating links to external URLs; checking that a change has a log entry, which needs the diff and is left to review.

## Decisions

- [ADR 0001](../docs/adr/0001-agents-md-is-the-source-of-truth.md), [0002](../docs/adr/0002-pattern-rules-have-one-source-and-a-mirror.md), [0003](../docs/adr/0003-symlinks-for-skills-and-cursor-mcp.md), [0005](../docs/adr/0005-docs-is-the-okf-bundle.md), [0007](../docs/adr/0007-one-spec-file-per-feature.md)
