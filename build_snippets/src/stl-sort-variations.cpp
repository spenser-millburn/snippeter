#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // std::sort - regular sort (not stable)
    std::vector<int> v1 = {5, 2, 8, 1, 9, 3};
    std::sort(v1.begin(), v1.end());
    std::cout << "Sorted: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // Sort in descending order
    std::vector<int> v2 = {5, 2, 8, 1, 9, 3};
    std::sort(v2.begin(), v2.end(), std::greater<int>());
    std::cout << "Descending: ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // std::stable_sort - preserves relative order of equal elements
    std::vector<int> v3 = {5, 2, 8, 1, 9, 3};
    std::stable_sort(v3.begin(), v3.end());

    // std::partial_sort - sort first N elements
    std::vector<int> v4 = {5, 2, 8, 1, 9, 3, 7, 4};
    std::partial_sort(v4.begin(), v4.begin() + 3, v4.end());
    std::cout << "Partial sort (first 3): ";
    for (int x : v4) std::cout << x << " ";
    std::cout << std::endl;

    // std::nth_element - find nth smallest element
    std::vector<int> v5 = {5, 2, 8, 1, 9, 3, 7, 4};
    std::nth_element(v5.begin(), v5.begin() + 3, v5.end());
    std::cout << "4th smallest element: " << v5[3] << std::endl;

    // is_sorted - check if sorted
    bool sorted = std::is_sorted(v1.begin(), v1.end());
    std::cout << "Is v1 sorted: " << (sorted ? "yes" : "no") << std::endl;

    return 0;
}