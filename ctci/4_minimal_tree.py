'''
Minimal Tree: Given a sorted (increasing order) array with unique 
integer elements, write an algorithm to create a binary search 
tree with minimal height. 
'''
import math

def create_minimal_binary_tree(arr):
    return insert_into_tree(arr, 0, len(arr)-1)

def insert_into_tree(arr, start, end):
    if end < start:
        return None

    middle = math.floor((start+end)/2)
    n = Node(arr[middle])
    n.left = insert_into_tree(arr, start, middle-1)
    n.right = insert_into_tree(arr, middle+1, end)
    return n


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

sorted_arr = [1,2,3,4,5,6,7,8,9,10]
root = create_minimal_binary_tree(sorted_arr)
root.PrintTree()