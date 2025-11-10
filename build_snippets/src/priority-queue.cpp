#include <queue>
#include <vector>
#include <iostream>

int main() {
    // Max heap (default)
    std::priority_queue<int> maxHeap;
    maxHeap.push(10);
    maxHeap.push(5);
    maxHeap.push(20);

    std::cout << "Max: " << maxHeap.top() << std::endl; // 20
    maxHeap.pop();

    // Min heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    minHeap.push(10);
    minHeap.push(5);
    minHeap.push(20);

    std::cout << "Min: " << minHeap.top() << std::endl; // 5
    minHeap.pop();

    return 0;
}