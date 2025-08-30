#!/usr/bin/env sh

set -x
set -e

uv run ruff check --fix .
