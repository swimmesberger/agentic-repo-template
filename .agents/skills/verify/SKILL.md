---
name: verify
description: Run every check this repository defines (tests, repository consistency, commit messages) and report what fails. Use before committing, after finishing a task, or when asked whether the build is green.
---
# Verify

1. From the repository root run `make check`, then `make check-commits` when the branch has a remote.
2. If `make` is unavailable, run the commands the Makefile's `check` and `check-commits` targets run. Never run other commands from `AGENTS.md` as part of this skill; some of them change files.
3. For every failing command, report the command and the last twenty lines of its output.
4. Do not fix anything as part of this skill. Fixing is a separate task with its own tests.
