#!/usr/bin/env sh

set -x
set -e

uv run coverage run -m pytest --ff
