import heapq
from common.path_reconstruction import reconstruct_path

def ucs(graph, start, goal):
    priority_queue = [(0, start)]
    visited = {}  
    parent = {start: None}
    expansion_order = []
    
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        

        if current_node in visited and visited[current_node] <= current_cost:
            continue
            
        visited[current_node] = current_cost
        expansion_order.append(current_node)
        
        if current_node == goal:
            path = reconstruct_path(parent, start, goal)
            return path, expansion_order, current_cost
        
        
        for neighbor, edge_cost in graph[current_node]:
            new_cost = current_cost + edge_cost
            if neighbor not in visited or new_cost < visited.get(neighbor, float('inf')):
                parent[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))
                
    print('Goal was not found')
    return None, expansion_order, 0