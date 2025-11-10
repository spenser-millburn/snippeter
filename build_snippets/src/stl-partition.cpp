#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // std::partition - rearrange elements by predicate
    std::vector<int> v1 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    auto partition_point = std::partition(v1.begin(), v1.end(),
        [](int x) { return x % 2 == 0; });

    std::cout << "Partitioned (evens first): ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;
    std::cout << "Partition point at index: " << (partition_point - v1.begin()) << std::endl;

    // std::stable_partition - preserve relative order
    std::vector<int> v2 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::stable_partition(v2.begin(), v2.end(), [](int x) { return x % 2 == 0; });
    std::cout << "Stable partition (evens first): ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // std::is_partitioned - check if already partitioned
    bool partitioned = std::is_partitioned(v1.begin(), v1.end(),
        [](int x) { return x % 2 == 0; });
    std::cout << "Is partitioned: " << (partitioned ? "yes" : "no") << std::endl;

    // std::partition_point - find partition point in partitioned range
    std::vector<int> v3 = {2, 4, 6, 8, 1, 3, 5, 7};
    auto pp = std::partition_point(v3.begin(), v3.end(),
        [](int x) { return x % 2 == 0; });
    std::cout << "Partition point value: " << *pp << std::endl;

    return 0;
}