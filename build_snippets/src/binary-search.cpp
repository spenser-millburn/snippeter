#include <vector>
#include <algorithm>
#include <iostream>

// Manual binary search
int binarySearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1; // Not found
}

int main() {
    std::vector<int> arr = {1, 3, 5, 7, 9, 11, 13};

    // Manual implementation
    int index = binarySearch(arr, 7);
    std::cout << "Index: " << index << std::endl;

    // STL binary_search (returns bool)
    bool found = std::binary_search(arr.begin(), arr.end(), 7);
    std::cout << "Found: " << found << std::endl;

    // STL lower_bound (returns iterator)
    auto it = std::lower_bound(arr.begin(), arr.end(), 7);
    if (it != arr.end()) {
        std::cout << "Lower bound index: " << (it - arr.begin()) << std::endl;
    }

    return 0;
}