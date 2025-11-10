#include <vector>
#include <iostream>

std::vector<std::vector<int>> adj; // Adjacency list
std::vector<bool> visited;

void dfs(int node) {
    visited[node] = true;
    std::cout << node << " ";

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor);
        }
    }
}

int main() {
    int n = 6; // Number of nodes
    adj.resize(n);
    visited.resize(n, false);

    // Example graph edges
    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0, 5};
    adj[3] = {1};
    adj[4] = {1};
    adj[5] = {2};

    std::cout << "DFS traversal: ";
    dfs(0);
    std::cout << std::endl;

    return 0;
}