"""Acceptance tests for spec 0001, one per scenario, named after it."""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))

from check_repo import check  # noqa: E402

COPY = ["AGENTS.md", "CLAUDE.md", "CONTEXT.md", ".mcp.json", ".agents", ".claude", ".cursor", ".github", "docs", "specs"]


class RepositoryCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for name in COPY:
            src = REPO / name
            if src.is_dir() and not src.is_symlink():
                shutil.copytree(src, self.root / name, symlinks=True)
            else:
                shutil.copy2(src, self.root / name, follow_symlinks=False)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def edit(self, rel, old, new):
        path = self.root / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assertFinding(self, path, *words):
        findings = check(self.root)
        hits = [f for f in findings if f.startswith(path) and all(w in f for w in words)]
        self.assertTrue(hits, f"no finding for {path} with {words}; got {findings}")

    def test_a_consistent_repository_passes(self):
        self.assertEqual(check(self.root), [])

    def test_a_router_with_content_is_reported(self):
        self.write("CLAUDE.md", "@AGENTS.md\n\nAlways use tabs.\n")
        self.assertFinding("CLAUDE.md", "only `@AGENTS.md`")

    def test_an_agents_md_without_router_is_reported(self):
        self.write("app/AGENTS.md", "# app\n")
        self.assertFinding("app/AGENTS.md", "no CLAUDE.md router")

    def test_a_mirror_with_different_globs_is_reported(self):
        self.edit(".claude/rules/tests.md", '  - "**/*_test.*"\n', "")
        self.assertFinding(".claude/rules/tests.md", "differ from applyTo")

    def test_an_unlisted_page_is_reported(self):
        self.write("docs/runbook.md", "---\ntype: Runbook\n---\n# Runbook\n")
        self.assertFinding("docs/runbook.md", "not listed in docs/index.md")

    def test_a_page_without_type_is_reported(self):
        self.edit("docs/architecture.md", "type: Architecture page\n", "")
        self.assertFinding("docs/architecture.md", "`type`")

    def test_a_log_not_newest_first_is_reported(self):
        self.write("docs/log.md", "# Log\n\n## 2026-01-01\n\n* **Update**: [a](index.md)\n\n## 2026-02-01\n\n* **Update**: [b](index.md)\n")
        self.assertFinding("docs/log.md", "newest first")

    def test_an_approved_spec_without_a_required_section_is_reported(self):
        self.edit("specs/0001-repository-check.md", "## Out of scope\n", "## Not covered\n")
        self.assertFinding("specs/0001-repository-check.md", "`## Out of scope`")

    def test_an_approved_spec_with_a_duplicated_requirement_number_is_reported(self):
        self.edit("specs/0001-repository-check.md", "- FR-002:", "- FR-001:")
        self.assertFinding("specs/0001-repository-check.md", "FR-001")

    def test_a_draft_spec_with_an_open_clarification_passes(self):
        self.write("specs/0002-draft.md", "---\ntype: Specification\nstatus: draft\n---\n# Draft\n\n## Intent\n\n[NEEDS CLARIFICATION: who uses this?]\n")
        self.assertEqual(check(self.root), [])


if __name__ == "__main__":
    unittest.main()
