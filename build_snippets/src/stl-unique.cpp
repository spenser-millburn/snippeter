#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // Remove consecutive duplicates
    std::vector<int> v1 = {1, 1, 2, 2, 2, 3, 3, 4, 5, 5};
    std::cout << "Original: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    auto new_end = std::unique(v1.begin(), v1.end());
    v1.erase(new_end, v1.end());
    std::cout << "After unique: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // Remove all duplicates (sort first, then unique)
    std::vector<int> v2 = {3, 1, 2, 1, 3, 2, 4, 3, 2};
    std::sort(v2.begin(), v2.end());
    v2.erase(std::unique(v2.begin(), v2.end()), v2.end());
    std::cout << "All duplicates removed: ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // Unique with custom comparator
    std::vector<int> v3 = {1, -1, 2, -2, 3, 3, 4};
    auto abs_end = std::unique(v3.begin(), v3.end(),
        [](int a, int b) { return std::abs(a) == std::abs(b); });
    v3.erase(abs_end, v3.end());
    std::cout << "Unique by absolute value: ";
    for (int x : v3) std::cout << x << " ";
    std::cout << std::endl;

    return 0;
}