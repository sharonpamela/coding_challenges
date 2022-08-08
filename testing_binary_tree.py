from collections import deque

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def in_order_traverse(self):
        if self.left:
            self.left.in_order_traverse()
        print(self.data)
        if self.right:
            self.right.in_order_traverse()

    def insert(self, new_data):
        q = deque()
        q.append(self)

        while len(q) > 0:
            curr_node = q.popleft()
            
            if curr_node is None:
                curr_node = new_data
                break
            elif curr_node.left is None:
                curr_node.left = Node(new_data)
                break
            elif curr_node.right is None:
                curr_node.right = Node(new_data)
                break
        
            if curr_node.left is not None:
                q.append(curr_node.left)
            if curr_node.right is not None:
                q.append(curr_node.right)

        
    def __repr__(self):
        if self.right is not None:
            fmt = '{}({data!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({data!r}, {left!r})'
        else:
            fmt = '{}({data!r})'
        return fmt.format(type(self).__name__, **vars(self))


# Building a sample tree:
# root = Node(5)
# root.insert(2)
# root.insert(8)
# root.insert(1)
# root.insert(3)
# root.insert(4)
# root.insert(6)
# root.insert(9)
# root.insert(7)
# root.insert(10)
# root.insert(1)
# root.insert(1)
# root.insert(1)
# root.insert(20)
# root.insert(30)


