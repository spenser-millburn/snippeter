#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> src = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    // std::copy - copy all elements
    std::vector<int> dest1(src.size());
    std::copy(src.begin(), src.end(), dest1.begin());
    std::cout << "Copied: ";
    for (int x : dest1) std::cout << x << " ";
    std::cout << std::endl;

    // std::copy_if - copy only elements matching predicate
    std::vector<int> evens;
    std::copy_if(src.begin(), src.end(), std::back_inserter(evens),
        [](int x) { return x % 2 == 0; });
    std::cout << "Evens: ";
    for (int x : evens) std::cout << x << " ";
    std::cout << std::endl;

    // std::replace - replace value
    std::vector<int> v1 = {1, 2, 3, 2, 4, 2, 5};
    std::replace(v1.begin(), v1.end(), 2, 99);
    std::cout << "Replace 2 with 99: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // std::replace_if - replace with predicate
    std::vector<int> v2 = {1, 2, 3, 4, 5, 6, 7, 8};
    std::replace_if(v2.begin(), v2.end(),
        [](int x) { return x % 2 == 0; }, 0);
    std::cout << "Replace evens with 0: ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // std::fill - fill with value
    std::vector<int> v3(10);
    std::fill(v3.begin(), v3.end(), 42);
    std::cout << "Filled with 42: ";
    for (int x : v3) std::cout << x << " ";
    std::cout << std::endl;

    // std::fill_n - fill first n elements
    std::vector<int> v4(10, 0);
    std::fill_n(v4.begin(), 5, 99);
    std::cout << "First 5 filled with 99: ";
    for (int x : v4) std::cout << x << " ";
    std::cout << std::endl;

    return 0;
}