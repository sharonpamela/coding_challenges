'''
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack

'''

class SetOfStacks(object):

    def __init__(self):
        self.stacks = []
        self.capacity = 4

    def push(self, item):
        last_stack = self.get_last_stack()
        if (last_stack is not None and self.isFull(last_stack) is False):
            last_stack.append(item)
        else:
            # create a new stack
            new_stack = []
            new_stack.append(item)
            self.stacks.append(new_stack)
    
    def pop(self):
        last_stack = self.get_last_stack()
        if last_stack is not None:
            removed = last_stack.pop()
            if len(last_stack) == 0:
                self.stacks.pop()
            return removed
        else:
            raise Exception("Empty stack")

    def get_last_stack(self):
        if len(self.stacks) > 0:
            return self.stacks[-1]
        else:
            return None

    def isFull(self, stack):
        return len(stack) >= self.capacity

    def __repr__(self):
        final_list = []
        for stack in self.stacks:
            for item in stack:
                final_list.append(str(item))
        return ",".join(final_list)
            
newPlateStack = SetOfStacks()
newPlateStack.push(1)
print(newPlateStack)
newPlateStack.push(2)
print(newPlateStack)
newPlateStack.push(3)
print(newPlateStack)
newPlateStack.push(3)
print(newPlateStack)
newPlateStack.push(3)
print(newPlateStack)
newPlateStack.push(3)
print(newPlateStack)
newPlateStack.pop()
print(newPlateStack)
newPlateStack.pop()
print(newPlateStack)
newPlateStack.pop()
print(newPlateStack)
newPlateStack.pop()
print(newPlateStack)
newPlateStack.pop()
print(newPlateStack)
newPlateStack.pop()
# newPlateStack.pop()
print(newPlateStack)


