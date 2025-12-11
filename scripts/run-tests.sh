#!/bin/bash
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

# Monorepo test runner for Structum v2.0
# Runs tests for all packages in the monorepo

set -e  # Exit on error

echo "🧪 Structum v2.0 - Monorepo Test Runner"
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test results tracking
TOTAL_PACKAGES=0
PASSED_PACKAGES=0
FAILED_PACKAGES=()

# Function to run tests for a package
run_package_tests() {
    local package_name=$1
    local package_dir=$2

    TOTAL_PACKAGES=$((TOTAL_PACKAGES + 1))

    echo "📦 Testing: $package_name"
    echo "   Location: $package_dir"

    if [ ! -d "$package_dir" ]; then
        echo -e "${YELLOW}   ⚠️  Package directory not found, skipping${NC}"
        return
    fi

    # Check if tests directory exists
    if [ ! -d "$package_dir/tests" ]; then
        echo -e "${YELLOW}   ⚠️  No tests directory, skipping${NC}"
        return
    fi

    # Run pytest for this package
    if pytest "$package_dir/tests" --tb=short -q 2>/dev/null; then
        echo -e "${GREEN}   ✅ PASSED${NC}"
        PASSED_PACKAGES=$((PASSED_PACKAGES + 1))
    else
        echo -e "${RED}   ❌ FAILED${NC}"
        FAILED_PACKAGES+=("$package_name")
    fi

    echo ""
}

# Parse arguments
COVERAGE=false
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --coverage|-c)
            COVERAGE=true
            shift
            ;;
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --help|-h)
            echo "Usage: ./run-tests.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --coverage, -c    Run with coverage report"
            echo "  --verbose, -v     Verbose output"
            echo "  --help, -h        Show this help"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Test all packages in order
echo "Running tests for all packages..."
echo ""

# Core framework
run_package_tests "structum (core)" "./structum"

# Official plugins
run_package_tests "structum_tree" "./structum_tree"
run_package_tests "structum_archive" "./structum_archive"
run_package_tests "structum_clean" "./structum_clean"
run_package_tests "structum_docs" "./structum_docs"
run_package_tests "structum_plugins" "./structum_plugins"

# Summary
echo "=========================================="
echo "📊 Test Summary"
echo "=========================================="
echo "Total packages tested: $TOTAL_PACKAGES"
echo -e "Passed: ${GREEN}$PASSED_PACKAGES${NC}"
echo -e "Failed: ${RED}${#FAILED_PACKAGES[@]}${NC}"

if [ ${#FAILED_PACKAGES[@]} -gt 0 ]; then
    echo ""
    echo "Failed packages:"
    for pkg in "${FAILED_PACKAGES[@]}"; do
        echo "  - $pkg"
    done
    echo ""
    exit 1
fi

echo ""
echo -e "${GREEN}✅ All tests passed!${NC}"
exit 0
