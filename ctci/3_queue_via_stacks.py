'''
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks. 

'''

class Queue(object):
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, item):
        self.stack_a.append(item)

    def pop(self):
        if len(self.stack_b) != 0:
            return self.stack_b.pop()
        else:
            while len(self.stack_a) > 0:
                self.stack_b.append(self.stack_a.pop())
            return self.stack_b.pop()

    def peek(self):
        if len(self.stack_b) > 0:
            return self.stack_b[-1]
        elif len(self.stack_a) > 0:
            return self.stack_a[0]
        else:
            raise Exception("Empty stack")

    def isEmpty(self):
        return len(self.stack_a) == 0 and len(self.stack_b) == 0


    def __repr__(self):
        final_list = []
        for i in range(len(self.stack_b)-1, -1, -1):
            final_list.append(str(self.stack_b[i]))
        for i in range(len(self.stack_a)):
            final_list.append(str(self.stack_a[i]))
        return ",".join(final_list)


testq = Queue()
testq.push(1) 
print("print [1]: ", testq)
testq.push(2)
testq.push(3)
print("print [1,2,3]: ", testq)
print("pop -> print 1: ", testq.pop())
print("print [2,3]: ", testq)
print("peek - > print 2: ", testq.peek())
testq.push(4)
print("print [2,3,4]: ", testq)
