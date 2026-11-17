.PHONY: check test check-repo

check: test check-repo

test:
	python3 -m unittest discover -s tests

check-repo:
	python3 tools/check_repo.py
