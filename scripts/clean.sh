#!/usr/bin/env sh

set -ex

rm -rf **/__pycache__
rm -rf .benchmarks
rm -rf .cache
rm -rf .coverage
rm -rf .pytest_cache
rm -rf .mypy_cache
rm -rf .ruff_cache
rm -rf .ropeproject
rm -rf *.egg-info
rm -rf *.sqlite*
rm -rf *.db
rm -rf htmlcov
rm -rf docs/_build
