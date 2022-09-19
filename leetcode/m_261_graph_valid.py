'''
You have a graph of n nodes labeled from 0 to n - 1. 
You are given an integer n and a list of edges where 
edges[i] = [ai, bi] indicates that there is an 
undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up 
a valid tree, and false otherwise.
'''

def validTree(n, edges):
 # create adjacency list of all nodes and edges
        if not n:
            return True
        
        # create adjacency list of all nodes and edges
        adj_list = { i:[] for i in range(n) }
        for n1,n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                # loop detected: node has already been visited
                return False
            
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == prev:
                    # skip the neighbor that led to current node
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)