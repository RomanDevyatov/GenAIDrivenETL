#!/usr/bin/env bash
set -e

echo "Installing dev dependencies..."
poetry install --no-root

echo "Running Black (autoformat)..."
poetry run black genaidrivenetl tests

echo "Running isort (import sort)..."
poetry run isort genaidrivenetl tests

echo "Running Flake8 (PEP8 checks)..."
poetry run flake8 genaidrivenetl tests

echo "Linting and formatting complete!"
