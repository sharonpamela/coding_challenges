'''
Paths with Sum: You are given a binary tree in which 
each node contains an integer value (which
might be positive or negative). 
Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at 
the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes). 
'''
import sys
sys.path.append(".")
from testing_binary_tree import Node


def count_paths_with_sum(root, target_sum):
    hash_map = {}
    return recurse_count_paths_with_sum(root, target_sum, 0, hash_map)

def recurse_count_paths_with_sum(node, target_sum, running_sum, path_count_hash):
    
    if node is None: return 0

    # count paths with sum ending at the current node
    running_sum += node.data
    new_sum = running_sum - target_sum
    total_paths = get_or_set(path_count_hash, new_sum)

    # if running sum equals target_sum, then the one additional path
    # starts at root
    if running_sum == target_sum:
        total_paths += 1

    # increment path_count_hash, recurse, then decrement path_count_hash
    increment_hash_table(path_count_hash, running_sum, 1)
    total_paths += recurse_count_paths_with_sum(node.left, target_sum, running_sum, path_count_hash)
    total_paths += recurse_count_paths_with_sum(node.right, target_sum, running_sum, path_count_hash)
    increment_hash_table(path_count_hash, running_sum, -1)

    return total_paths


def get_or_set(hash_map, key):
    # given a hash map and a value, add the key to it
    # if not already there with value of 0
    if key not in hash_map:
        hash_map[key] = 0

    return hash_map[key]


def increment_hash_table(hash_table, key, delta):
    new_count = get_or_set(hash_table, key) + delta
    
    if new_count == 0:
        # remove key with counts 0
        del hash_table[key]
    else:
        hash_table[key] = new_count

# Building a sample tree:
root = Node(10)
root.insert(5)
root.insert(-3)
root.insert(3)
root.insert(1)
root.insert(11)
root.insert(3)
root.insert(-2)
root.insert(2)
# print(root)

print(count_paths_with_sum(root, 8))

# brute force approach: visit every node, look at all possible paths
'''
In a balanced binary tree, d will be no more than approximately log N. 
Therefore, we know that with N nodes in the tree, 
count_paths_with_sum_from_node will be called O(N log N) times. 
runtime: O(N log N)
'''
# def brute_count_paths_with_sum(node, target_sum):
#     if node is None: return 0

#     # count paths wiht sum starting from the root
#     paths_from_root = count_paths_with_sum_from_node(root, target_sum, 0)

#     paths_on_left = brute_count_paths_with_sum(root.left, target_sum)
#     paths_on_right = brute_count_paths_with_sum(root.right, target_sum)

#     return paths_from_root + paths_on_left + paths_on_right

# def count_paths_with_sum_from_node(node, target_sum, current_sum):
#     # returns the number of paths with this sum starting from this node
#     if node is None: return 0

#     current_sum += node.data

#     total_paths = 0
#     if current_sum == target_sum:
#         total_paths += 1
    
#     total_paths += count_paths_with_sum_from_node(node.left, target_sum, current_sum)
#     total_paths += count_paths_with_sum_from_node(node.right, target_sum, current_sum)
#     return total_paths