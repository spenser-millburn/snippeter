#include <iostream>
#include <vector>

std::vector<std::vector<int>> result;

// Generate all permutations
void permuteBacktrack(std::vector<int>& nums, int start) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }

    for (int i = start; i < nums.size(); i++) {
        std::swap(nums[start], nums[i]);
        permuteBacktrack(nums, start + 1);
        std::swap(nums[start], nums[i]); // Backtrack
    }
}

// Generate all subsets
void subsetsBacktrack(const std::vector<int>& nums, int index,
                      std::vector<int>& current, std::vector<std::vector<int>>& result) {
    result.push_back(current);

    for (int i = index; i < nums.size(); i++) {
        current.push_back(nums[i]);
        subsetsBacktrack(nums, i + 1, current, result);
        current.pop_back(); // Backtrack
    }
}

// N-Queens with pruning
bool isSafe(const std::vector<std::string>& board, int row, int col, int n) {
    // Check column
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 'Q') return false;
    }

    // Check diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q') return false;
    }

    // Check anti-diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 'Q') return false;
    }

    return true;
}

void solveNQueens(int n, int row, std::vector<std::string>& board,
                  std::vector<std::vector<std::string>>& solutions) {
    if (row == n) {
        solutions.push_back(board);
        return;
    }

    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 'Q';
            solveNQueens(n, row + 1, board, solutions);
            board[row][col] = '.'; // Backtrack
        }
    }
}

int main() {
    // Permutations
    std::vector<int> nums = {1, 2, 3};
    permuteBacktrack(nums, 0);
    std::cout << "Permutations: " << result.size() << std::endl;

    // Subsets
    result.clear();
    std::vector<int> current;
    subsetsBacktrack(nums, 0, current, result);
    std::cout << "Subsets: " << result.size() << std::endl;

    // N-Queens
    int n = 4;
    std::vector<std::vector<std::string>> solutions;
    std::vector<std::string> board(n, std::string(n, '.'));
    solveNQueens(n, 0, board, solutions);
    std::cout << n << "-Queens solutions: " << solutions.size() << std::endl;

    return 0;
}