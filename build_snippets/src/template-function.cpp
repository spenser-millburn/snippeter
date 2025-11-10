#include <iostream>
#include <vector>
#include <string>

// Basic template function
template<typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Template with multiple type parameters
template<typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}

// Template function with container
template<typename T>
void printVector(const std::vector<T>& vec) {
    for (const auto& elem : vec) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

// Template with constraints (concept-like, C++20 style)
template<typename T>
T sumVector(const std::vector<T>& vec) {
    T sum = T();
    for (const auto& elem : vec) {
        sum += elem;
    }
    return sum;
}

// Template class
template<typename T>
class Container {
private:
    T value;
public:
    Container(T val) : value(val) {}
    T getValue() const { return value; }
    void setValue(T val) { value = val; }
};

int main() {
    std::cout << maximum(10, 20) << std::endl;
    std::cout << maximum(3.14, 2.71) << std::endl;
    std::cout << maximum<std::string>("apple", "banana") << std::endl;

    std::cout << add(5, 3.14) << std::endl;

    std::vector<int> v1 = {1, 2, 3, 4, 5};
    printVector(v1);

    std::vector<std::string> v2 = {"hello", "world"};
    printVector(v2);

    Container<int> c1(42);
    std::cout << c1.getValue() << std::endl;

    return 0;
}