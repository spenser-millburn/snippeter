# C++ Snippets Build

This directory contains all the C++ snippets as individual compilable files.

## Statistics

- Total snippets: 37
- Successfully compiled: 35
- Failed to compile: 2

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


### Algorithms

- ✓ `binary-search`
- ✓ `dfs-template`
- ✓ `bfs-template`
- ✓ `sorting-custom`

### Basic

- ✓ `basic-main`
- ✗ `class-template`
- ✗ `header-guard`

### Common Patterns

- ✓ `sliding-window`
- ✓ `two-pointers`
- ✓ `backtracking`
- ✓ `monotonic-stack`
- ✓ `prefix-sum`

### Competitive Programming

- ✓ `mod-arithmetic`
- ✓ `gcd-lcm`

### Data Structures

- ✓ `vector-ops`
- ✓ `map-set`
- ✓ `priority-queue`
- ✓ `pair-tuple`

### I/O

- ✓ `fast-io`
- ✓ `file-io`
- ✓ `string-stream`

### Modern C++

- ✓ `lambda-functions`
- ✓ `range-for`
- ✓ `smart-pointers`
- ✓ `template-function`

### STL

- ✓ `stl-find`
- ✓ `stl-count`
- ✓ `stl-accumulate`
- ✓ `stl-transform`
- ✓ `stl-remove`
- ✓ `stl-sort-variations`
- ✓ `stl-minmax`
- ✓ `stl-predicates`
- ✓ `stl-unique`
- ✓ `stl-partition`
- ✓ `stl-copy-replace`
- ✓ `stl-for-each`

## Compilation Errors


### class-template

```
build_snippets/src/class-template.cpp: In member function ‘void ClassName::display() const’:
build_snippets/src/class-template.cpp:28:14: error: ‘cout’ is not a member of ‘std’
   28 |         std::cout << "Data: " << data << std::endl;
      |              ^~~~
build_snippets/src/class-template.cpp:1:1: note: ‘std::cout’ is defined in header ‘<iostream>’; this is probably fixable by adding ‘#include <iostream>’
  +++ |+#include <iostream>
    1 | class ClassName {
build_snippets/src/class-template.cpp:28:47: error: ‘endl’ is not a member of ‘std’
   28 |         std::cout << "Data: " << data << std::endl;
      |                                               ^~~~
build_snippets/src/class-template.cpp:1:1: note: ‘std::endl’ is defined in header ‘<ostream>’; this is probably fixable by adding ‘#include <ostream>’
  +++ |+#include <ostream>
    1 | class ClassName {

```

### header-guard

```
/usr/bin/ld: /usr/lib/gcc/x86_64-redhat-linux/14/../../../../lib64/crt1.o: in function `_start':
(.text+0x1b): undefined reference to `main'
collect2: error: ld returned 1 exit status

```
