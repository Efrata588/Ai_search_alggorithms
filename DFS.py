from collections import deque
from common.path_reconstruction import reconstruct_path

def dfs(graph,start,goal):
    stack=[start]
    visted=set()
    parent={}
    expansion_order=[]
    found =False
    


    while stack:
        node=stack.pop()
        if node not in visted:
            visted.add(node)
            expansion_order.append(node)

            if node == goal:
                found=True
                break

            for neighbor,_ in graph[node]:#Therfore it starts from the right most
                if neighbor not in visted:
                    stack.append(neighbor)
                    parent[neighbor]=node

    if not found:
        print('Goal was not found')
        return None,expansion_order

    path=reconstruct_path(parent,start,goal)

    return path, expansion_order

            
