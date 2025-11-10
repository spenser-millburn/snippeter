# Snippeter - C++ Code Snippets

A beautiful tool for managing and accessing C++ code snippets with both CLI and web interfaces.

## Features

- 37 pre-loaded C++ snippets covering:
  - Basic structures and boilerplate
  - Input/Output operations
  - Data structures (vectors, maps, sets, priority queues)
  - Algorithms (binary search, DFS, BFS)
  - Modern C++ features (lambdas, smart pointers, templates)
  - Competitive programming helpers (modular arithmetic, GCD/LCM)
  - Common patterns (sliding window, two pointers, backtracking, monotonic stack, prefix sum)
  - STL algorithms (find, count, accumulate, transform, sort variations, min/max, predicates, etc.)

- **CLI Features:**
  - Rich terminal UI with syntax highlighting
  - Interactive browsing mode
  - Search and filter capabilities
  - Fuzzy search with match scoring
  - Interactive fuzzy finder (fzf-style)
  - Clipboard integration
  - Statistics and random snippet features

- **Web Interface:**
  - Modern black and white minimalist design
  - Real-time search and category filtering
  - Grid layout with responsive design
  - Modal view for full snippet code with syntax highlighting
  - One-click copy to clipboard
  - Statistics dashboard

## Installation

### Quick Install

```bash
# Clone or navigate to the directory
cd snippeter

# Install dependencies
pip install -r requirements.txt

# Install as a CLI tool
pip install -e .
```

### Alternative: Run Directly

```bash
# Install dependencies
pip install typer rich pyperclip

# Run the CLI directly
python cli.py --help
```

## Usage

### List all snippets
```bash
snippeter list
```

### Filter snippets by keyword
```bash
snippeter list --filter search
snippeter list -f graph
```

### Show a specific snippet
```bash
snippeter show binary-search
```

### Show and copy to clipboard
```bash
snippeter show dfs --copy
```

### Search snippets
```bash
snippeter search vector
snippeter search "priority queue"
```

### Fuzzy search snippets
```bash
# Fuzzy search with match scores
snippeter fuzzy "heap"
snippeter fuzzy "dfs graph"

# Fuzzy search and copy best match
snippeter fuzzy "binary tree" --copy

# Show more results (default is 5)
snippeter fuzzy "sorting" --limit 10
```

### Interactive fuzzy finder (like fzf)
```bash
# Launch interactive fuzzy search
snippeter fuzzyi

# Auto-copy selected snippet
snippeter fuzzyi --copy
```

### Get snippet info
```bash
snippeter info lambda-functions
```

### Copy snippet directly to clipboard
```bash
snippeter copy fast-io
```

### Interactive mode
```bash
snippeter interactive
```

### Get a random snippet
```bash
snippeter random-snippet
```

### View collection statistics
```bash
snippeter stats
```

## Web Interface

The web interface provides a modern browser-based way to browse and copy snippets.

### Starting the Web Server

```bash
# Using the CLI (recommended)
snippeter web

# Or with the Fish function
snip web

# Custom port
snippeter web --port 3000

# Don't open browser automatically
snippeter web --no-browser
```

The server will start at `http://localhost:8000` (or your specified port) and automatically open in your default browser. The `snippets.json` file is automatically generated if needed.

### Features

- **Search**: Real-time search across snippet names, descriptions, and code
- **Filter by Category**: Dropdown filter to show only snippets from specific categories
- **Grid Layout**: Clean, responsive grid showing all snippets at a glance
- **Modal View**: Click any snippet card to view the full code with C++ syntax highlighting
- **Syntax Highlighting**: Powered by Highlight.js with Atom One Dark theme
- **Copy**: One-click copy to clipboard from cards or modal
- **Statistics**: Live stats showing total snippets, categories, and filtered count

## Available Snippets

| Category | Snippets |
|----------|----------|
| **Basic** | basic-main, class, header-guard |
| **I/O** | fast-io, file-io, string-stream |
| **Data Structures** | vector-ops, map-set, priority-queue, pair-tuple |
| **Algorithms** | binary-search, dfs, bfs, sorting-custom |
| **Modern C++** | lambda-functions, range-for, smart-pointers, template-function |
| **Competitive Programming** | mod-arithmetic, gcd-lcm |
| **Common Patterns** | sliding-window, two-pointers, backtracking, monotonic-stack, prefix-sum |
| **STL** | stl-find, stl-count, stl-accumulate, stl-transform, stl-remove, stl-sort-variations, stl-minmax, stl-predicates, stl-unique, stl-partition, stl-copy-replace, stl-for-each |

## Requirements

- Python 3.7+
- typer
- rich
- pyperclip (for clipboard functionality)
- thefuzz (for fuzzy searching)
- python-Levenshtein (optional, for faster fuzzy matching)
- InquirerPy (for interactive fuzzy finder)

## Development

To add more snippets, edit the `snippets.py` file and add entries to the `CPP_SNIPPETS` list:

```python
{
    "name": "snippet-name",
    "category": "Category Name",
    "description": "Brief description",
    "snippet": """
    // Your C++ code here
    """
}
```

## Building and Testing Snippets

You can compile all snippets to verify they work correctly:

```bash
# Run the build script
python build_snippets.py

# This creates a build_snippets/ directory with:
# - src/: All snippets as individual .cpp files
# - bin/: Compiled executables
# - build.sh: Script to rebuild all
# - Makefile: For building with make

# Run a compiled snippet
cd build_snippets
./bin/binary-search
./bin/stl-find

# Rebuild all
./build.sh
# or
make
```

The build script compiles all snippets using g++ with `-std=c++17 -Wall -Wextra -O2`.

## License

MIT License
