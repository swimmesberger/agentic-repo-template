# TODO: project name

TODO: one or two sentences on what this project is and who uses it. Humans: read README.md. Agents: this file and the files it points to are your instructions.

## Layout

- TODO: the source folders, one line each. A folder with rules of its own gets its own `AGENTS.md` and a `CLAUDE.md` router next to it.
- `CLAUDE.md` files: one-line routers (`@AGENTS.md`). Never put content in them; a `CLAUDE.md` with content of its own stops Claude Code from reading the `AGENTS.md` next to it.
- `CONTEXT.md`: the glossary.
- `docs/`: project knowledge beyond the code, kept as an Open Knowledge Format bundle. `docs/index.md` lists every page, `docs/guide.md` says what lives where and how the folder is kept.
- `specs/`: what each feature must do, and how it is built; format in `specs/README.md`.
- `.agents/skills/`: procedures in the Agent Skills format.
- `tools/`: `check_repo.py` keeps this layout consistent, `log_add.py` adds log entries.

## Commands

- All checks: `make check`
- Tests: TODO
- Repository consistency: `python3 tools/check_repo.py`
- Log entry: `python3 tools/log_add.py "**Update**: what and why, with a [link](page.md)"`

## Rules that always apply

- Use the terms in `CONTEXT.md`; do not invent synonyms. A new term goes into the glossary in the same change.
- Record decisions that are hard to reverse in `docs/adr/`, with the `adr` skill.
- Every behaviour change comes with a test. Run `make check` before you report a task as done.
- Spec and code change together: a pull request that changes behaviour updates its spec, or says why not.
- Never commit secrets. `.env` files are ignored; do not paste their contents into prompts.
- Prefer the smallest change that satisfies the spec. Do not add dependencies without an ADR.
- Do not use harness memory; it is off in the committed settings. Anything worth remembering goes into a file: a rule here, an ADR, a glossary term, a spec, or the log. Working notes and session handoffs go into `.scratch/`, which git ignores.

## Workflow and where artefacts go

The flow is clarify, specify, plan, decompose, implement, verify. Skills that produce artefacts write them here, whatever location they would otherwise use:

- Decisions and terms found while clarifying (grilling, domain modeling): `docs/adr/` and `CONTEXT.md`, in the formats those files define.
- Specs: one file per feature, `specs/NNNN-slug.md`, in the format of `specs/README.md`, written with the `spec` skill or any skill that produces a spec. A skill that wants to publish a spec to an issue tracker writes the file first and links it from the issue.
- Implementation and testing decisions: `specs/NNNN-slug.plan.md` next to the spec, or an ADR when they are hard to reverse. Never in the spec.
- Tickets: in the issue tracker, each linking the spec and naming the FR numbers it covers. Local tickets in `.scratch/<feature>/issues/` are allowed for solo work, but git ignores them, so they are no evidence.
- Research notes: `docs/sources/YYYY-MM-DD-topic.md` with `type: Source` and the URLs they rest on. Files that cannot carry frontmatter (PDF, HTML, office files) stay outside `docs/`, in `raw/`.
- Anything created under `docs/`, by whichever skill: frontmatter with a `type`, an entry in the index of its folder (`docs/index.md`, `docs/adr/index.md`) and an entry in `docs/log.md`, in the same change. Skills do not know this format; `make check` fails until it is done.
- Reviews check two axes: standards (this file, nested `AGENTS.md` files, ADRs, `CONTEXT.md`) and spec (the spec file, its FR numbers, a test per acceptance scenario).

## If a spec framework is added

One per repository. It keeps its own folder outside `docs/` (`.specify/`, `openspec/`, `.kiro/`), because everything under `docs/` must be OKF conformant. Its rules file (constitution, config, steering) points to this file and does not repeat it. If it wants a managed block in an agent context file, the block goes here, never into a `CLAUDE.md` router. Its skills share `.agents/skills/`; install and update them only with its own command. Existing specs move into its layout in one change.

## Pointers: read these when the task calls for it

- A term is unclear, or you are about to name something: `CONTEXT.md`.
- Module boundaries, why the code is shaped as it is, whether something may be added: `docs/architecture.md`, then the ADRs it cites.
- A decision seems odd, or you are about to make one that is hard to reverse: `docs/adr/index.md` and the `adr` skill.
- What a feature must do: its file in `specs/`; how it is built: the `.plan.md` next to it.
- What happened before, or why a page says what it says: `docs/log.md`, then `docs/sources/`.
- Anything you learned about the project and would otherwise remember: put it in one of the files above, list new pages in their index, and add a log entry in the same change.

## Where the rest lives

- Pattern rules: `.github/instructions/*.instructions.md` (source), mirrored for Claude Code in `.claude/rules/`.
- Procedures: `.agents/skills/*/SKILL.md`.
- Tool servers: `.mcp.json`.
- TODO: tracker, dashboards, external docs, one line each.
