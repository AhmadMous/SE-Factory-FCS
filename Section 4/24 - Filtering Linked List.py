# Class for node of a linked list or queue
class Node:

    # Initializes data and pointer to next node 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

# Class for linked list
class LinkedList:

    # Initializes LL length and pointer to its head node = 0
    def __init__(self):
        self.length = 0
        self.head = None
    

    # Iterates over nodes of the list, printing them
    def print_list(self):

        # Start with node at the head of the LL
        node = self.head

        # While end is not reached
        while node is not None:

            # Print the node, and then set it to equal the next node
            print(node, end=' ')
            node = node.next
        print('')
    

    # Adds a node at the head of the LL
    def add_at_head(self, node):

        # First sets the pointer of the node to the current head, then points head to new node
        node.next = self.head
        self.head = node
        self.length += 1
    

    # Removes node after parameter node
    def remove_node_after(self, node):

        # If not at the end of the list
        if node.next is not None:

            # Keep track the next node
            temp = node.next

            # Make the next attribute to the node after next node
            node.next = node.next.next

            # Clear next node
            temp.next = None
            self.length -= 1
    

    # Removes first node of the linked list
    def remove_first_node(self):

        # If the node is empty, return
        if self.head is None:
            return

        # Keep track of first node, which head points to
        temp = self.head

        # Set head to point to the following node
        self.head = self.head.next

        # Clear the next pointer of old head
        temp.next = None
        self.length -= 1
    
    
    # Prints the LL backwards
    def print_backward(self):
        
        # Helper function that prints the LL backwards
        def print_nodes_backward(node):

            # If there exists a next node, print that first
            if node.next is not None:
                print_nodes_backward(node.next)

            # After printing next node, if the node isn't empty, print it
            if node is not None:
                print(node, end=' ')
        
        # If the list isn't empty, invoke the helper function
        if self.head is not None:
            print_nodes_backward(self.head)
        
        print('')


# Filters nodes with odd data out of the linked list
def filter_even(ll):

    # Handles case where head node is odd
    while (ll.head is not None) and (ll.head.data % 2 != 0):
        ll.remove_first_node()

    # Create a pointer to use for LL traversal
    pointer = ll.head
    while pointer is not None and pointer.next is not None:

        # Check if next node has odd data, delete it using method of it does
        if pointer.next.data % 2 != 0:
            ll.remove_node_after(pointer)

        # Else move to nxt node
        else:
            pointer = pointer.next

# For Testing
# def test_ll(test_fn):
#     test_list = LinkedList()
#     for i in range (8 ,0, -1):
#         new_node = Node(i)
#         test_list.add_at_head(new_node)
#     test_list.print_backward()
#     test_fn(test_list)
#     test_list.print_backward()
#     return test_list

# test_ll(filter_even)