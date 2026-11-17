.PHONY: check test check-repo check-commits

# Everything that runs offline. The commit check needs the remote's default branch: `make check-commits`.
check: test check-repo

test:
	python3 -m unittest discover -s tools/tests

check-repo:
	python3 tools/check_repo.py

check-commits:
	python3 tools/check_commits.py
