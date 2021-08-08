'''
CTCI Chapter 2: Linked Lists
'''
from collections import deque

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class link_list:
    def __init__(self):
        self.head = node()  # initialize the head node
    
    def append_node(self, data):
        new_node = node(data = data)
        curr = self.head

        if (new_node != None):
            # successfully allocated memory for new node
            if curr.next == None:
                # list is empty
                curr.next = new_node
            
            else:
                while(curr.next != None):
                    curr = curr.next
            
            curr.next = new_node
    
    def append_front(self, data):
        new_node = node(data = data)
        curr = self.head

        if (new_node != None):
            # successfully allocated memory for new node
            temp = curr.next    # node/null that the new node inserted @ front points to
            new_node.next = temp
            curr.next = new_node
    
    def insert_node(self, node):
        curr = self.head

        if (curr.next == None):
            curr.next = node
        
        else:
            while (curr.next != None):
                curr = curr.next
            curr.next = node

    def del_dups(self):
        '''2.1: Remove Dups; Write code to remove duplicates from an unsorted linked list
        BONUS: How might you do this w/out a temporary buffer?'''
        data_map = {}
        prev = None
        curr = self.head

        if curr.next == None:
            return
        
        else:
            while curr.next != None:
                prev = curr
                curr = curr.next
                if (curr.data not in data_map):
                    # data is new, add it to hash table
                    data_map[curr.data] = curr.data
                
                else: 
                    # data was already in hash table
                    prev.next = curr.next
    
    def len_list(self):
        lis_len = 0
        curr = self.head

        while (curr.next != None):
            lis_len += 1
            curr = curr.next
        
        return lis_len

    def kth_last(self, k):
        '''2.2: Find the kth to last element of a singly linked list'''
        lis_len = 0
        curr = self.head

        if (curr.next == None): return  # list is empty

        else:
            lis_len = self.len_list()

        curr = self.head    # reset

        for n in range(lis_len - (k -1)):
            # go to the kth element
            curr = curr.next
        
        return curr.data
    
    def del_mid(self, target):
        '''2.3: Delete a node in the middle (not the first or last node)'''
        steps = 0   # times we've gone through the list
        lis_len = self.len_list()
        prev = None
        curr = self.head

        if (curr.next == None): return  # empty list, can't delete jack

        else:
            for s in range(lis_len):
                prev = curr
                curr = curr.next
                steps += 1
                if (curr.data == target and (steps != 1 and steps != lis_len)):
                    # match found, del it 
                    prev.next = curr.next
    
    def partition(self, part_val):
        '''2.4: Partition a linked list around a value x, such that all nodes < x come before all nodes >= x'''
        curr = self.head
        bef_part = []   # stores nodes < partitioning val
        aft_part =[]      # stores nodes >= partitioning val

        if (curr.next == None): return  # list is empty

        else:
            # list is filled
            while (curr.next != None):
                # move through list and append node to correct list
                curr = curr.next
                
                if (curr.data < part_val):
                     bef_part.append(curr)
                
                elif (curr.data >= part_val):
                    aft_part.append(curr)
            
            if (bool(bef_part)):
                self.head.next = bef_part[0]
                # reorder nodes less than partition value
                for n in range(len(bef_part) - 2):
                    bef_part[n].next = bef_part[n + 1]
                bef_part[len(bef_part) - 1].next = aft_part[0]

            else:
                self.head.next = aft_part[0]

            for n in range(len(aft_part) - 2):
                aft_part[n].next = aft_part[n + 1]
            aft_part[len(aft_part) - 1].next = None
    
    def is_palindrome(self):
        '''2.6: Check if a linked list is a palindrome'''
        is_palin = True
        curr = self.head
        list_len = self.len_list()
        val_holder = deque([])

        print(list_len)
        if (list_len <= 1): return is_palin
        
        elif (list_len == 2): 
            is_palin = False

        else:
            while (curr.next != None):
                # add all node values to the list
                curr = curr.next
                val_holder.append(curr.data)
            
            # reverse the linked list, then compare with val stack
            prev = None
            curr = self.head.next
            while (curr != None):
                next = curr.next    # node in front of curr
                curr.next = prev    # reverse current nodes pointer
                prev = curr     # update prev node
                curr = next     # update to following node
            self.head.next = prev
            
            # check if palindorme
            curr = self.head.next
            while (curr != None and bool(val_holder)):
                if (curr.data != val_holder.pop()):
                    is_palin = False
                curr = curr.next

        return is_palin
    
    def find_loop(self):
        '''2.8: Given a circularly linked list, return the node at the beginning of the loop'''
        curr = self.head.next
        lag = curr
        steps = 0

        if (curr == None):
            return 'This linked list does not have a loop'
        
        else:
            while (curr != None):
                curr = curr.next
                steps += 1
                if (steps % 2 == 0):
                    lag = lag.next
                if (curr == lag):
                    print(f"The loop starts with the node whose value is {curr.data}")
                    return curr
                

    def print_list(self):
        curr = self.head

        print("--> ")
        while(curr.next != None):
            curr = curr.next
            print(str(curr.data) + "--> ")


def sum_lists(head1, head2):
    '''2.5: Two numbers represented by a linked list, each node contains a single digit and the digits are in
    reverse order such that the 1's digit is the head of the list. Add the two lists/numbers and returns the sum in reverse order
    E.g.: Input: (7->1->6) + (5->9->2) is 617 + 295 
        Output: 2->1->9 which is actually 912
    '''
    sum1 = 0
    sum2 = 0
    sumFin = 0
    tens_count = 0

    # add both numbers in linked lists 
    curr = head1
    while (curr.next != None):
        curr = curr.next
        sum1 += (10 ** tens_count) * curr.data
        tens_count += 1
    
    curr = head2 
    tens_count = 0
    while (curr.next != None):
        curr = curr.next
        sum2 += (10 ** tens_count) * curr.data
        tens_count += 1
    sumFin = sum1 + sum2

    # creating the reversed sum [linked list]
    tens_digs = len(str(sumFin)) - 1 # length of the sum

    rev_list = link_list()
    while (tens_digs >= 0):
        curr = rev_list.head
        if (curr.next == None): 
            # list is empty
           rev_list.append_node(sumFin // (10 ** tens_digs))
           sumFin -= (sumFin // (10 ** tens_digs) * (10 ** tens_digs))
           tens_digs -= 1
        
        else:
            # list is not empty
            rev_list.append_front(sumFin // (10 ** tens_digs))
            sumFin -= (sumFin // (10 ** tens_digs) * (10 ** tens_digs))
            tens_digs -= 1
    
    return rev_list.print_list()    

def find_intersec(head1, head2):
    '''2.7: Given two (singly) linked lists, determine if the two lists intersect. Return the intersection node.
    Intersection is defined based on reference; kth node of lnklist1 is exact same node as jth node of lnklist2
    '''
    node_map = {}
    curr = head1

    # traverse through first lnked list; add nodes to map
    while (curr.next != None):
        curr = curr.next
        node_map[curr] = curr.data
    
    # traverse through second lnked list; check for intersect
    curr = head2
    while (curr.next != None):
        curr = curr.next
        if (curr in node_map):
            print(f"The node with {curr.data} as its value is an intersection.")
            return curr
    
    print("There is no intersection between the two linked lists.")
    
linky = link_list()
linky.append_node(1)
linky.append_node(2)
loopy_node = node(3)
linky.insert_node(loopy_node)
linky.append_node(4)
monkey_node = node(5)
linky.insert_node(monkey_node)
monkey_node.next = loopy_node
#####################
linky.find_loop()