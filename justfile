# Default recipe of the justfile
default: help

# Show this info message
help:
  just --list

# Setup the Python venv for development
setup: generic-setup
  .venv/bin/pip install -r requirements/requirements.txt

[private]
generic-setup:
  rm -rf .venv
  python3 -m venv .venv
  .venv/bin/pip install --upgrade pip

[private]
setup-check: generic-setup
  .venv/bin/pip install -r requirements/requirements-check.txt

[private]
setup-tests: generic-setup
  .venv/bin/pip install .
  .venv/bin/pip install -r requirements/requirements-tests.txt

[private]
setup-docs: generic-setup
  .venv/bin/pip install .
  .venv/bin/pip install -r requirements/requirements-docs.txt

# Check if the project is following the guidelines
check:
  .venv/bin/mypy src
  .venv/bin/ruff check --fix
  .venv/bin/ruff format

# Install a pre-commit hook to ensure that the CI will pass
install-hook: uninstall-hook
  cp scripts/pre-commit.sh .git/hooks/pre-commit
  chmod +x .git/hooks/pre-commit

# Uninstall the pre-commit hook
uninstall-hook:
  rm -f .git/hooks/pre-commit

# Spin up a local documentation of the project
docs:
  .venv/bin/mkdocs serve

# Run all tests
test:
  .venv/bin/pytest

# Generate a new lock file for all the deps
lock: lock-dev-deps lock-check-deps lock-docs-deps lock-tests-deps

[private]
lock-dev-deps:
  .venv/bin/pip-compile --extra=dev --output-file=requirements/requirements-dev.txt pyproject.toml

[private]
lock-check-deps:
  .venv/bin/pip-compile --extra=check --output-file=requirements/requirements-check.txt pyproject.toml

[private]
lock-docs-deps:
  .venv/bin/pip-compile --extra=docs --output-file=requirements/requirements-docs.txt pyproject.toml

[private]
lock-tests-deps:
  .venv/bin/pip-compile --extra=tests --output-file=requirements/requirements-tests.txt pyproject.toml

[private]
deploy-docs:
  .venv/bin/mkdocs gh-deploy --force
