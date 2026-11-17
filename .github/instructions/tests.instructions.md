---
applyTo: "**/tests/**,**/*.test.*,**/*_test.*"
---
# Test files

- Name a test after the behaviour it proves; for a spec's acceptance scenario, after the scenario.
- Test through the public interface. Never import private helpers into a test.
- Do not mock the module under test. Mock only what crosses a process or network boundary.
- One behaviour per test. Several behaviours mean several tests.
- A failing test that documents a known bug is allowed if it is marked as expected failure and links the issue.
