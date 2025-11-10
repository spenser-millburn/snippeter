#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v1 = {2, 4, 6, 8, 10};
    std::vector<int> v2 = {1, 3, 5, 7, 9};
    std::vector<int> v3 = {1, 2, 3, 4, 5};

    // std::all_of - check if all elements satisfy condition
    bool all_even = std::all_of(v1.begin(), v1.end(), [](int x) { return x % 2 == 0; });
    std::cout << "All even in v1: " << (all_even ? "yes" : "no") << std::endl;

    // std::any_of - check if any element satisfies condition
    bool any_even = std::any_of(v2.begin(), v2.end(), [](int x) { return x % 2 == 0; });
    std::cout << "Any even in v2: " << (any_even ? "yes" : "no") << std::endl;

    // std::none_of - check if no elements satisfy condition
    bool none_negative = std::none_of(v3.begin(), v3.end(), [](int x) { return x < 0; });
    std::cout << "None negative in v3: " << (none_negative ? "yes" : "no") << std::endl;

    // Practical examples
    std::vector<int> ages = {25, 30, 35, 28, 32};

    bool all_adults = std::all_of(ages.begin(), ages.end(), [](int age) { return age >= 18; });
    std::cout << "All adults: " << (all_adults ? "yes" : "no") << std::endl;

    bool any_senior = std::any_of(ages.begin(), ages.end(), [](int age) { return age >= 65; });
    std::cout << "Any senior: " << (any_senior ? "yes" : "no") << std::endl;

    bool none_minor = std::none_of(ages.begin(), ages.end(), [](int age) { return age < 18; });
    std::cout << "None minor: " << (none_minor ? "yes" : "no") << std::endl;

    return 0;
}