# Agentic repository template

A repository layout that lets any coding agent (Claude Code, GitHub Copilot, Codex, Cursor and every other harness that follows the public conventions) work on a project from the repository alone, and keeps it that way with one checker. Use it as a GitHub template, or copy the parts you need into an existing repository.

It combines four things that each answer a different question:

| Part | Answers | Here |
|---|---|---|
| Harness standards | Where does an agent start? | `AGENTS.md` (root and per directory), `.agents/skills/`, `.mcp.json`; one-line routers and symlinks for the exceptions |
| Knowledge format | How do knowledge files look? | `docs/` is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (OKF 0.2) bundle: frontmatter on every page, an index, a log |
| Decisions | Why is it like this? | Short architecture decision records in `docs/adr/`, glossary in `CONTEXT.md` |
| Spec-driven work | What must a change do before it is built? | One spec per feature in `specs/`, the how in a plan next to it |

Agents read `AGENTS.md`; this README is for people.

## Principles

1. **Commit the standard form, route the exception.** Instructions are written once, in `AGENTS.md`. Every other instruction file is a one-line router, a mirror whose body only points at the source, or a symlink. Never a copy. ([ADR 0001](docs/adr/0001-agents-md-is-the-source-of-truth.md), [0002](docs/adr/0002-pattern-rules-have-one-source-and-a-mirror.md), [0003](docs/adr/0003-symlinks-for-skills-and-cursor-mcp.md))
2. **The repository is the memory.** Harness memory is switched off. What an agent would remember goes into a file that is reviewed and versioned: a rule, an ADR, a glossary term, a spec, a log entry. ([ADR 0006](docs/adr/0006-the-repository-is-the-memory.md))
3. **Pointers, not payload.** `AGENTS.md` holds the rules that always apply and one-line pointers phrased by task ("a term is unclear: read `CONTEXT.md`"). Everything behind a pointer costs nothing until it is needed.
4. **Knowledge is a format, not a folder.** `docs/` follows OKF strictly: every page has frontmatter with a `type`, every page is in the index, every change is in the log, newest first. Raw files that cannot carry frontmatter stay outside. ([ADR 0005](docs/adr/0005-docs-is-the-okf-bundle.md))
5. **Spec before code, what apart from how.** A spec states user scenarios, numbered requirements in RFC 2119 language and success criteria; implementation decisions go into a plan file or an ADR. The spec survives a later move to any spec framework. ([ADR 0007](docs/adr/0007-one-spec-file-per-feature.md))
6. **A checker, not discipline.** `make check` fails when a router, mirror, link, index, log or spec drifts. Wire it into CI.

## The map

| Path | Role |
|---|---|
| `AGENTS.md` | Source. Always-on instructions, layout, commands, where artefacts go, task-shaped pointers. Nested `AGENTS.md` files per directory add local rules; the closest one wins |
| `CLAUDE.md` | Router. Only `@AGENTS.md`, next to every `AGENTS.md`. Claude Code reads `AGENTS.md` itself in most setups; the router covers the rest, and content of its own would stop Claude Code from reading `AGENTS.md` at all |
| `CONTEXT.md` | The glossary and nothing else: project terms, one or two sentences each, with the words to avoid. Named so because public domain-modeling skills look for it there |
| `docs/index.md` | The map of the knowledge bundle: headings and `* [Title](path) - description` entries only |
| `docs/guide.md` | What lives where in `docs/` and the rules for keeping it |
| `docs/log.md` | What changed and why, `## YYYY-MM-DD` headings, newest first; add with `tools/log_add.py` |
| `docs/adr/` | Decisions: when to write one and the format in `docs/adr/README.md`, the list in `docs/adr/index.md` |
| `docs/architecture.md` | Compiled page: the system's shape and why, citing ADRs and sources |
| `docs/sources/` | Raw material that can carry frontmatter, stored as received, never edited |
| `specs/` | One spec per feature (`NNNN-slug.md`) and its plan (`NNNN-slug.plan.md`); format in `specs/README.md` |
| `.agents/skills/` | Procedures in the Agent Skills format (`adr`, `spec`, `verify`), only the `name` and `description` fields so every harness loads them |
| `.claude/skills` | Symlink to `.agents/skills` |
| `.github/instructions/*.instructions.md` | Source of pattern-scoped rules (`applyTo`), read by every Copilot surface including code review |
| `.claude/rules/*.md` | Mirror for Claude Code: same globs under `paths`, body is one pointer sentence |
| `.github/copilot-instructions.md` | Pointer for Copilot surfaces that do not read `AGENTS.md` |
| `.mcp.json`, `.cursor/mcp.json` | MCP servers under `mcpServers`; the Cursor file is a symlink |
| `.claude/settings.json`, `.vscode/settings.json` | Memory off, nested `AGENTS.md` on |
| `apm.yml` | Optional: shared skills through the Agent Package Manager |
| `tools/check_repo.py` | The checker. `tools/log_add.py` adds log entries |

