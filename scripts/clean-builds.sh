#!/bin/bash
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

# Clean build artifacts from all packages

set -e

echo "🧹 Cleaning build artifacts..."
echo ""

# Function to clean a package
clean_package() {
    local package_dir=$1
    local package_name=$(basename "$package_dir")

    if [ -d "$package_dir" ]; then
        echo "  Cleaning: $package_name"

        # Remove build artifacts
        rm -rf "$package_dir/dist"
        rm -rf "$package_dir/build"
        rm -rf "$package_dir"/*.egg-info
        rm -rf "$package_dir"/src/*.egg-info

        # Remove Python cache
        find "$package_dir" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
        find "$package_dir" -type f -name "*.pyc" -delete 2>/dev/null || true
        find "$package_dir" -type f -name "*.pyo" -delete 2>/dev/null || true

        # Remove pytest cache
        rm -rf "$package_dir/.pytest_cache"

        # Remove coverage files
        rm -f "$package_dir/.coverage"
        rm -rf "$package_dir/htmlcov"
    fi
}

# Clean all packages
clean_package "./structum"
clean_package "./structum_tree"
clean_package "./structum_archive"
clean_package "./structum_clean"
clean_package "./structum_docs"
clean_package "./structum_plugins"

# Clean root artifacts
echo "  Cleaning: root directory"
rm -rf .pytest_cache
rm -f .coverage
rm -rf htmlcov
find . -maxdepth 1 -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

echo ""
echo "✅ All build artifacts cleaned"
