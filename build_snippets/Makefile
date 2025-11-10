# Makefile for C++ snippets

CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2

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
	@mkdir -p $(BIN_DIR)
	@echo "Compiling $<..."
	@$(CXX) $(CXXFLAGS) $< -o $@

# Clean target
clean:
	@echo "Cleaning build artifacts..."
	@rm -rf $(BIN_DIR)

# Phony targets
.PHONY: all clean
