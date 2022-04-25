# Thought process:
# - Lists of unequal sizes can't be equal
# - Empty lists are equal
# - For lists of same size, traverse both at same time
# If we find a difference, then they are unequal, else they are equal


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



# Function that returns whether 2 linked lists are equal
def equal_linked_lists(linked_list_1, linked_list_2):

    # Lists are of unequal length
    if linked_list_1.length != linked_list_2.length:
        return False
    
    # Lists are empty
    elif linked_list_1.head == None and linked_list_2.head == None:
        return True

    # Both lists unempty and of same length
    else:

        # Create pointers to traverse respective lists
        pointer_1 = linked_list_1.head
        pointer_2 = linked_list_2.head

        # Traverse list till it is finished
        while pointer_1 is not None:

            # If any node has different data than other respective node -> unequal
            if pointer_1.data != pointer_2.data:
                return False

            # Point to next nodes
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

        # No difference found, every node of each list has respective equal node in other list 
        return True