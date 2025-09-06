#!/usr/bin/env bash

set -x
set -e


uv run mypy .
uv run ruff check --fix .
uv run tombi lint .
