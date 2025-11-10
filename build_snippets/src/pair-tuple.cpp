#include <utility>
#include <tuple>
#include <iostream>

int main() {
    // Pair
    std::pair<int, std::string> p1 = {1, "one"};
    std::pair<int, std::string> p2 = std::make_pair(2, "two");

    std::cout << p1.first << " " << p1.second << std::endl;

    // Structured binding (C++17)
    auto [num, str] = p1;
    std::cout << num << " " << str << std::endl;

    // Tuple
    std::tuple<int, double, std::string> t = {1, 3.14, "pi"};

    std::cout << std::get<0>(t) << " ";
    std::cout << std::get<1>(t) << " ";
    std::cout << std::get<2>(t) << std::endl;

    // Structured binding with tuple
    auto [i, d, s] = t;
    std::cout << i << " " << d << " " << s << std::endl;

    return 0;
}