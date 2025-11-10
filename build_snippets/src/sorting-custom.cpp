#include <vector>
#include <algorithm>
#include <iostream>

struct Person {
    std::string name;
    int age;
};

// Comparator function
bool compareByAge(const Person& a, const Person& b) {
    return a.age < b.age;
}

int main() {
    std::vector<Person> people = {
        {"Alice", 30},
        {"Bob", 25},
        {"Charlie", 35}
    };

    // Using function
    std::sort(people.begin(), people.end(), compareByAge);

    // Using lambda
    std::sort(people.begin(), people.end(), [](const Person& a, const Person& b) {
        return a.name < b.name;
    });

    // Sorting pairs by second element
    std::vector<std::pair<int, int>> pairs = {{1, 5}, {2, 3}, {3, 8}};
    std::sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;
    });

    // Print results
    for (const auto& p : people) {
        std::cout << p.name << " (" << p.age << ")" << std::endl;
    }

    return 0;
}