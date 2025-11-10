#include <vector>
#include <queue>
#include <iostream>

std::vector<std::vector<int>> adj; // Adjacency list
std::vector<bool> visited;

void bfs(int start) {
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

    std::cout << "BFS traversal: ";
    bfs(0);
    std::cout << std::endl;

    return 0;
}