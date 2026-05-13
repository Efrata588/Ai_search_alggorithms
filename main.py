from common.graph import graph
from BFS import bfs
from DFS import dfs
from UCS import ucs
bfs_path, bfs_expansion = bfs(graph, 'Arad', 'Craiov')

print("===== BFS =====")
print("Expansion Order:", bfs_expansion)
print("Path:", bfs_path)

dfs_path, dfs_expansion = dfs(graph,'Arad', 'Craiov')

print("\n===== DFS =====")
print("Expansion Order:", dfs_expansion)
print("Path:", dfs_path)

ucs_path, ucs_expansion, ucs_cost = ucs(graph, 'Arad', 'Craiov')

print("\n===== UCS =====")
print("Expansion Order:", ucs_expansion)
print("Path:", ucs_path)
print("Total Path Cost:", ucs_cost) 