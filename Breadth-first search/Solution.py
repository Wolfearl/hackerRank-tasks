from collections import deque, defaultdict

def bfs(n, m, edges, s):
    # Create adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Initialize distances array
    distances = [-1] * n
    distances[s - 1] = 0  # Distance to itself is 0

    # Initialize queue for BFS
    queue = deque([s])

    while queue:
        node = queue.popleft()
        current_distance = distances[node - 1]

        for neighbor in adj[node]:
            if distances[neighbor - 1] == -1:  # If not visited
                distances[neighbor - 1] = current_distance + 6  # Each edge weighs 6
                queue.append(neighbor)

    # Remove the distance for the starting node and return results
    return [dist for i, dist in enumerate(distances) if i != s - 1]

# Example usage:
# q = int(input())
# for _ in range(q):
#     n, m = map(int, input().split())
#     edges = [tuple(map(int, input().split())) for _ in range(m)]
#     s = int(input())
#     result = bfs(n, m, edges, s)
#     print(' '.join(map(str, result)))

print(bfs(4, 2, [[1, 2], [1, 3]], 1))