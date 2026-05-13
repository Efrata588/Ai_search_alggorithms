from collections import deque
from common.path_reconstruction import reconstruct_path

def bfs(graph,start,goal):
    queue=deque([start])
    visited = set ([start])
    parent={}
    expansion_order=[]

    while queue:
        current_node=queue.popleft()
        expansion_order.append(current_node)


        if current_node == goal:
            break

        for neighbour,_ in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour]=current_node
                queue.append(neighbour)
        
    path=reconstruct_path(parent,start,goal)
    return path, expansion_order







