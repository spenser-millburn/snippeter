#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    // std::find - search for value
    auto it = std::find(v.begin(), v.end(), 5);
    if (it != v.end()) {
        std::cout << "Found: " << *it << " at position " << (it - v.begin()) << std::endl;
    }

    // std::find_if - search with predicate
    auto even = std::find_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; });
    if (even != v.end()) {
        std::cout << "First even: " << *even << std::endl;
    }

    // std::find_if_not - search for element not matching predicate
    auto not_small = std::find_if_not(v.begin(), v.end(), [](int x) { return x < 5; });
    if (not_small != v.end()) {
        std::cout << "First not small: " << *not_small << std::endl;
    }

    // Check if element exists
    bool has_seven = std::find(v.begin(), v.end(), 7) != v.end();
    std::cout << "Has 7: " << (has_seven ? "yes" : "no") << std::endl;

    return 0;
}