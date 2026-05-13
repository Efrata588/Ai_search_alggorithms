from common.graph import graph
from BFS import bfs
from DFS import dfs

bfs_path, bfs_expansion = bfs(graph, 'Arad', 'Craiov')

print("===== BFS =====")
print("Expansion Order:", bfs_expansion)
print("Path:", bfs_path)

dfs_path, dfs_expansion = dfs(graph,'Arad', 'Craiov')

print("\n===== DFS =====")
print("Expansion Order:", dfs_expansion)
print("Path:", dfs_path)