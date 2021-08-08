'''
Question: Given an UNSORTED doubly linked list, 
1. write a function to sort the values in order of least to greatest (increasing) 
2. and then write another function to insert a value in a sorted way. 
-- Explain the sorting algorithm you chose and why. --
Task 1: Sort the doubly linked list in increasing order 
Ex.: 10, 8, 5, 3, 12
Output: 3 <-> 5 <-> 8 <-> 10 <-> 12

Task 2: Insert a value while maintaining sorted order 
Example: If the value of 9 were given, the insertion would accomplish maintaining order and insertion as the example given below.
Output: 3 <-> 5 <-> 8 <-> 9 <-> 10 <-> 12
'''

class node():
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.next = prev
        self.prev = next

class DubLinked:
    def __init__(self) -> None:
        self.head = node()

    def append_node(self, data):
        new_node = node(data)

        if (new_node != None):
            curr = self.head
            # successful allocation of memory for node
            while (curr.next != None):
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    def print_list(self):
        curr = self.head.next

        print("--> ", end="")
        while (curr != None):
            print(f"<--{curr.data}-->", end="")
            curr = curr.next

linky = DubLinked()
linky.append_node(10)
linky.append_node(8)
linky.append_node(5)
linky.append_node(3)
linky.append_node(12)
linky.print_list()