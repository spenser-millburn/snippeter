#include <vector>
#include <algorithm>
#include <iostream>
#include <functional>

int main() {
    // Basic lambda
    auto add = [](int a, int b) { return a + b; };
    std::cout << add(3, 4) << std::endl;

    // Lambda with capture
    int multiplier = 3;
    auto multiply = [multiplier](int x) { return x * multiplier; };
    std::cout << multiply(5) << std::endl;

    // Capture by reference
    int counter = 0;
    auto increment = [&counter]() { counter++; };
    increment();
    increment();
    std::cout << "Counter: " << counter << std::endl;

    // Generic lambda (C++14)
    auto print = [](const auto& val) { std::cout << val << std::endl; };
    print(42);
    print("Hello");

    // Lambda with algorithms
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::for_each(v.begin(), v.end(), [](int x) {
        std::cout << x * 2 << " ";
    });
    std::cout << std::endl;

    // Lambda as return type
    auto makeAdder = [](int n) {
        return [n](int x) { return x + n; };
    };
    auto add10 = makeAdder(10);
    std::cout << add10(5) << std::endl;

    return 0;
}