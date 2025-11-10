#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {5, 2, 8, 1, 9, 3};

    // std::min and std::max for two values
    int a = 10, b = 20;
    std::cout << "Min: " << std::min(a, b) << std::endl;
    std::cout << "Max: " << std::max(a, b) << std::endl;

    // std::min_element and std::max_element
    auto min_it = std::min_element(v.begin(), v.end());
    auto max_it = std::max_element(v.begin(), v.end());
    std::cout << "Min element: " << *min_it << " at index " << (min_it - v.begin()) << std::endl;
    std::cout << "Max element: " << *max_it << " at index " << (max_it - v.begin()) << std::endl;

    // std::minmax - get both min and max
    auto [min_val, max_val] = std::minmax({5, 2, 8, 1, 9});
    std::cout << "Minmax: " << min_val << ", " << max_val << std::endl;

    // std::minmax_element - get both iterators
    auto [min_iter, max_iter] = std::minmax_element(v.begin(), v.end());
    std::cout << "Min: " << *min_iter << ", Max: " << *max_iter << std::endl;

    // With custom comparator
    auto abs_max = std::max_element(v.begin(), v.end(),
        [](int a, int b) { return std::abs(a) < std::abs(b); });
    std::cout << "Max by absolute value: " << *abs_max << std::endl;

    // Clamp value to range
    int value = 15;
    int clamped = std::clamp(value, 5, 10);
    std::cout << "Clamped " << value << " to [5,10]: " << clamped << std::endl;

    return 0;
}