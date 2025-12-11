#!/bin/bash
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

# Build all packages in the monorepo
# Creates distribution packages (wheel + sdist) for PyPI upload

set -e  # Exit on error

echo "📦 Structum v2.0 - Build All Packages"
echo "======================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Build counters
TOTAL_PACKAGES=0
BUILT_PACKAGES=0

# Function to build a package
build_package() {
    local package_name=$1
    local package_dir=$2

    TOTAL_PACKAGES=$((TOTAL_PACKAGES + 1))

    echo "📦 Building: $package_name"
    echo "   Location: $package_dir"

    if [ ! -d "$package_dir" ]; then
        echo -e "${YELLOW}   ⚠️  Package directory not found, skipping${NC}"
        return
    fi

    # Clean old builds
    rm -rf "$package_dir/dist" "$package_dir/build" "$package_dir"/*.egg-info

    # Build with hatchling
    (cd "$package_dir" && python -m build --no-isolation 2>/dev/null)

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}   ✅ Built successfully${NC}"
        BUILT_PACKAGES=$((BUILT_PACKAGES + 1))

        # Show built files
        if [ -d "$package_dir/dist" ]; then
            echo "   Built files:"
            ls -lh "$package_dir/dist" | grep -v "^total" | awk '{print "     -", $9, "("$5")"}'
        fi
    else
        echo "   ❌ Build failed"
    fi

    echo ""
}

# Check if build tool is available
if ! command -v python -m build &> /dev/null; then
    echo "❌ Python build tool not found"
    echo "   Install with: pip install build"
    exit 1
fi

echo "Building all packages..."
echo ""

# Build all packages
build_package "structum (core)" "./structum"
build_package "structum_tree" "./structum_tree"
build_package "structum_archive" "./structum_archive"
build_package "structum_clean" "./structum_clean"
build_package "structum_docs" "./structum_docs"
build_package "structum_plugins" "./structum_plugins"

# Summary
echo "=========================================="
echo "📊 Build Summary"
echo "=========================================="
echo "Total packages: $TOTAL_PACKAGES"
echo -e "Built successfully: ${GREEN}$BUILT_PACKAGES${NC}"
echo ""

if [ $BUILT_PACKAGES -eq $TOTAL_PACKAGES ]; then
    echo -e "${GREEN}✅ All packages built successfully!${NC}"
    echo ""
    echo "Distribution packages are in each package's dist/ directory"
    echo ""
    echo "To upload to PyPI:"
    echo "  twine upload structum/dist/*"
    echo "  twine upload structum_tree/dist/*"
    echo "  # ... etc"
    echo ""
    echo "Or use: ./scripts/publish-all.sh"
else
    echo "⚠️  Some packages failed to build"
    exit 1
fi
