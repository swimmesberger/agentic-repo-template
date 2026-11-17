# Agentic repository template

A repository layout that lets any coding agent (Claude Code, GitHub Copilot, Codex, Cursor and every other harness that follows the public conventions) work on a project from the repository alone, and keeps it that way with one checker. Use it as a GitHub template, or copy the parts you need into an existing repository.

It combines five things that each answer a different question:

| Part | Answers | Here |
|---|---|---|
| Harness standards | Where does an agent start? | `AGENTS.md` (root and per directory), `.agents/skills/`, `.mcp.json`; one-line routers and symlinks for the exceptions |
| Knowledge format | How do knowledge files look? | `docs/` is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (OKF 0.2) bundle: frontmatter on every page, an index, a log |
| Decisions | Why is it like this? | Short architecture decision records in `docs/adr/`, glossary in `GLOSSARY.md` |
| Spec-driven work | What must a change do before it is built? | One spec per feature in `specs/`, the how in a plan next to it |
| Way of working | How does a change get from idea to merge? | [`docs/workflow.md`](docs/workflow.md): steps with human checkpoints, right-sizing, practices; Matt Pocock's engineering skills, preconfigured; Conventional Commits |

Agents read `AGENTS.md`; this README is for people.

## Principles

1. **Commit the standard form, route the exception.** Instructions are written once, in `AGENTS.md`. Every other instruction file is a one-line router, a mirror whose body only points at the source, or a symlink. Never a copy. ([ADR 0001](docs/adr/0001-agents-md-is-the-source-of-truth.md), [0002](docs/adr/0002-pattern-rules-have-one-source-and-a-mirror.md), [0003](docs/adr/0003-symlinks-for-skills-and-cursor-mcp.md))
2. **The repository is the memory.** Harness memory is switched off. What an agent would remember goes into a file that is reviewed and versioned: a rule, an ADR, a glossary term, a spec, a log entry. ([ADR 0006](docs/adr/0006-the-repository-is-the-memory.md))
3. **Pointers, not payload.** `AGENTS.md` holds the rules that always apply and one-line pointers phrased by task ("a term is unclear: read `GLOSSARY.md`"). Everything behind a pointer costs nothing until it is needed.
4. **Knowledge is a format, not a folder.** `docs/` follows OKF strictly: every page has frontmatter with a `type`, every page is in the index, every change is in the log, newest first. Raw files that cannot carry frontmatter stay outside. ([ADR 0005](docs/adr/0005-docs-is-the-okf-bundle.md))
5. **Spec before code, what apart from how.** A spec states user scenarios, numbered requirements in RFC 2119 language and success criteria; implementation decisions go into a plan file or an ADR. The spec survives a later move to any spec framework. ([ADR 0007](docs/adr/0007-one-spec-file-per-feature.md))
6. **Humans approve, agents execute.** The agent does the work; a person approves the spec and the plan before code exists and reads every diff before it is merged. The amount of process scales with the change, from a one-line fix to a migration. ([docs/workflow.md](docs/workflow.md))
7. **History is readable.** Commit messages and pull request titles follow Conventional Commits; the person who commits owns the change. ([ADR 0008](docs/adr/0008-conventional-commits.md))
8. **A checker, not discipline.** `make check` fails when a router, mirror, link, index, log or spec drifts, and CI rejects commits that are not Conventional Commits.

## The map

