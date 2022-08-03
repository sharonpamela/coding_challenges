'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''

class Stack(object):
    def __init__(self):
        self.stack = []
        self.min_num = []

    def push (self, item):
        #  Add an item to the top of the stack
        self.stack.append(item)
        if len(self.min_num) == 0 or (len(self.min_num) > 0 and self.min_num[-1] > item):
            self.min_num.append(item) 
      
    def pop(self):
        # Remove item from the top of the stack if not empty.
        if len(self.stack) == 0:
            return False
        removed = self.stack.pop()
        if removed == self.min_num[-1]:
            self.min_num.pop()
        return removed

    def peek(self):
        # Return the top of the stack.
        if len(self.stack) == 0:
            return False
        return self.stack[-1]

    def isEmpty(self):
        # Return true if and only if the stack is empty
        return len(self.stack) == 0

    def stack_min(self):
        # returns the smallest elem in the stack if it exists else None
        return self.min_num[-1] if len(self.min_num) > 0 else None