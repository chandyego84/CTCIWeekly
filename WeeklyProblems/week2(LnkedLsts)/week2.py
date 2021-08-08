'''
Week 2 Coding Question (Isaac Chepkwony):
Reversing a sublist: Given the head of a linked list and two positions 'p' and 'q',
reverse the linked list from position 'p' to 'q'.
Ex.: 
Original List 1-> 2-> 3-> 4-> 5-> null if p=2 and q=4
Resulting List 1-> 4-> 3-> 2-> 5-> null
------------------------------------------------
BONUS QUESTION: Given the head of a singly linked list and number 'k',
rotate the linked list to the right by 'k' nodes
Ex.:
Original List 1-> 2-> 3-> 4-> 5-> null if k = 3
Resulting List 3-> 4-> 5-> 1-> 2-> null
'''

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()  # head node 
    
    def append(self, data):
        new_node = node(data)
        curr = self.head

        if (new_node != None):
            # successfully made the new node
            if (curr.next == None):
                # empty list, insert at front 
                curr.next = new_node
            
            else:
                # non-empty list
                while (curr.next != None):
                    curr = curr.next
        
        curr.next = new_node
    
    def length(self):
        curr = self.head
        num_nodes = 0

        if (curr.next != None):
            # list is not empty
            while (curr.next != None):
                curr = curr.next
                num_nodes += 1
        
        return num_nodes
    
    def rev_subslis(self, p, q):
        '''Given the head node, p, and q; reverse so q --> p --> ...'''
        prev = None
        curr = self.head
        
        if (curr.next == None or p == q): return  # empty list or range is 0

        else:
            # loop to get to the "p" node 
            for i in range(p):
                prev = curr
                curr = curr.next
            before_start = prev # node before the starting node ("node p") of the given range
            start = curr    # "node p"

            # loop to move through "node p" to "node q"
            for n in range((q - p) + 1):
                next = curr.next    # node ahead of curr node 
                curr.next = prev    # reverse the curr node pointer 
                prev = curr     # update prev node 
                curr = next     # move to the next node 
            
            before_start.next = prev    # node before "node p" points to "node q"
            start.next = curr   # "node p" points to what "node q" was initially pointing to
    
    def rotate_list(self, k):
        '''Given the head node and k, rotate the list to the right by k'''
        curr = self.head
        len = self.length()

        if (curr.next == None or k == len or k == 0): return    # list is empty or rotate # does nothing

        else:
            front = curr.next   # front of the list

            for i in range(len - k):
                # go to the starting node of the range to rotate 
                prev = curr
                curr = curr.next
            before_start = prev.next # node right before starting node of the range to rotate
            start = curr.next    # starting node of the range to rotate 

            for n in range(k):
                # move through the range of nodes to rotate
                prev = curr
                curr = curr.next
            end = curr  # node at the end of the list

            self.head.next = start  # head points to the starting node of the range 
            end.next = front    # end of the list points to front of list
            before_start.next = None    # node before starting node points to NULL 

    def print_list(self):
        curr = self.head

        print("--> ")
        while (curr.next != None):
            curr = curr.next
            print(str(curr.data) + "--> ")

if __name__ == '__main__':
    nums_arr = [1, 2, 3, 4, 5]
    # test cases
    print("LINKED LIST 1: REVERSE 2, 3 AND ROTATE 3")
    test_list = linked_list()
    for n in nums_arr: test_list.append(n)
    test_list.rev_subslis(2, 3)
    test_list.print_list()
    test_list.rotate_list(3)
    test_list.print_list()
    print("**********")
    print("LINKED LIST 2: REVERSE 0, 0 AND ROTATE 0")
    test_list2 = linked_list()
    for n in nums_arr: test_list2.append(n)
    test_list2.rev_subslis(0, 0)
    test_list2.print_list()
    test_list2.rotate_list(0)
    test_list2.print_list()
    print("**********")
    print("LINKED LIST 3: REVERSE 1, 5 AND ROTATE 5")
    test_list3 = linked_list()
    for n in nums_arr: test_list3.append(n)
    test_list3.rev_subslis(1, 5)
    test_list3.print_list()
    test_list3.rotate_list(5)
    test_list3.print_list()
    print("**********")