'''
CTCI Chapter 3: Stacks and Queues Interview Questions
'''
from collections import deque

'''3.2: How would you design a stack which, in addition to push and pop, 
has a function min which returns the minimum element? Push, pop, and min should all
operate in O(1) time.
'''

class myStack:
    def __init__(self, list) -> None:
        self.stack = list
        self.min = None     # min element in the stack
        self.mins_stack = myStack()

    def print_stack(self):
        stacky = self.stack
        
        print([i for i in stacky])
    
    def push(self, elem):
        stacky = self.stack

        if not stacky:
            # stack is empty
            stacky.append(elem)
            self.min = elem
        
        else:
            # stack is not empty
            if (elem < self.min):
                # new element is the min
                self.min = elem

    def pop(self):
        stacky = self.stack[:-1]
        self.stack = stacky

        return self.stack[-1]
    
    def get_min(self):
        return self.min
    



# MY STACK: ALL OPERATIONS (EXCEPT PRINT) TO BE IN O(1)
stark = myStack([])
# PUSHING #
stark.push(3)
stark.push(1)
stark.push(0)
stark.push(42)
stark.push(69)
stark.print_stack()
# POPPING #'
stark.pop()
stark.pop()
stark.pop()
stark.pop()
stark.print_stack()
# MIN VAL #
print(stark.get_min())
