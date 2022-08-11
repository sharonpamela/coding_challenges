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
            if self.data:
                if new_data <= self.data:
                    if self.left is None:
                        self.left = Node(new_data)
                    else:
                        self.left.insert(new_data)
                elif new_data > self.data:
                    if self.right is None:
                        self.right = Node(new_data)
                    else:
                        self.right.insert(new_data)
            else:
                self.data = new_data

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