## Workflow

The steps every spec-driven method shares, with the artefact each leaves in this layout. Right-size it: a one-line fix goes straight to implement with a test; a feature runs all of it.

| Step | Artefact | Human checkpoint |
|---|---|---|
| Ground rules | `AGENTS.md`, `CONTEXT.md`, `docs/adr/` | Changed like code, through review |
| Clarify | Answers to the agent's questions; decisions become ADRs, terms enter `CONTEXT.md` | The human answers, the agent asks |
| Specify | `specs/NNNN-slug.md` | Approve the spec, the cheapest review there is |
| Plan | `specs/NNNN-slug.plan.md`, ADRs for what is hard to reverse | Review the plan |
| Decompose | Tickets in the tracker (or `.scratch/`), each naming its FR numbers | Agree order and slices |
| Implement | Code and tests, one slice per fresh session | Read every diff |
| Verify | Review on two axes: spec (a test per acceptance scenario) and standards (`AGENTS.md`, ADRs, glossary) | Automated first, human second |
| Learn | A rule after the second correction, a superseded ADR, an updated spec | Decide what becomes permanent |

Spec frameworks (spec-kit, OpenSpec, Kiro) and skill sets such as [mattpocock/skills](https://github.com/mattpocock/skills) are namings of these steps. The layout is built so Pocock's skills run without configuration (`CONTEXT.md` at the root, `docs/adr/`), and `AGENTS.md` tells them where to put specs and tickets. If a team adopts a framework, `AGENTS.md` has the rules for letting it in.

## Adopting it

New repository: click "Use this template", then

1. Replace the placeholders in `AGENTS.md`, `CONTEXT.md` and `docs/architecture.md` (search for `TODO`).
2. Keep or delete the example spec `specs/0001-repository-check.md`; it specifies the checker in this repository and shows the format.
3. Add nested `AGENTS.md` files with a `CLAUDE.md` router next to each when subprojects need their own rules.
4. Run `make check`.

Existing repository: copy `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/`, `.github/instructions/`, `.github/copilot-instructions.md`, `.mcp.json`, `.cursor/`, `docs/`, `specs/`, `CONTEXT.md` and `tools/`, move existing instruction text into `AGENTS.md`, and let `make check` tell you what is left.

Optional shared skills: install the [Agent Package Manager](https://github.com/microsoft/apm) and run `apm install`. It deploys the skills declared in `apm.yml` into `.agents/skills/`, which every harness reads (Claude Code through the symlink); commit the deployed skills and `apm.lock.yaml`.

## Known limits

- Codex keeps MCP servers in `~/.codex/config.toml`, outside the repository.
- Copilot code review on GitHub.com reads `.github/copilot-instructions.md` and the pattern rules, not `AGENTS.md`. A rule that must reach code review belongs in a pattern rule.
- GitHub's server-side Copilot Memory cannot be switched off from a file; repository admins do it in the repository's Copilot settings.
- Symlinks need `core.symlinks=true` and symlink rights on Windows. The checker accepts identical copies as a fallback.
- Product behaviour is as of November 2026; settings names move, check the vendor docs.

## Sources

- [AGENTS.md](https://agents.md/), [Agent Skills](https://agentskills.io/), [Model Context Protocol](https://modelcontextprotocol.io/)
- [Open Knowledge Format, specification 0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) and Andrej Karpathy's [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern it formalises
- Michael Nygard, [Documenting architecture decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174), requirement key words; [spec-kit's spec template](https://github.com/github/spec-kit/blob/main/templates/spec-template.md)
- [mattpocock/skills](https://github.com/mattpocock/skills)

## License

MIT, see [LICENSE](LICENSE).
