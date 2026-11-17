---
name: verify
description: Run every check this repository defines and report what fails. Use before committing, after finishing a task, or when asked whether the build is green.
---
# Verify

1. From the repository root run `make check`.
2. If `make` is unavailable, run the commands listed under Commands in `AGENTS.md`, in that order.
3. For every failing command, report the command and the last twenty lines of its output.
4. Do not fix anything as part of this skill. Fixing is a separate task with its own tests.
