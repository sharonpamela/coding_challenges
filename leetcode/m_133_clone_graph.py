'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) 
and a list (List[Node]) of its neighbors.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''
from collections import deque
from signal import valid_signals

# def cloneGraph(node):
#     old_new = {}
#     q = deque()
#     q.append((None, node))

#     if not node: return None

#     #breath first search aproach
#     while q:
#         c,cur = q.popleft()
#         copy = Node(cur.val)

#         # now we can link the neighbor that lead to this node
#         if c:
#             c.neighbors.append(copy)
#         old_new[cur] = copy

#         # navigate thru all neighbors of current node and add them to q
#         for n in cur.neighbors:
#             if n not in old_new:
#                 # append cur node's copy and its neighbor to the q
#                 # so that the cur -> clone(n) link can be stablished later
#                 q.append((copy,n))

#     return old_new(node)


def cloneGraph(node):
    old_new = {}

    #depth first search recursive aproach
    def clone(node):
        if node in old_new:
            # dont create a new clone if already created
            return old_new[node]
        copy = Node(node.val)
        old_new[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(clone(n))
        return copy
    return clone(node) if node else None