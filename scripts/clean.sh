#!/usr/bin/env bash

set -x
set -e

find ./ -name '*.pyc' -exec rm -f {} \;
find ./ -name '__pycache__' -exec rm -rf {} \;
find ./ -name '*~' -exec rm -f {} \;
rm -rf .cache
rm -rf .pytest_cache
rm -rf .mypy_cache
rm -rf .ruff_cache
rm -rf .ropeproject
rm -rf *.egg-info
rm -rf *.sqlite*
rm -rf *.db
rm -rf htmlcov
rm -rf docs/_build
