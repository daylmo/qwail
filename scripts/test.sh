#!/usr/bin/env bash

set -x
set -e

uv run pytest tests $@
