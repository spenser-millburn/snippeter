#include <vector>
#include <map>
#include <iostream>

int main() {
    // Vector iteration
    std::vector<int> v = {1, 2, 3, 4, 5};

    // Read-only
    for (const auto& elem : v) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // Modify elements
    for (auto& elem : v) {
        elem *= 2;
    }

    // Copy (less efficient)
    for (auto elem : v) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // Map iteration with structured binding
    std::map<std::string, int> m = {
        {"apple", 5},
        {"banana", 3},
        {"orange", 7}
    };

    for (const auto& [key, value] : m) {
        std::cout << key << ": " << value << std::endl;
    }

    // Traditional iterator when index is needed
    for (size_t i = 0; i < v.size(); ++i) {
        std::cout << "v[" << i << "] = " << v[i] << std::endl;
    }

    return 0;
}