| Path | Role |
|---|---|
| `AGENTS.md` | Source. Always-on instructions, layout, commands, where artefacts go, task-shaped pointers. Nested `AGENTS.md` files per directory add local rules; the closest one wins |
| `CLAUDE.md` | Router. Only `@AGENTS.md`, next to every `AGENTS.md`. Claude Code reads `AGENTS.md` itself in most setups; the router covers the rest, and content of its own would stop Claude Code from reading `AGENTS.md` at all |
| `GLOSSARY.md` | The glossary and nothing else: project terms, one or two sentences each, with the words to avoid. Named so because public domain-modeling skills look for it there |
| `docs/index.md` | The map of the knowledge bundle: headings and `* [Title](path) - description` entries only |
| `docs/guide.md` | What lives where in `docs/` and the rules for keeping it |
| `docs/log.md` | What changed and why, `## YYYY-MM-DD` headings, newest first; add with `tools/log_add.py` |
| `docs/adr/` | Decisions: when to write one and the format in `docs/adr/README.md`, the list in `docs/adr/index.md` |
| `docs/workflow.md` | How we work: the steps and checkpoints, how much process a change needs, practices, which skill does what |
| `docs/agents/` | Where the engineering skills find the issue tracker and the domain docs (what `setup-matt-pocock-skills` would write) |
| `docs/architecture.md` | Compiled page: the system's shape and why, citing ADRs and sources |
| `docs/sources/` | Raw material that can carry frontmatter, stored as received, never edited |
| `specs/` | One spec per feature (`NNNN-slug.md`) and its plan (`NNNN-slug.plan.md`); format in `specs/README.md` |
| `.agents/skills/` | Procedures in the Agent Skills format: ours (`adr`, `spec`, `verify`) and Matt Pocock's engineering skills, deployed by APM |
| `.claude/skills` | Symlink to `.agents/skills` |
| `.github/instructions/*.instructions.md` | Source of pattern-scoped rules (`applyTo`), read by every Copilot surface including code review |
| `.claude/rules/*.md` | Mirror for Claude Code: same globs under `paths`, body is one pointer sentence |
| `.github/copilot-instructions.md` | Pointer for Copilot surfaces that do not read `AGENTS.md` |
| `.mcp.json`, `.cursor/mcp.json` | MCP servers under `mcpServers`; the Cursor file is a symlink |
| `.claude/settings.json`, `.vscode/settings.json` | Memory off, nested `AGENTS.md` on |
| `apm.yml`, `apm.lock.yaml` | The shared skills, pinned to a commit, through the Agent Package Manager |
| `tools/check_repo.py` | The layout checker |
| `tools/check_commits.py`, `tools/hooks/commit-msg` | The commit message check, for CI and as a local hook |
| `tools/log_add.py` | Adds a log entry in the right place |
| `.github/workflows/` | `check` on every push, `commits` on every pull request |

## How to work with it

The whole process, with the practices and a skill per step, is in [docs/workflow.md](docs/workflow.md). A typical feature:

1. `/grill-with-docs`: the agent interviews you about the idea, one question at a time, and writes settled terms into `GLOSSARY.md` and decisions into `docs/adr/`.
2. `/to-spec`: it turns the conversation into `specs/NNNN-slug.md` and a plan next to it, and opens an issue that links them. You approve the spec and the plan.
3. `/to-tickets`, when the work needs more than one session: thin vertical slices as issues with blocking edges.
4. `/implement` per ticket, in a fresh session each time: test-first at the agreed seams, then `code-review` on two axes (spec and standards), then a Conventional Commit.
5. You read the diff, `make check` and CI pass, you merge. What the agent got wrong twice becomes a rule in `AGENTS.md`.

A one-line fix skips to step 4. Spec frameworks (spec-kit, OpenSpec, Kiro) name the same steps; if a team adopts one, `AGENTS.md` has the rules for letting it in.

## Adopting it

New repository: click "Use this template", then

1. Replace the placeholders in `AGENTS.md`, `GLOSSARY.md` and `docs/architecture.md` (search for `TODO`).
2. Keep or delete the example spec `specs/0001-repository-check.md`; it specifies the checker in this repository and shows the format.
3. Add nested `AGENTS.md` files with a `CLAUDE.md` router next to each when subprojects need their own rules.
4. Enable the commit hook with `git config core.hooksPath tools/hooks`, and run `make check`.
5. Using GitLab or local issues instead of GitHub: replace `docs/agents/issue-tracker.md` with the matching seed from `setup-matt-pocock-skills`, or install that skill and run it.

Existing repository: copy `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/`, `.github/instructions/`, `.github/copilot-instructions.md`, `.mcp.json`, `.cursor/`, `docs/`, `specs/`, `GLOSSARY.md` and `tools/`, move existing instruction text into `AGENTS.md`, and let `make check` tell you what is left.

Shared skills: the deployed skills are committed, so a clone works without any tool. To add, remove or update one, edit `apm.yml`, run `apm install` with the [Agent Package Manager](https://github.com/microsoft/apm), review the diff of `.agents/skills/` and commit it with `apm.lock.yaml`. Repositories that still have `CONTEXT.md` from before September 2026: rename it to `GLOSSARY.md` (ADR 0004).

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
- [mattpocock/skills](https://github.com/mattpocock/skills) (MIT), deployed into `.agents/skills/`
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- Birgitta Böckeler, [Understanding spec-driven development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

## License

MIT, see [LICENSE](LICENSE).
