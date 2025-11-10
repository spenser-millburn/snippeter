#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

// Fixed size sliding window
int maxSumFixedWindow(const std::vector<int>& arr, int k) {
    int n = arr.size();
    if (n < k) return -1;

    int windowSum = 0;
    for (int i = 0; i < k; i++) {
        windowSum += arr[i];
    }

    int maxSum = windowSum;
    for (int i = k; i < n; i++) {
        windowSum += arr[i] - arr[i - k];
        maxSum = std::max(maxSum, windowSum);
    }

    return maxSum;
}

// Variable size sliding window - longest substring with at most k distinct chars
int longestSubstringKDistinct(const std::string& s, int k) {
    std::unordered_map<char, int> freq;
    int left = 0, maxLen = 0;

    for (int right = 0; right < s.length(); right++) {
        freq[s[right]]++;

        // Shrink window if constraint violated
        while (freq.size() > k) {
            freq[s[left]]--;
            if (freq[s[left]] == 0) {
                freq.erase(s[left]);
            }
            left++;
        }

        maxLen = std::max(maxLen, right - left + 1);
    }

    return maxLen;
}

int main() {
    std::vector<int> arr = {1, 4, 2, 10, 23, 3, 1, 0, 20};
    std::cout << "Max sum of window size 4: " << maxSumFixedWindow(arr, 4) << std::endl;

    std::string s = "aabbcc";
    std::cout << "Longest substring with 2 distinct: " << longestSubstringKDistinct(s, 2) << std::endl;

    return 0;
}