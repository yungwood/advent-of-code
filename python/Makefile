WORKDIR?=.
VENVDIR?=$(WORKDIR)/.venv
VENV=$(VENVDIR)/bin

.ONESHELL:
.PHONY: help dev clean lint test

help: ## Display this help (default)
	@echo "Available targets:"
	@awk -F ':|##' '/^[a-zA-Z0-9_-]+:.*##/ {printf "  %-15s %s\n", $$1, $$3}' $(MAKEFILE_LIST)

dev: venv ## Set up everything for local development

clean: ## Clean up all local development files
	rm -rfv .venv

lint: venv ## Run linting
	.venv/bin/pdm run pylint aoc
	.venv/bin/flake8 .

test: venv ## Run tests
	.venv/bin/pdm run pytest

venv: .venv .venv/touchfile ## Set up or update python virtual environment

.venv:
	python3 -mvenv .venv

.venv/touchfile: pyproject.toml
	.venv/bin/pip install -e .[dev]
	touch .venv/touchfile
