#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // std::for_each - apply function to each element
    std::cout << "Print each: ";
    std::for_each(v.begin(), v.end(), [](int x) {
        std::cout << x << " ";
    });
    std::cout << std::endl;

    // Modify elements with for_each
    std::for_each(v.begin(), v.end(), [](int& x) {
        x *= 2;
    });
    std::cout << "After doubling: ";
    for (int x : v) std::cout << x << " ";
    std::cout << std::endl;

    // for_each with stateful lambda
    int sum = 0;
    std::for_each(v.begin(), v.end(), [&sum](int x) {
        sum += x;
    });
    std::cout << "Sum: " << sum << std::endl;

    // for_each with custom function object
    struct Counter {
        int count = 0;
        void operator()(int x) {
            if (x % 2 == 0) count++;
        }
    };
    Counter c = std::for_each(v.begin(), v.end(), Counter());
    std::cout << "Even count: " << c.count << std::endl;

    // Print with index
    int index = 0;
    std::for_each(v.begin(), v.end(), [&index](int x) {
        std::cout << "v[" << index++ << "] = " << x << std::endl;
    });

    return 0;
}