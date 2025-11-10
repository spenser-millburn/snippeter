#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::string str = "10 20 30 40 50";
    std::stringstream ss(str);

    std::vector<int> numbers;
    int num;
    while (ss >> num) {
        numbers.push_back(num);
    }

    // Process numbers
    for (int n : numbers) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}