#include <iostream>
#include <vector>
#include <stack>

// Next greater element to the right
std::vector<int> nextGreaterElement(const std::vector<int>& arr) {
    int n = arr.size();
    std::vector<int> result(n, -1);
    std::stack<int> s; // Stack stores indices

    for (int i = 0; i < n; i++) {
        // Maintain decreasing monotonic stack
        while (!s.empty() && arr[s.top()] < arr[i]) {
            result[s.top()] = arr[i];
            s.pop();
        }
        s.push(i);
    }

    return result;
}

// Next smaller element to the left
std::vector<int> nextSmallerLeft(const std::vector<int>& arr) {
    int n = arr.size();
    std::vector<int> result(n, -1);
    std::stack<int> s;

    for (int i = 0; i < n; i++) {
        // Maintain increasing monotonic stack
        while (!s.empty() && arr[s.top()] >= arr[i]) {
            s.pop();
        }
        if (!s.empty()) {
            result[i] = arr[s.top()];
        }
        s.push(i);
    }

    return result;
}

// Largest rectangle in histogram
int largestRectangleArea(const std::vector<int>& heights) {
    std::stack<int> s;
    int maxArea = 0;
    int n = heights.size();

    for (int i = 0; i < n; i++) {
        while (!s.empty() && heights[s.top()] > heights[i]) {
            int h = heights[s.top()];
            s.pop();
            int width = s.empty() ? i : i - s.top() - 1;
            maxArea = std::max(maxArea, h * width);
        }
        s.push(i);
    }

    while (!s.empty()) {
        int h = heights[s.top()];
        s.pop();
        int width = s.empty() ? n : n - s.top() - 1;
        maxArea = std::max(maxArea, h * width);
    }

    return maxArea;
}

// Daily temperatures - how many days until warmer
std::vector<int> dailyTemperatures(const std::vector<int>& temps) {
    int n = temps.size();
    std::vector<int> result(n, 0);
    std::stack<int> s;

    for (int i = 0; i < n; i++) {
        while (!s.empty() && temps[s.top()] < temps[i]) {
            int idx = s.top();
            s.pop();
            result[idx] = i - idx;
        }
        s.push(i);
    }

    return result;
}

int main() {
    std::vector<int> arr = {4, 5, 2, 10, 8};

    auto nge = nextGreaterElement(arr);
    std::cout << "Next greater elements: ";
    for (int x : nge) std::cout << x << " ";
    std::cout << std::endl;

    std::vector<int> heights = {2, 1, 5, 6, 2, 3};
    std::cout << "Largest rectangle area: " << largestRectangleArea(heights) << std::endl;

    std::vector<int> temps = {73, 74, 75, 71, 69, 72, 76, 73};
    auto days = dailyTemperatures(temps);
    std::cout << "Days until warmer: ";
    for (int d : days) std::cout << d << " ";
    std::cout << std::endl;

    return 0;
}