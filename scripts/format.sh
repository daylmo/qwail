#!/usr/bin/env bash

set -x
set -e

uv run ruff check .
uv run ruff format .
uv run tombi format .
