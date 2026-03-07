"""
Course Schedule (Topological Sort)
Can you finish numCourses? Prerequisites: [a, b] means b -> a (take b before a).
"""

from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj: list[list[int]] = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    count = 0
    while q:
        u = q.popleft()
        count += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return count == num_courses


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """Return a valid order to finish all courses (or [] if impossible)."""
    adj: list[list[int]] = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == num_courses else []


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))           # True
    print(can_finish(2, [[1, 0], [0, 1]]))   # False
    print(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # e.g. [0, 1, 2, 3]
