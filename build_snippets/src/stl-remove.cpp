#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // Remove specific value (erase-remove idiom)
    std::vector<int> v1 = {1, 2, 3, 2, 4, 2, 5};
    std::cout << "Original: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // std::remove doesn't actually remove, it moves elements
    auto new_end = std::remove(v1.begin(), v1.end(), 2);
    v1.erase(new_end, v1.end());
    std::cout << "After remove 2: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // Remove with predicate (remove even numbers)
    std::vector<int> v2 = {1, 2, 3, 4, 5, 6, 7, 8};
    v2.erase(
        std::remove_if(v2.begin(), v2.end(), [](int x) { return x % 2 == 0; }),
        v2.end()
    );
    std::cout << "After remove evens: ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // Remove elements greater than 5
    std::vector<int> v3 = {1, 8, 3, 9, 2, 7, 4};
    v3.erase(
        std::remove_if(v3.begin(), v3.end(), [](int x) { return x > 5; }),
        v3.end()
    );
    std::cout << "After remove > 5: ";
    for (int x : v3) std::cout << x << " ";
    std::cout << std::endl;

    return 0;
}