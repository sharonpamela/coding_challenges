'''
Route Between Nodes: Given a directed graph, 
design an algorithm to find out whether there is a
route between two nodes. 
'''
'''
i'm assuming the graph looks as follows:
graph = {
  0 : [1,4,5],
  1 : [3,4],
  2 : [1],
  3 : [2,4],
  4 : [],
  5 : []
}
'''
from collections import deque

def find_route(g, nodea, nodeb):

    q = deque()
    visited = [nodea]
    q.append(nodea)

    while len(q) > 0:
        node = q.popleft()
        if node == nodeb:
            return True
        
        if node not in visited:
            visited.append(node)

        for neighbor in g[node]:
            if neighbor not in q and neighbor not in visited:
                q.append(neighbor) 
    
    return False

graph = {
  0 : [1,4,5],
  1 : [3,4],
  2 : [1],
  3 : [2,4],
  4 : [],
  5 : []
}

print(find_route(graph, 2, 4)) # True
print(find_route(graph, 3, 0)) # false
print(find_route(graph, 0, 3)) # True