"""C++ code snippets for common patterns and use cases."""

CPP_SNIPPETS = [
    {
        "name": "basic-main",
        "category": "Basic",
        "description": "Simple main function template",
        "snippet": """#include <iostream>

int main() {
    // Your code here
    return 0;
}"""
    },
    {
        "name": "class",
        "category": "Basic",
        "description": "Basic class structure with constructor, destructor, and common methods",
        "snippet": """class ClassName {
private:
    int data;

public:
    ClassName() : data(0) {}
    ClassName(int val) : data(val) {}
    ~ClassName() {}

    int getData() const {
        return data;
    }

    void setData(int val) {
        data = val;
    }

    void display() const {
        std::cout << "Data: " << data << std::endl;
    }
};"""
    },
    {
        "name": "header-guard",
        "category": "Basic",
        "description": "Include guard pattern for header files",
        "snippet": """#ifndef FILENAME_H
#define FILENAME_H

// Your header content here

#endif // FILENAME_H"""
    },
    {
        "name": "fast-io",
        "category": "I/O",
        "description": "Fast input/output optimization for competitive programming",
        "snippet": """#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // Your code here

    return 0;
}"""
    },
    {
        "name": "file-io",
        "category": "I/O",
        "description": "File reading and writing template",
        "snippet": """#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Reading from file
    std::ifstream inputFile("input.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Error opening input file" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(inputFile, line)) {
        // Process line
        std::cout << line << std::endl;
    }
    inputFile.close();

    // Writing to file
    std::ofstream outputFile("output.txt");
    if (!outputFile.is_open()) {
        std::cerr << "Error opening output file" << std::endl;
        return 1;
    }

    outputFile << "Hello, File!" << std::endl;
    outputFile.close();

    return 0;
}"""
    },
    {
        "name": "string-stream",
        "category": "I/O",
        "description": "String parsing with stringstream",
        "snippet": """#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::string str = "10 20 30 40 50";
    std::stringstream ss(str);

    std::vector<int> numbers;
    int num;
    while (ss >> num) {
        numbers.push_back(num);
    }

    // Process numbers
    for (int n : numbers) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}"""
    },
    {
        "name": "vector-ops",
        "category": "Data Structures",
        "description": "Common vector initialization and operations",
        "snippet": """#include <vector>
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
}"""
    },
    {
        "name": "map-set",
        "category": "Data Structures",
        "description": "STL map and set examples",
        "snippet": """#include <map>
#include <set>
#include <iostream>

int main() {
    // Map operations
    std::map<std::string, int> m;
    m["apple"] = 5;
    m["banana"] = 3;
    m.insert({"orange", 7});

    // Check existence
    if (m.find("apple") != m.end()) {
        std::cout << "Found apple: " << m["apple"] << std::endl;
    }

    // Iterate
    for (const auto& [key, value] : m) {
        std::cout << key << ": " << value << std::endl;
    }

    // Set operations
    std::set<int> s = {1, 2, 3, 4, 5};
    s.insert(6);
    s.erase(3);

    // Check existence
    if (s.count(4) > 0) {
        std::cout << "4 is in the set" << std::endl;
    }

    return 0;
}"""
    },
    {
        "name": "priority-queue",
        "category": "Data Structures",
        "description": "Min/max heap implementations using priority_queue",
        "snippet": """#include <queue>
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
}"""
    },
    {
        "name": "pair-tuple",
        "category": "Data Structures",
        "description": "Using pairs and tuples in C++",
        "snippet": """#include <utility>
#include <tuple>
#include <iostream>

int main() {
    // Pair
    std::pair<int, std::string> p1 = {1, "one"};
    std::pair<int, std::string> p2 = std::make_pair(2, "two");

    std::cout << p1.first << " " << p1.second << std::endl;

    // Structured binding (C++17)
    auto [num, str] = p1;
    std::cout << num << " " << str << std::endl;

    // Tuple
    std::tuple<int, double, std::string> t = {1, 3.14, "pi"};

    std::cout << std::get<0>(t) << " ";
    std::cout << std::get<1>(t) << " ";
    std::cout << std::get<2>(t) << std::endl;

    // Structured binding with tuple
    auto [i, d, s] = t;
    std::cout << i << " " << d << " " << s << std::endl;

    return 0;
}"""
    },
    {
        "name": "binary-search",
        "category": "Algorithms",
        "description": "Binary search implementation",
        "snippet": """#include <vector>
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
}"""
    },
    {
        "name": "dfs",
        "category": "Algorithms",
        "description": "Depth-first search for graphs and grids",
        "snippet": """#include <vector>
#include <iostream>

// Graph DFS (Adjacency List)
std::vector<std::vector<int>> adj;
std::vector<bool> visited;

void dfs_graph(int node) {
    visited[node] = true;
    std::cout << node << " ";

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs_graph(neighbor);
        }
    }
}

// Grid/Matrix DFS
int dx[] = {-1, 1, 0, 0}; // Up, Down, Left, Right
int dy[] = {0, 0, -1, 1};

void dfs_grid(std::vector<std::vector<int>>& grid, int x, int y) {
    int rows = grid.size();
    int cols = grid[0].size();

    if (x < 0 || x >= rows || y < 0 || y >= cols || grid[x][y] == 0) {
        return;
    }

    grid[x][y] = 0; // Mark as visited

    for (int i = 0; i < 4; i++) {
        dfs_grid(grid, x + dx[i], y + dy[i]);
    }
}

int main() {
    // Example 1: Graph DFS
    int n = 6;
    adj.resize(n);
    visited.resize(n, false);

    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0, 5};

    std::cout << "Graph DFS: ";
    dfs_graph(0);
    std::cout << std::endl;

    // Example 2: Grid DFS (find connected components)
    std::vector<std::vector<int>> grid = {
        {1, 1, 0, 0, 0},
        {1, 1, 0, 0, 1},
        {0, 0, 1, 0, 0},
        {0, 0, 0, 1, 1}
    };

    dfs_grid(grid, 0, 0); // Visit island starting at (0,0)

    return 0;
}"""
    },
    {
        "name": "bfs",
        "category": "Algorithms",
        "description": "Breadth-first search for graphs and grids",
        "snippet": """#include <vector>
#include <queue>
#include <iostream>

// Graph BFS (Adjacency List)
std::vector<std::vector<int>> adj;
std::vector<bool> visited;

void bfs_graph(int start) {
    std::queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        std::cout << node << " ";

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

// Grid/Matrix BFS
int dx[] = {-1, 1, 0, 0}; // Up, Down, Left, Right
int dy[] = {0, 0, -1, 1};

int bfs_grid(std::vector<std::vector<int>>& grid, int startX, int startY) {
    int rows = grid.size();
    int cols = grid[0].size();

    if (grid[startX][startY] == 0) return 0;

    std::queue<std::pair<int, int>> q;
    q.push({startX, startY});
    grid[startX][startY] = 0; // Mark as visited

    int count = 0;
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        count++;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 1) {
                grid[nx][ny] = 0; // Mark as visited
                q.push({nx, ny});
            }
        }
    }
    return count;
}

int main() {
    // Example 1: Graph BFS
    int n = 6;
    adj.resize(n);
    visited.resize(n, false);

    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0, 5};

    std::cout << "Graph BFS: ";
    bfs_graph(0);
    std::cout << std::endl;

    // Example 2: Grid BFS (count island size)
    std::vector<std::vector<int>> grid = {
        {1, 1, 0, 0, 0},
        {1, 1, 0, 0, 1},
        {0, 0, 1, 0, 0},
        {0, 0, 0, 1, 1}
    };

    int island_size = bfs_grid(grid, 0, 0);
    std::cout << "Island size: " << island_size << std::endl;

    return 0;
}"""
    },
    {
        "name": "sorting-custom",
        "category": "Algorithms",
        "description": "Custom comparator for sorting",
        "snippet": """#include <vector>
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
}"""
    },
    {
        "name": "lambda-functions",
        "category": "Modern C++",
        "description": "Lambda syntax and usage examples",
        "snippet": """#include <vector>
#include <algorithm>
#include <iostream>
#include <functional>

int main() {
    // Basic lambda
    auto add = [](int a, int b) { return a + b; };
    std::cout << add(3, 4) << std::endl;

    // Lambda with capture
    int multiplier = 3;
    auto multiply = [multiplier](int x) { return x * multiplier; };
    std::cout << multiply(5) << std::endl;

    // Capture by reference
    int counter = 0;
    auto increment = [&counter]() { counter++; };
    increment();
    increment();
    std::cout << "Counter: " << counter << std::endl;

    // Generic lambda (C++14)
    auto print = [](const auto& val) { std::cout << val << std::endl; };
    print(42);
    print("Hello");

    // Lambda with algorithms
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::for_each(v.begin(), v.end(), [](int x) {
        std::cout << x * 2 << " ";
    });
    std::cout << std::endl;

    // Lambda as return type
    auto makeAdder = [](int n) {
        return [n](int x) { return x + n; };
    };
    auto add10 = makeAdder(10);
    std::cout << add10(5) << std::endl;

    return 0;
}"""
    },
    {
        "name": "range-for",
        "category": "Modern C++",
        "description": "Modern C++ range-based iteration patterns",
        "snippet": """#include <vector>
#include <map>
#include <iostream>

int main() {
    // Vector iteration
    std::vector<int> v = {1, 2, 3, 4, 5};

    // Read-only
    for (const auto& elem : v) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // Modify elements
    for (auto& elem : v) {
        elem *= 2;
    }

    // Copy (less efficient)
    for (auto elem : v) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // Map iteration with structured binding
    std::map<std::string, int> m = {
        {"apple", 5},
        {"banana", 3},
        {"orange", 7}
    };

    for (const auto& [key, value] : m) {
        std::cout << key << ": " << value << std::endl;
    }

    // Traditional iterator when index is needed
    for (size_t i = 0; i < v.size(); ++i) {
        std::cout << "v[" << i << "] = " << v[i] << std::endl;
    }

    return 0;
}"""
    },
    {
        "name": "smart-pointers",
        "category": "Modern C++",
        "description": "Modern C++ smart pointer usage (unique_ptr, shared_ptr)",
        "snippet": """#include <memory>
#include <iostream>
#include <vector>

class MyClass {
public:
    MyClass(int val) : value(val) {
        std::cout << "Constructor: " << value << std::endl;
    }
    ~MyClass() {
        std::cout << "Destructor: " << value << std::endl;
    }
    void display() {
        std::cout << "Value: " << value << std::endl;
    }
private:
    int value;
};

int main() {
    // unique_ptr - exclusive ownership
    std::unique_ptr<MyClass> ptr1 = std::make_unique<MyClass>(10);
    ptr1->display();

    // Transfer ownership
    std::unique_ptr<MyClass> ptr2 = std::move(ptr1);
    // ptr1 is now nullptr

    // shared_ptr - shared ownership
    std::shared_ptr<MyClass> sptr1 = std::make_shared<MyClass>(20);
    {
        std::shared_ptr<MyClass> sptr2 = sptr1; // Reference count = 2
        sptr2->display();
        std::cout << "Use count: " << sptr1.use_count() << std::endl;
    } // sptr2 destroyed, reference count = 1

    std::cout << "Use count: " << sptr1.use_count() << std::endl;

    // weak_ptr - non-owning reference
    std::weak_ptr<MyClass> wptr = sptr1;
    if (auto locked = wptr.lock()) {
        locked->display();
    }

    // Vector of unique_ptrs
    std::vector<std::unique_ptr<MyClass>> vec;
    vec.push_back(std::make_unique<MyClass>(30));
    vec.push_back(std::make_unique<MyClass>(40));

    return 0;
}"""
    },
    {
        "name": "template-function",
        "category": "Modern C++",
        "description": "Generic function template examples",
        "snippet": """#include <iostream>
#include <vector>
#include <string>

// Basic template function
template<typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Template with multiple type parameters
template<typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}

// Template function with container
template<typename T>
void printVector(const std::vector<T>& vec) {
    for (const auto& elem : vec) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

// Template with constraints (concept-like, C++20 style)
template<typename T>
T sumVector(const std::vector<T>& vec) {
    T sum = T();
    for (const auto& elem : vec) {
        sum += elem;
    }
    return sum;
}

// Template class
template<typename T>
class Container {
private:
    T value;
public:
    Container(T val) : value(val) {}
    T getValue() const { return value; }
    void setValue(T val) { value = val; }
};

int main() {
    std::cout << maximum(10, 20) << std::endl;
    std::cout << maximum(3.14, 2.71) << std::endl;
    std::cout << maximum<std::string>("apple", "banana") << std::endl;

    std::cout << add(5, 3.14) << std::endl;

    std::vector<int> v1 = {1, 2, 3, 4, 5};
    printVector(v1);

    std::vector<std::string> v2 = {"hello", "world"};
    printVector(v2);

    Container<int> c1(42);
    std::cout << c1.getValue() << std::endl;

    return 0;
}"""
    },
    {
        "name": "mod-arithmetic",
        "category": "Competitive Programming",
        "description": "Modular arithmetic helpers for competitive programming",
        "snippet": """#include <iostream>

const long long MOD = 1e9 + 7;

// Modular addition
long long addMod(long long a, long long b, long long mod = MOD) {
    return ((a % mod) + (b % mod)) % mod;
}

// Modular subtraction
long long subMod(long long a, long long b, long long mod = MOD) {
    return ((a % mod) - (b % mod) + mod) % mod;
}

// Modular multiplication
long long mulMod(long long a, long long b, long long mod = MOD) {
    return ((a % mod) * (b % mod)) % mod;
}

// Modular exponentiation (fast power)
long long powerMod(long long base, long long exp, long long mod = MOD) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// Modular inverse using Fermat's little theorem (when mod is prime)
long long modInverse(long long a, long long mod = MOD) {
    return powerMod(a, mod - 2, mod);
}

// Modular division
long long divMod(long long a, long long b, long long mod = MOD) {
    return mulMod(a, modInverse(b, mod), mod);
}

int main() {
    long long a = 1000000000;
    long long b = 999999999;

    std::cout << "Add: " << addMod(a, b) << std::endl;
    std::cout << "Mul: " << mulMod(a, b) << std::endl;
    std::cout << "Power: " << powerMod(2, 10) << std::endl;
    std::cout << "Inverse: " << modInverse(3) << std::endl;

    return 0;
}"""
    },
    {
        "name": "gcd-lcm",
        "category": "Competitive Programming",
        "description": "Greatest common divisor and least common multiple",
        "snippet": """#include <iostream>
#include <numeric> // For std::gcd and std::lcm (C++17)
#include <algorithm>

// Manual GCD implementation (Euclidean algorithm)
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Manual LCM implementation
long long lcm(long long a, long long b) {
    return (a / gcd(a, b)) * b;
}

// Extended Euclidean Algorithm
// Finds gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b)
long long extendedGCD(long long a, long long b, long long& x, long long& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long gcd = extendedGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return gcd;
}

int main() {
    long long a = 48, b = 18;

    // Using manual implementation
    std::cout << "GCD(" << a << ", " << b << ") = " << gcd(a, b) << std::endl;
    std::cout << "LCM(" << a << ", " << b << ") = " << lcm(a, b) << std::endl;

    // Using C++17 STL
    std::cout << "STL GCD: " << std::gcd(a, b) << std::endl;
    std::cout << "STL LCM: " << std::lcm(a, b) << std::endl;

    // Extended GCD
    long long x, y;
    long long g = extendedGCD(a, b, x, y);
    std::cout << "Extended GCD: " << g << std::endl;
    std::cout << a << "*" << x << " + " << b << "*" << y << " = " << g << std::endl;

    return 0;
}"""
    },
    {
        "name": "sliding-window",
        "category": "Common Patterns",
        "description": "Sliding window technique template for subarray problems",
        "snippet": """#include <iostream>
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
}"""
    },
    {
        "name": "two-pointers",
        "category": "Common Patterns",
        "description": "Two pointers pattern for array problems",
        "snippet": """#include <iostream>
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
}"""
    },
    {
        "name": "backtracking",
        "category": "Common Patterns",
        "description": "Backtracking template with pruning for combinatorial problems",
        "snippet": """#include <iostream>
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
}"""
    },
    {
        "name": "monotonic-stack",
        "category": "Common Patterns",
        "description": "Monotonic stack for next greater/smaller element problems",
        "snippet": """#include <iostream>
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
}"""
    },
    {
        "name": "prefix-sum",
        "category": "Common Patterns",
        "description": "Prefix sum and difference array techniques",
        "snippet": """#include <iostream>
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
}"""
    },
    {
        "name": "stl-find",
        "category": "STL",
        "description": "std::find and std::find_if for searching in containers",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    // std::find - search for value
    auto it = std::find(v.begin(), v.end(), 5);
    if (it != v.end()) {
        std::cout << "Found: " << *it << " at position " << (it - v.begin()) << std::endl;
    }

    // std::find_if - search with predicate
    auto even = std::find_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; });
    if (even != v.end()) {
        std::cout << "First even: " << *even << std::endl;
    }

    // std::find_if_not - search for element not matching predicate
    auto not_small = std::find_if_not(v.begin(), v.end(), [](int x) { return x < 5; });
    if (not_small != v.end()) {
        std::cout << "First not small: " << *not_small << std::endl;
    }

    // Check if element exists
    bool has_seven = std::find(v.begin(), v.end(), 7) != v.end();
    std::cout << "Has 7: " << (has_seven ? "yes" : "no") << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-count",
        "category": "STL",
        "description": "std::count and std::count_if for counting elements",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    std::vector<int> v = {1, 2, 3, 2, 4, 2, 5, 2};

    // std::count - count occurrences of value
    int count_twos = std::count(v.begin(), v.end(), 2);
    std::cout << "Number of 2s: " << count_twos << std::endl;

    // std::count_if - count with predicate
    int count_even = std::count_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; });
    std::cout << "Even numbers: " << count_even << std::endl;

    // Count in strings
    std::string str = "hello world";
    int count_l = std::count(str.begin(), str.end(), 'l');
    std::cout << "Letter 'l' count: " << count_l << std::endl;

    // Count with complex predicate
    int count_large = std::count_if(v.begin(), v.end(), [](int x) { return x > 3; });
    std::cout << "Numbers > 3: " << count_large << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-accumulate",
        "category": "STL",
        "description": "std::accumulate for sum, product, and custom operations",
        "snippet": """#include <iostream>
#include <vector>
#include <numeric>
#include <string>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // Sum of elements
    int sum = std::accumulate(v.begin(), v.end(), 0);
    std::cout << "Sum: " << sum << std::endl;

    // Product of elements
    int product = std::accumulate(v.begin(), v.end(), 1, std::multiplies<int>());
    std::cout << "Product: " << product << std::endl;

    // Custom operation with lambda
    int sum_of_squares = std::accumulate(v.begin(), v.end(), 0,
        [](int acc, int x) { return acc + x * x; });
    std::cout << "Sum of squares: " << sum_of_squares << std::endl;

    // Concatenate strings
    std::vector<std::string> words = {"Hello", " ", "World", "!"};
    std::string sentence = std::accumulate(words.begin(), words.end(), std::string(""));
    std::cout << "Sentence: " << sentence << std::endl;

    // Count elements matching condition
    int count_even = std::accumulate(v.begin(), v.end(), 0,
        [](int acc, int x) { return acc + (x % 2 == 0 ? 1 : 0); });
    std::cout << "Even count: " << count_even << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-transform",
        "category": "STL",
        "description": "std::transform to apply function to range",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <string>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::vector<int> result(v.size());

    // Square each element
    std::transform(v.begin(), v.end(), result.begin(),
        [](int x) { return x * x; });
    std::cout << "Squares: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;

    // Transform in-place
    std::transform(v.begin(), v.end(), v.begin(),
        [](int x) { return x * 2; });
    std::cout << "Doubled: ";
    for (int x : v) std::cout << x << " ";
    std::cout << std::endl;

    // Binary transform - add two vectors
    std::vector<int> v1 = {1, 2, 3};
    std::vector<int> v2 = {4, 5, 6};
    std::vector<int> sum(v1.size());
    std::transform(v1.begin(), v1.end(), v2.begin(), sum.begin(),
        [](int a, int b) { return a + b; });
    std::cout << "Sum of vectors: ";
    for (int x : sum) std::cout << x << " ";
    std::cout << std::endl;

    // Convert string to uppercase
    std::string str = "hello world";
    std::transform(str.begin(), str.end(), str.begin(), ::toupper);
    std::cout << "Uppercase: " << str << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-remove",
        "category": "STL",
        "description": "std::remove and std::remove_if with erase idiom",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // Remove specific value (erase-remove idiom)
    std::vector<int> v1 = {1, 2, 3, 2, 4, 2, 5};
    std::cout << "Original: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // std::remove doesn't actually remove, it moves elements
    auto new_end = std::remove(v1.begin(), v1.end(), 2);
    v1.erase(new_end, v1.end());
    std::cout << "After remove 2: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // Remove with predicate (remove even numbers)
    std::vector<int> v2 = {1, 2, 3, 4, 5, 6, 7, 8};
    v2.erase(
        std::remove_if(v2.begin(), v2.end(), [](int x) { return x % 2 == 0; }),
        v2.end()
    );
    std::cout << "After remove evens: ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // Remove elements greater than 5
    std::vector<int> v3 = {1, 8, 3, 9, 2, 7, 4};
    v3.erase(
        std::remove_if(v3.begin(), v3.end(), [](int x) { return x > 5; }),
        v3.end()
    );
    std::cout << "After remove > 5: ";
    for (int x : v3) std::cout << x << " ";
    std::cout << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-sort-variations",
        "category": "STL",
        "description": "std::sort, stable_sort, partial_sort, and nth_element",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // std::sort - regular sort (not stable)
    std::vector<int> v1 = {5, 2, 8, 1, 9, 3};
    std::sort(v1.begin(), v1.end());
    std::cout << "Sorted: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // Sort in descending order
    std::vector<int> v2 = {5, 2, 8, 1, 9, 3};
    std::sort(v2.begin(), v2.end(), std::greater<int>());
    std::cout << "Descending: ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // std::stable_sort - preserves relative order of equal elements
    std::vector<int> v3 = {5, 2, 8, 1, 9, 3};
    std::stable_sort(v3.begin(), v3.end());

    // std::partial_sort - sort first N elements
    std::vector<int> v4 = {5, 2, 8, 1, 9, 3, 7, 4};
    std::partial_sort(v4.begin(), v4.begin() + 3, v4.end());
    std::cout << "Partial sort (first 3): ";
    for (int x : v4) std::cout << x << " ";
    std::cout << std::endl;

    // std::nth_element - find nth smallest element
    std::vector<int> v5 = {5, 2, 8, 1, 9, 3, 7, 4};
    std::nth_element(v5.begin(), v5.begin() + 3, v5.end());
    std::cout << "4th smallest element: " << v5[3] << std::endl;

    // is_sorted - check if sorted
    bool sorted = std::is_sorted(v1.begin(), v1.end());
    std::cout << "Is v1 sorted: " << (sorted ? "yes" : "no") << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-minmax",
        "category": "STL",
        "description": "std::min, max, min_element, max_element, and minmax",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {5, 2, 8, 1, 9, 3};

    // std::min and std::max for two values
    int a = 10, b = 20;
    std::cout << "Min: " << std::min(a, b) << std::endl;
    std::cout << "Max: " << std::max(a, b) << std::endl;

    // std::min_element and std::max_element
    auto min_it = std::min_element(v.begin(), v.end());
    auto max_it = std::max_element(v.begin(), v.end());
    std::cout << "Min element: " << *min_it << " at index " << (min_it - v.begin()) << std::endl;
    std::cout << "Max element: " << *max_it << " at index " << (max_it - v.begin()) << std::endl;

    // std::minmax - get both min and max
    auto [min_val, max_val] = std::minmax({5, 2, 8, 1, 9});
    std::cout << "Minmax: " << min_val << ", " << max_val << std::endl;

    // std::minmax_element - get both iterators
    auto [min_iter, max_iter] = std::minmax_element(v.begin(), v.end());
    std::cout << "Min: " << *min_iter << ", Max: " << *max_iter << std::endl;

    // With custom comparator
    auto abs_max = std::max_element(v.begin(), v.end(),
        [](int a, int b) { return std::abs(a) < std::abs(b); });
    std::cout << "Max by absolute value: " << *abs_max << std::endl;

    // Clamp value to range
    int value = 15;
    int clamped = std::clamp(value, 5, 10);
    std::cout << "Clamped " << value << " to [5,10]: " << clamped << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-predicates",
        "category": "STL",
        "description": "std::all_of, any_of, none_of for testing predicates",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v1 = {2, 4, 6, 8, 10};
    std::vector<int> v2 = {1, 3, 5, 7, 9};
    std::vector<int> v3 = {1, 2, 3, 4, 5};

    // std::all_of - check if all elements satisfy condition
    bool all_even = std::all_of(v1.begin(), v1.end(), [](int x) { return x % 2 == 0; });
    std::cout << "All even in v1: " << (all_even ? "yes" : "no") << std::endl;

    // std::any_of - check if any element satisfies condition
    bool any_even = std::any_of(v2.begin(), v2.end(), [](int x) { return x % 2 == 0; });
    std::cout << "Any even in v2: " << (any_even ? "yes" : "no") << std::endl;

    // std::none_of - check if no elements satisfy condition
    bool none_negative = std::none_of(v3.begin(), v3.end(), [](int x) { return x < 0; });
    std::cout << "None negative in v3: " << (none_negative ? "yes" : "no") << std::endl;

    // Practical examples
    std::vector<int> ages = {25, 30, 35, 28, 32};

    bool all_adults = std::all_of(ages.begin(), ages.end(), [](int age) { return age >= 18; });
    std::cout << "All adults: " << (all_adults ? "yes" : "no") << std::endl;

    bool any_senior = std::any_of(ages.begin(), ages.end(), [](int age) { return age >= 65; });
    std::cout << "Any senior: " << (any_senior ? "yes" : "no") << std::endl;

    bool none_minor = std::none_of(ages.begin(), ages.end(), [](int age) { return age < 18; });
    std::cout << "None minor: " << (none_minor ? "yes" : "no") << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-unique",
        "category": "STL",
        "description": "std::unique to remove consecutive duplicates",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // Remove consecutive duplicates
    std::vector<int> v1 = {1, 1, 2, 2, 2, 3, 3, 4, 5, 5};
    std::cout << "Original: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    auto new_end = std::unique(v1.begin(), v1.end());
    v1.erase(new_end, v1.end());
    std::cout << "After unique: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // Remove all duplicates (sort first, then unique)
    std::vector<int> v2 = {3, 1, 2, 1, 3, 2, 4, 3, 2};
    std::sort(v2.begin(), v2.end());
    v2.erase(std::unique(v2.begin(), v2.end()), v2.end());
    std::cout << "All duplicates removed: ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // Unique with custom comparator
    std::vector<int> v3 = {1, -1, 2, -2, 3, 3, 4};
    auto abs_end = std::unique(v3.begin(), v3.end(),
        [](int a, int b) { return std::abs(a) == std::abs(b); });
    v3.erase(abs_end, v3.end());
    std::cout << "Unique by absolute value: ";
    for (int x : v3) std::cout << x << " ";
    std::cout << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-partition",
        "category": "STL",
        "description": "std::partition and related partitioning algorithms",
        "snippet": """#include <iostream>
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
}"""
    },
    {
        "name": "stl-copy-replace",
        "category": "STL",
        "description": "std::copy_if, replace_if, and fill operations",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> src = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    // std::copy - copy all elements
    std::vector<int> dest1(src.size());
    std::copy(src.begin(), src.end(), dest1.begin());
    std::cout << "Copied: ";
    for (int x : dest1) std::cout << x << " ";
    std::cout << std::endl;

    // std::copy_if - copy only elements matching predicate
    std::vector<int> evens;
    std::copy_if(src.begin(), src.end(), std::back_inserter(evens),
        [](int x) { return x % 2 == 0; });
    std::cout << "Evens: ";
    for (int x : evens) std::cout << x << " ";
    std::cout << std::endl;

    // std::replace - replace value
    std::vector<int> v1 = {1, 2, 3, 2, 4, 2, 5};
    std::replace(v1.begin(), v1.end(), 2, 99);
    std::cout << "Replace 2 with 99: ";
    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    // std::replace_if - replace with predicate
    std::vector<int> v2 = {1, 2, 3, 4, 5, 6, 7, 8};
    std::replace_if(v2.begin(), v2.end(),
        [](int x) { return x % 2 == 0; }, 0);
    std::cout << "Replace evens with 0: ";
    for (int x : v2) std::cout << x << " ";
    std::cout << std::endl;

    // std::fill - fill with value
    std::vector<int> v3(10);
    std::fill(v3.begin(), v3.end(), 42);
    std::cout << "Filled with 42: ";
    for (int x : v3) std::cout << x << " ";
    std::cout << std::endl;

    // std::fill_n - fill first n elements
    std::vector<int> v4(10, 0);
    std::fill_n(v4.begin(), 5, 99);
    std::cout << "First 5 filled with 99: ";
    for (int x : v4) std::cout << x << " ";
    std::cout << std::endl;

    return 0;
}"""
    },
    {
        "name": "stl-for-each",
        "category": "STL",
        "description": "std::for_each to apply function to each element",
        "snippet": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // std::for_each - apply function to each element
    std::cout << "Print each: ";
    std::for_each(v.begin(), v.end(), [](int x) {
        std::cout << x << " ";
    });
    std::cout << std::endl;

    // Modify elements with for_each
    std::for_each(v.begin(), v.end(), [](int& x) {
        x *= 2;
    });
    std::cout << "After doubling: ";
    for (int x : v) std::cout << x << " ";
    std::cout << std::endl;

    // for_each with stateful lambda
    int sum = 0;
    std::for_each(v.begin(), v.end(), [&sum](int x) {
        sum += x;
    });
    std::cout << "Sum: " << sum << std::endl;

    // for_each with custom function object
    struct Counter {
        int count = 0;
        void operator()(int x) {
            if (x % 2 == 0) count++;
        }
    };
    Counter c = std::for_each(v.begin(), v.end(), Counter());
    std::cout << "Even count: " << c.count << std::endl;

    // Print with index
    int index = 0;
    std::for_each(v.begin(), v.end(), [&index](int x) {
        std::cout << "v[" << index++ << "] = " << x << std::endl;
    });

    return 0;
}"""
    }
]
