'''Linked List in Python'''

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None    # pointer to next node

class linked_list:
    def __init__(self):
        self.head = node()  # initialize head node  

    def append(self, data):
        new_node = node(data)
        
        if (new_node != None):
            # successfully allocated memory for the new node
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node  # at last node, insert new node

        else:
            print("Node creation is unsuccessful.")

    def insert_inOrder(self, data):
        '''For inserting node in correct index'''
        new_node = node(data)
        prev = None 
        curr = self.head    

        if (new_node != None):
            # successful allocation of memory for node
            if (curr.next == None):
                # empty list, insert at front
                curr.next = new_node
                return
            
            else:
                # list is not empty, iterate through it until right spot is found
                while (curr.next != None and (curr.data <= curr.next.data)):
                    prev = curr
                    curr = curr.next
        
        prev.next = new_node
        new_node.next = curr
    
    def del_node(self, index):
        '''Delete the node at certain index'''
        prev = None
        curr = self.head

        for i in range(index + 1):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

    def length(self):
        curr = self.head
        nodes_count = 0
        while curr.next != None:
            nodes_count += 1
            curr = curr.next
        
        return nodes_count
    
    def print_list(self):
        curr = self.head
        print("--> ")
        while curr.next != None:
            curr = curr.next
            print(str(curr.data) + "--> ")
    
    def get(self, index):
        '''get the data at a certain index'''
        curr = self.head

        if (index >= self.length()): 
            print("ERROR: Index out of range!") 
            return None

        for i in range(index + 1):
            curr = curr.next

        print(curr.data)
    

ex_link = linked_list() # initialize the linked list
ex_link.insert_inOrder(69)
ex_link.insert_inOrder(42)
ex_link.insert_inOrder(50)

ex_link.print_list()