'''
Three in One: Describe how you could use a single array to implement three stacks. 
'''

class ThreeStacks_in_one(object):
    '''
    using a single array, we could divide the array into 3 (limited)
    partitions and only allow the stacks to grow within their respective
    partition.
    '''
    def __init__(self, stack_size):
        self.num_of_stacks = 3
        self.stack_capacity = stack_size
        self.total_values = [ 0 ] * (self.stack_capacity * self.num_of_stacks)
        self.sizes_tracker = [0] * self.num_of_stacks

    def push(self, stack_num, value):
        # adjust stack_num to be the index number
        
        if self.isFull(stack_num):
            raise Exception(f"Stack number {stack_num-1} is full")
        
        self.sizes_tracker[stack_num]+=1
        self.total_values[self.top_index(stack_num)] = value

    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            raise Exception(f"Stack number {stack_num-1} is empty")
        
        top_index = self.top_index(stack_num)
        value = self.total_values[top_index]
        self.total_values[top_index] = 0
        self.sizes_tracker[stack_num]-=1
        return value

    def isFull(self, stack_num):
        return self.stack_capacity > self.sizes_tracker[stack_num]

    def top_index(self, stack_num):
        # get starting index
        starting_idx = self.stack_capacity * stack_num
        # add the size and subtract one to get index
        stack_size = self.sizes_tracker[stack_num]
        return starting_idx + stack_size - 1

    def isEmpty(self, stack_num):
        return self.sizes_tracker[stack_num] == 0

    def peek(self, stack_num):
        return self.top_index(stack_num)