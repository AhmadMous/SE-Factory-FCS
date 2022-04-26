# Thought process:
# - The two lists are already sorted, therefore it is enough to compare the
# leading data of each to choose the lower to copy to the list we are building
# - We can compare the data of the lists while we aren't pointing to None
# - Thus we can create pointers to advance through the list to allow for comparisons
# - Thus we can loop while neither pointers of nodes in the lists are zero
# - When one of the lists is exhausted, it is enough to copy the remaining nodes of the other list
# as they are already sorted


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

# Function to create a merge of 2 linked lists
def merge_linked_lists(linked_list_1, linked_list_2):

    # The linked list which will be the resultant
    new_list = LinkedList()

    # Handles case where both input lists are empty
    if linked_list_1.length == 0 and linked_list_2.length == 0:
        return new_list

    # Pointers to traverse input linked lists
    pointer_1, pointer_2  = linked_list_1.head, linked_list_2.head

    # Dummy node at head to facilitate merge
    new_list.add_at_head(Node())
    main_pointer = new_list.head

    # Loop over the nodes while you can compare the data they carry
    while pointer_1 is not None and pointer_2 is not None:

        # There are still nodes to compare, meaning there are nodes to fill
        main_pointer.next = Node()
        main_pointer = main_pointer.next

        
        # Copy data of smaller node, and increment respective pointer to next node in that list
        if pointer_1.data <= pointer_2.data:
            main_pointer.data = pointer_1.data
            pointer_1 = pointer_1.next

        else:
            main_pointer.data = pointer_2.data
            pointer_2 = pointer_2.next


    # Exhaust the list which is not empty by copying remaining nodes
    for pointer in (pointer_1, pointer_2):
        while pointer is not None:
            main_pointer.next = Node()
            main_pointer = main_pointer.next
            main_pointer.data = pointer.data
            pointer = pointer.next

    # Remove dummy node, correct the length of the list, and return
    new_list.remove_first_node()
    new_list.length = linked_list_1.length + linked_list_2.length
    return new_list

#For Testing
def test_ll():

    # Create 2 empty linked lists
    test_list = LinkedList()
    test_list2 = LinkedList()

    # Fill the 2 lists with values
    for i in range (8 ,0, -2):
        new_node = Node(i)
        test_list.add_at_head(new_node)

    for i in range (9 ,1, -2):
        new_node = Node(i)
        test_list2.add_at_head(new_node)

    # Merge the resultant and view it backwards
    merge_list = merge_linked_lists(test_list, test_list2)
    test_list.print_list()
    test_list2.print_list()
    merge_list.print_list()

test_ll()