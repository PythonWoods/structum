#!/usr/bin/env bash

set -e

echo "📦 Cleaning previous builds..."
rm -rf dist *.egg-info

echo "📚 Building package..."
uv build

echo "🚀 Publishing to PyPI..."
uv publish

echo "✨ Done! Package published on PyPI."
