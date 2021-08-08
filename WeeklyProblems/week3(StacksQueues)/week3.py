'''Week 3: Stacks and Queues
Coding Question: Implement a function Flatten() that takes a multi-level Lnked List
and returns the values ordered by level.
For the multi-level linked list, the nodes follows the same structure as a singly linked list 
but they have an additional property 'child' that points to a node in the next level deeper.  
This can continue.  Down arrows are child relationships. 
Right arrows are next relationships
From pic: A, B, C, D, E, F, G, H, I, J, K, L

BONUS: Instead, change the order of the values by inserting children before
the next parent.
Output: A, F, G, J, H, B, C, D, I, K, L, E
'''

from collections import deque

class node:
    def __init__(self, data=None, child=None):
        self.data = data
        self.next = None    # pointer to next node
        self.child = child   # pointer to child node

class linked_list:
    def __init__(self):
        self.head = node()  # initialize head node  
    
    def append(self, node):
        curr = self.head
        
        if (curr.next == None): 
            # list is empty
            curr.next = node
    
        else:
            # list not empty
            while (curr.next != None):
                curr = curr.next
            # reached end of the list; append the node
            curr.next = node
    
    def flatten(self):
        curr = self.head
        baby_q = deque([]) # stores padawans; init queue
        
        if (self.head == None): return # list is fookin empty
    
        else:
            # list is filled
            while (curr.next != None):
                curr = curr.next
                print(str(curr.data) + "--> ")
                if (curr.child):
                    # curr node has a child
                    baby_q.append(curr.child)
            # reached end of the first level
            
            while (bool(baby_q)):
                # move through the children until queue is empty
                baby = baby_q[0]    # always starting from the beginning
                while (baby != None):
                    print(str(baby.data) + "--> ")
                    if (baby.child):
                        # the child has a child; add it to end of list
                        baby_q.append(baby.child)
                    baby = baby.next
                baby_q.popleft()    # deletion of the first child we used
    
    def child_first(self):
        curr = self.head
        node_vals = []
        baby_stack = deque([])

        print("--> ")
        if (curr.next == None): return

        else:
            # list not empty; move through linked list while pointer != null or stack is !empty
            curr = curr.next
            while (curr or bool(baby_stack)):
                if (curr != None and curr.child):
                    # current node has baby; send node to list
                    node_vals.append(curr)
                    if (curr.next != None):
                        # send its neighbor to the stack
                        baby_stack.append(curr.next)
                    curr = curr.child   # assign pointer to child
                elif (curr != None):
                    # current node has no child; send to list, move to next node
                    node_vals.append(curr)
                    curr = curr.next
                else:
                    # current node == null
                    curr = baby_stack.pop()
                    node_vals.append(curr)
                    if (curr.child):
                        # node has a child in the stack
                        baby_stack.append(curr.next)
                        curr = curr.child
                    else:
                        # node has no child in stack, move to neighbor
                        curr = curr.next
        
        return [i.data for i in node_vals]
                    
    def print_list(self):
        curr = self.head

        print("--> ")
        if (curr.next == None): return  # list is empty

        else:
            # list is not empty
            while (curr.next != None):
                curr = curr.next
                print(str(curr.data) + "--> ")

###### Initialize the linked list ######
lnk_list = linked_list()
###### First node ######
child1 = node(6)    # child of nodeV1 (first level)
child7 = node(10)   # child of nodeV7
child1.next = node(7, child7)   
child1.next.next = node(8)  
nodeV1 = node(1, child1)    # nodeV1 (first level)
lnk_list.append(nodeV1)
###### Second node ######
nodeV2 = node(2)
lnk_list.append(nodeV2)
###### Third node######
nodeV3 = node(3)
lnk_list.append(nodeV3)
###### Fourth node ######
child9 = node(11)   # child of nodeV9
child9.next = node(12)
child4 = node(9, child9)    # child of nodeV4
nodeV4 = node(4, child4)
lnk_list.append(nodeV4)
###### Fifth node ######
nodeV5 = node(5)
lnk_list.append(nodeV5)
###### Testing ######
print(lnk_list.child_first())
