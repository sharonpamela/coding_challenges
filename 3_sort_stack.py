'''
Sort Stack: Write a program to sort a stack such that 
the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the 
elements into any other data structure
(such as an array). The stack supports the following 
operations: push, pop, peek, and is Empty.
'''

def sort_stack(stack):
    min_seen = float('inf')
    temp_stack = Stack()
    items_sorted = 0
    total_elems = stack.getLength()

    while items_sorted != total_elems:
        min_seen = stack.peek()
        while stack.getLength() > 0:
            curr_item = stack.pop()
            min_seen = min(min_seen, curr_item)
            temp_stack.push(curr_item)

        while temp_stack.getLength() > items_sorted:
            curr_elem = temp_stack.pop()
            if curr_elem != min_seen:
                stack.push(curr_elem)

        # place first sorted item in the temp stack
        temp_stack.push(min_seen)
        items_sorted += 1
    while temp_stack.getLength() > 0:
        stack.push(temp_stack.pop())


class Stack(object):
    def __init__(self):
        self.stack = []
        self.min_num = []
        self.len  = 0

    def push (self, item):
        #  Add an item to the top of the stack
        self.stack.append(item)
        if len(self.min_num) == 0 or (len(self.min_num) > 0 and self.min_num[-1] > item):
            self.min_num.append(item)
        self.len +=1
      
    def pop(self):
        # Remove item from the top of the stack if not empty.
        if len(self.stack) == 0:
            return False
        removed = self.stack.pop()
        if removed == self.min_num[-1]:
            self.min_num.pop()
        self.len -=1
        return removed

    def peek(self):
        # Return the top of the stack.
        if len(self.stack) == 0:
            return False
        return self.stack[-1]

    def getLength(self):
        return self.len

    def isEmpty(self):
        # Return true if and only if the stack is empty
        return len(self.stack) == 0

    def getMin(self):
        # returns the smallest elem in the stack if it exists else None
        return self.min_num[-1] if len(self.min_num) > 0 else None

    def __repr__(self):
        final_list = []
        for item in self.stack:
            final_list.append(str(item))
        return ",".join(final_list)


s = Stack()
s.push(3)
s.push(1)
s.push(2)
print(s)
sort_stack(s)
print("sorted: ", s)

s1 = Stack()
s1.push(2)
s1.push(1)
s1.push(3)
print(s1)
sort_stack(s1)
print("sorted: ", s1)