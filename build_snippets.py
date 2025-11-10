#!/usr/bin/env python3
"""
Build script to create individual C++ files for each snippet and compile with g++
"""

import os
import shutil
import subprocess
from pathlib import Path
from snippets import CPP_SNIPPETS

# Configuration
BUILD_DIR = Path("build_snippets")
SRC_DIR = BUILD_DIR / "src"
BIN_DIR = BUILD_DIR / "bin"

# Compiler settings
CXX = "g++"
CXXFLAGS = ["-std=c++17", "-Wall", "-Wextra", "-O2"]

def clean_build_dir():
    """Remove existing build directory"""
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)
    SRC_DIR.mkdir(parents=True)
    BIN_DIR.mkdir(parents=True)
    print(f"✓ Created build directory: {BUILD_DIR}")

def create_snippet_files():
    """Create a .cpp file for each snippet"""
    created_files = []

    for snippet in CPP_SNIPPETS:
        filename = f"{snippet['name']}.cpp"
        filepath = SRC_DIR / filename

        # Write snippet to file
        with open(filepath, 'w') as f:
            f.write(snippet['snippet'])

        created_files.append(snippet['name'])
        print(f"  Created: {filename}")

    return created_files

def compile_snippets():
    """Compile all snippets using g++"""
    print("\nCompiling snippets...")

    compiled = []
    failed = []

    for snippet in CPP_SNIPPETS:
        src_file = SRC_DIR / f"{snippet['name']}.cpp"
        bin_file = BIN_DIR / snippet['name']

        # Build compile command
        cmd = [CXX] + CXXFLAGS + [str(src_file), "-o", str(bin_file)]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            compiled.append(snippet['name'])
            print(f"  ✓ Compiled: {snippet['name']}")
        except subprocess.CalledProcessError as e:
            failed.append((snippet['name'], e.stderr))
            print(f"  ✗ Failed: {snippet['name']}")

    return compiled, failed

def generate_readme(compiled, failed):
    """Generate README for the build directory"""
    readme_content = f"""# C++ Snippets Build

This directory contains all the C++ snippets as individual compilable files.

## Statistics

- Total snippets: {len(CPP_SNIPPETS)}
- Successfully compiled: {len(compiled)}
- Failed to compile: {len(failed)}

## Running

Executables are in the `bin/` directory:

```bash
# Run a snippet
./bin/binary-search
./bin/sliding-window
./bin/stl-find
# etc.
```

## Building

To rebuild all snippets:

```bash
./build.sh
```

Or compile a single snippet:

```bash
g++ -std=c++17 -Wall -Wextra -O2 src/binary-search.cpp -o bin/binary-search
```

## Snippets by Category

"""

    # Group by category
    by_category = {}
    for snippet in CPP_SNIPPETS:
        cat = snippet['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(snippet['name'])

    for category, snippets in sorted(by_category.items()):
        readme_content += f"\n### {category}\n\n"
        for name in snippets:
            status = "✓" if name in compiled else "✗"
            readme_content += f"- {status} `{name}`\n"

    if failed:
        readme_content += "\n## Compilation Errors\n\n"
        for name, error in failed:
            readme_content += f"\n### {name}\n\n```\n{error}\n```\n"

    readme_path = BUILD_DIR / "README.md"
    with open(readme_path, 'w') as f:
        f.write(readme_content)

    print(f"✓ Created README.md")

def generate_build_script():
    """Generate a convenience build script"""
    build_script = f"""#!/bin/bash
# Convenience script to build all snippets with g++

set -e

echo "Compiling C++ snippets..."

# Compiler settings
CXX="{CXX}"
CXXFLAGS="{' '.join(CXXFLAGS)}"

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
"""

    script_path = BUILD_DIR / "build.sh"
    with open(script_path, 'w') as f:
        f.write(build_script)

    # Make executable
    os.chmod(script_path, 0o755)
    print(f"✓ Created build.sh")

def generate_makefile():
    """Generate a Makefile for building snippets"""
    makefile_content = f"""# Makefile for C++ snippets

CXX = {CXX}
CXXFLAGS = {' '.join(CXXFLAGS)}

SRC_DIR = src
BIN_DIR = bin

# Find all source files
SOURCES = $(wildcard $(SRC_DIR)/*.cpp)
# Generate executable names
EXECUTABLES = $(patsubst $(SRC_DIR)/%.cpp,$(BIN_DIR)/%,$(SOURCES))

# Default target
all: $(EXECUTABLES)

# Pattern rule for building executables
$(BIN_DIR)/%: $(SRC_DIR)/%.cpp
\t@mkdir -p $(BIN_DIR)
\t@echo "Compiling $<..."
\t@$(CXX) $(CXXFLAGS) $< -o $@

# Clean target
clean:
\t@echo "Cleaning build artifacts..."
\t@rm -rf $(BIN_DIR)

# Phony targets
.PHONY: all clean
"""

    makefile_path = BUILD_DIR / "Makefile"
    with open(makefile_path, 'w') as f:
        f.write(makefile_content)

    print(f"✓ Created Makefile")

def main():
    print("Building C++ snippets structure...\n")

    # Clean and create directories
    clean_build_dir()

    # Create snippet files
    print(f"\nCreating {len(CPP_SNIPPETS)} snippet files...")
    created_files = create_snippet_files()

    # Compile all snippets
    compiled, failed = compile_snippets()

    # Generate build files
    print("\nGenerating build files...")
    generate_readme(compiled, failed)
    generate_build_script()
    generate_makefile()

    # Summary
    print("\n" + "="*50)
    print("Summary:")
    print(f"  Total snippets: {len(created_files)}")
    print(f"  Successfully compiled: {len(compiled)}")
    print(f"  Failed to compile: {len(failed)}")
    print(f"  Output directory: {BUILD_DIR}")
    print(f"  Source directory: {SRC_DIR}")
    print(f"  Binary directory: {BIN_DIR}")
    print("="*50)

    if failed:
        print("\n⚠ Some snippets failed to compile. Check README.md for details.")

    print("\nTo rebuild:")
    print(f"  cd {BUILD_DIR}")
    print("  ./build.sh")
    print("\nOr use make:")
    print(f"  cd {BUILD_DIR}")
    print("  make")
    print("\nTo run a snippet:")
    print(f"  cd {BUILD_DIR}")
    print("  ./bin/binary-search")

if __name__ == "__main__":
    main()
