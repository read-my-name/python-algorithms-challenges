from collections import deque

def recursive_bfs(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return
    
    vertex = queue.popleft()
    visited.add(vertex)
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    recursive_bfs(graph, queue, visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Recursive BFS traversal:")
queue = deque(['A'])
recursive_bfs(graph, queue)
print()  # Print new line for formatting
