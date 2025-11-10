#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    // Initialization
    std::vector<int> v1;                    // Empty vector
    std::vector<int> v2(10);                // 10 elements, default value 0
    std::vector<int> v3(10, 5);             // 10 elements, all 5
    std::vector<int> v4 = {1, 2, 3, 4, 5};  // Initializer list

    // Operations
    v1.push_back(10);
    v1.pop_back();
    v1.insert(v1.begin(), 5);
    v1.erase(v1.begin());

    // Access
    int front = v4.front();
    int back = v4.back();
    int at_index = v4[2];

    // Size operations
    size_t size = v4.size();
    bool empty = v4.empty();
    v4.clear();

    // Sorting
    std::sort(v4.begin(), v4.end());
    std::reverse(v4.begin(), v4.end());

    return 0;
}