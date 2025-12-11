#!/bin/bash
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

# Development setup script for Structum v2.0
# This script installs all packages in editable mode for local development

set -e  # Exit on error

echo "🚀 Structum v2.0 - Development Setup"
echo "======================================"
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Check if we're in a virtual environment
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "⚠️  Warning: Not in a virtual environment"
    echo "   Consider running: python3 -m venv .venv && source .venv/bin/activate"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✓ Virtual environment: $VIRTUAL_ENV"
fi

echo ""
echo "📦 Installing packages in editable mode..."
echo ""

# Install core framework
echo "Installing structum (core framework)..."
pip install -e ./structum

echo ""
echo "Installing official plugins..."

# Install all plugins
pip install -e ./structum_tree
pip install -e ./structum_archive
pip install -e ./structum_clean
pip install -e ./structum_docs
pip install -e ./structum_plugins

echo ""
echo "Installing development dependencies..."
pip install -e "./structum[dev,mkdocs]"

echo ""
echo "✅ Setup complete!"
echo ""
echo "You can now run:"
echo "  structum --help              # See available commands"
echo "  structum plugins list        # List installed plugins"
echo "  structum tree .              # Visualize directory tree"
echo ""
echo "Development commands:"
echo "  pytest                       # Run tests"
echo "  ruff check src/              # Lint code"
echo "  mypy src/                    # Type checking"
echo ""
