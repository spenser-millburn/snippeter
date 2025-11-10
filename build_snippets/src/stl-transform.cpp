#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <string>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::vector<int> result(v.size());

    // Square each element
    std::transform(v.begin(), v.end(), result.begin(),
        [](int x) { return x * x; });
    std::cout << "Squares: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;

    // Transform in-place
    std::transform(v.begin(), v.end(), v.begin(),
        [](int x) { return x * 2; });
    std::cout << "Doubled: ";
    for (int x : v) std::cout << x << " ";
    std::cout << std::endl;

    // Binary transform - add two vectors
    std::vector<int> v1 = {1, 2, 3};
    std::vector<int> v2 = {4, 5, 6};
    std::vector<int> sum(v1.size());
    std::transform(v1.begin(), v1.end(), v2.begin(), sum.begin(),
        [](int a, int b) { return a + b; });
    std::cout << "Sum of vectors: ";
    for (int x : sum) std::cout << x << " ";
    std::cout << std::endl;

    // Convert string to uppercase
    std::string str = "hello world";
    std::transform(str.begin(), str.end(), str.begin(), ::toupper);
    std::cout << "Uppercase: " << str << std::endl;

    return 0;
}