#include <iostream>
#include <vector>
#include <numeric>
#include <string>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // Sum of elements
    int sum = std::accumulate(v.begin(), v.end(), 0);
    std::cout << "Sum: " << sum << std::endl;

    // Product of elements
    int product = std::accumulate(v.begin(), v.end(), 1, std::multiplies<int>());
    std::cout << "Product: " << product << std::endl;

    // Custom operation with lambda
    int sum_of_squares = std::accumulate(v.begin(), v.end(), 0,
        [](int acc, int x) { return acc + x * x; });
    std::cout << "Sum of squares: " << sum_of_squares << std::endl;

    // Concatenate strings
    std::vector<std::string> words = {"Hello", " ", "World", "!"};
    std::string sentence = std::accumulate(words.begin(), words.end(), std::string(""));
    std::cout << "Sentence: " << sentence << std::endl;

    // Count elements matching condition
    int count_even = std::accumulate(v.begin(), v.end(), 0,
        [](int acc, int x) { return acc + (x % 2 == 0 ? 1 : 0); });
    std::cout << "Even count: " << count_even << std::endl;

    return 0;
}