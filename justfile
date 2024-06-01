default: help

# Show this info message
help:
  just --list

# Setup the Python venv for development
setup:
  rm -r .venv
  python3 -m venv .venv
  .venv/bin/pip install --upgrade pip
  .venv/bin/pip install -r requirements/requirements.txt

# Check if the project is following the guidelines
check:
  mypy src/knuckles
  mypy tests
  ruff check --fix
  ruff format

# Spin up a local documentation of the project
docs:
  .venv/bin/mkdocs serve

# Run all tests
test:
  .venv/bin/pytest

# Generate a new lock file for all the deps
lock: lock-dev-deps lock-docs-deps lock-tests-deps

[private]
lock-dev-deps:
  .venv/bin/pip-compile --extra=dev --output-file=requirements/requirements-dev.txt pyproject.toml

[private]
lock-docs-deps:
  .venv/bin/pip-compile --extra=docs --output-file=requirements/requirements-docs.txt pyproject.toml

[private]
lock-tests-deps:
  .venv/bin/pip-compile --extra=tests --output-file=requirements/requirements-tests.txt pyproject.toml
