"""
Detect Cycle in a Directed Graph
Using DFS with recursion stack (gray/black coloring) or Kahn's (indegree).
"""

from collections import deque


def has_cycle_dfs(n: int, edges: list[list[int]]) -> bool:
    """DFS: 0=unvisited, 1=in stack, 2=done."""
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    color = [0] * n

    def dfs(u: int) -> bool:
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and dfs(v):
                return True
        color[u] = 2
        return False

    for i in range(n):
        if color[i] == 0 and dfs(i):
            return True
    return False


def has_cycle_kahn(n: int, edges: list[list[int]]) -> bool:
    """Kahn's (BFS): if topo order has < n nodes, there's a cycle."""
    adj: list[list[int]] = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    count = 0
    while q:
        u = q.popleft()
        count += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return count != n


if __name__ == "__main__":
    n = 4
    edges = [[0, 1], [1, 2], [2, 3], [3, 1]]  # cycle 1->2->3->1
    print(has_cycle_dfs(n, edges))   # True
    print(has_cycle_kahn(n, edges))  # True
    edges2 = [[0, 1], [1, 2], [2, 3]]
    print(has_cycle_dfs(n, edges2))   # False
    print(has_cycle_kahn(n, edges2))  # False
