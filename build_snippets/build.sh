#!/bin/bash
# Convenience script to build all snippets with g++

set -e

echo "Compiling C++ snippets..."

# Compiler settings
CXX="g++"
CXXFLAGS="-std=c++17 -Wall -Wextra -O2"

# Create bin directory if it doesn't exist
mkdir -p bin

# Compile each snippet
compiled=0
failed=0

for cpp_file in src/*.cpp; do
    filename=$(basename "$cpp_file" .cpp)
    echo -n "  Compiling $filename... "

    if $CXX $CXXFLAGS "$cpp_file" -o "bin/$filename" 2>/dev/null; then
        echo "✓"
        ((compiled++))
    else
        echo "✗"
        ((failed++))
    fi
done

echo ""
echo "Build complete!"
echo "  Compiled: $compiled"
echo "  Failed: $failed"
echo ""
echo "Executables are in: $(pwd)/bin"
