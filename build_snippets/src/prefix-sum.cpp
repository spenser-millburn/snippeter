#include <iostream>
#include <vector>

// Basic prefix sum
class PrefixSum {
private:
    std::vector<long long> prefix;

public:
    PrefixSum(const std::vector<int>& arr) {
        int n = arr.size();
        prefix.resize(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + arr[i];
        }
    }

    // Sum of range [left, right] (0-indexed)
    long long rangeSum(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
};

// 2D prefix sum
class PrefixSum2D {
private:
    std::vector<std::vector<long long>> prefix;

public:
    PrefixSum2D(const std::vector<std::vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        prefix.resize(m + 1, std::vector<long long>(n + 1, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefix[i][j] = matrix[i-1][j-1]
                             + prefix[i-1][j]
                             + prefix[i][j-1]
                             - prefix[i-1][j-1];
            }
        }
    }

    // Sum of submatrix from (r1,c1) to (r2,c2) (0-indexed)
    long long rangeSum(int r1, int c1, int r2, int c2) {
        r1++; c1++; r2++; c2++;
        return prefix[r2][c2]
             - prefix[r1-1][c2]
             - prefix[r2][c1-1]
             + prefix[r1-1][c1-1];
    }
};

// Difference array for range updates
class DifferenceArray {
private:
    std::vector<long long> diff;

public:
    DifferenceArray(int n) : diff(n + 1, 0) {}

    // Add val to range [left, right]
    void rangeAdd(int left, int right, int val) {
        diff[left] += val;
        diff[right + 1] -= val;
    }

    // Get final array after all updates
    std::vector<long long> getFinalArray() {
        std::vector<long long> result;
        long long sum = 0;
        for (int i = 0; i < diff.size() - 1; i++) {
            sum += diff[i];
            result.push_back(sum);
        }
        return result;
    }
};

int main() {
    // 1D prefix sum
    std::vector<int> arr = {1, 2, 3, 4, 5};
    PrefixSum ps(arr);
    std::cout << "Sum [1, 3]: " << ps.rangeSum(1, 3) << std::endl;

    // 2D prefix sum
    std::vector<std::vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    PrefixSum2D ps2d(matrix);
    std::cout << "2D sum [(0,0) to (1,1)]: " << ps2d.rangeSum(0, 0, 1, 1) << std::endl;

    // Difference array
    DifferenceArray diff(5);
    diff.rangeAdd(0, 2, 10);
    diff.rangeAdd(1, 4, 5);
    auto result = diff.getFinalArray();
    std::cout << "After range updates: ";
    for (long long x : result) std::cout << x << " ";
    std::cout << std::endl;

    return 0;
}