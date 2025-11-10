#include <iostream>
#include <vector>
#include <algorithm>

// Two sum in sorted array
std::pair<int, int> twoSumSorted(const std::vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;

    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            return {left, right};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return {-1, -1};
}

// Remove duplicates from sorted array (in-place)
int removeDuplicates(std::vector<int>& arr) {
    if (arr.empty()) return 0;

    int writePos = 1;
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] != arr[i - 1]) {
            arr[writePos++] = arr[i];
        }
    }

    return writePos;
}

// Container with most water
int maxArea(const std::vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int maxWater = 0;

    while (left < right) {
        int width = right - left;
        int h = std::min(height[left], height[right]);
        maxWater = std::max(maxWater, width * h);

        // Move pointer with smaller height
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxWater;
}

int main() {
    std::vector<int> sorted = {1, 2, 3, 4, 6};
    auto [i, j] = twoSumSorted(sorted, 6);
    std::cout << "Two sum indices: " << i << ", " << j << std::endl;

    std::vector<int> dups = {1, 1, 2, 2, 3, 3, 4};
    int newLen = removeDuplicates(dups);
    std::cout << "New length after removing duplicates: " << newLen << std::endl;

    std::vector<int> heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    std::cout << "Max water: " << maxArea(heights) << std::endl;

    return 0;
}