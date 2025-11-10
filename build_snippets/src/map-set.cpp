#include <map>
#include <set>
#include <iostream>

int main() {
    // Map operations
    std::map<std::string, int> m;
    m["apple"] = 5;
    m["banana"] = 3;
    m.insert({"orange", 7});

    // Check existence
    if (m.find("apple") != m.end()) {
        std::cout << "Found apple: " << m["apple"] << std::endl;
    }

    // Iterate
    for (const auto& [key, value] : m) {
        std::cout << key << ": " << value << std::endl;
    }

    // Set operations
    std::set<int> s = {1, 2, 3, 4, 5};
    s.insert(6);
    s.erase(3);

    // Check existence
    if (s.count(4) > 0) {
        std::cout << "4 is in the set" << std::endl;
    }

    return 0;
}