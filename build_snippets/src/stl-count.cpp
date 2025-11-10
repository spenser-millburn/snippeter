#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    std::vector<int> v = {1, 2, 3, 2, 4, 2, 5, 2};

    // std::count - count occurrences of value
    int count_twos = std::count(v.begin(), v.end(), 2);
    std::cout << "Number of 2s: " << count_twos << std::endl;

    // std::count_if - count with predicate
    int count_even = std::count_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; });
    std::cout << "Even numbers: " << count_even << std::endl;

    // Count in strings
    std::string str = "hello world";
    int count_l = std::count(str.begin(), str.end(), 'l');
    std::cout << "Letter 'l' count: " << count_l << std::endl;

    // Count with complex predicate
    int count_large = std::count_if(v.begin(), v.end(), [](int x) { return x > 3; });
    std::cout << "Numbers > 3: " << count_large << std::endl;

    return 0;
}