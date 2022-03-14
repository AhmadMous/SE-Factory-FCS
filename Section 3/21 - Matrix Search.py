# Thought process:
# - We can iterate one item at a time, per sublist, and one sublist at a time, but it isn´t performant
# - The lists are sorted though, therefore if the last number of a sublist is samller than the integer,
# we can skip the whole sublist.
# - This can be done till we find a list whose last number is greater than the integer
# - In this case we iterate through that list from the end to the beginning till we find it, or we break out
# of the loop if it isn´t there and we go out of the list bounds
# - Thus we need 2 pointers, one pointing to a list, this one starts at 0 and gets incremented by 1, 
# and another one which starts at the last element in a sublist, at n - 1, and gets decremented by 1, to move it backwards

def sorted_matrix_search(matrix, integer):
    n = len(matrix[0])
    i, j = 0, n - 1
    
    # Loop over the matrix, breaking out when you exhaust it but can´t find the integer
    while(i < n and j >= 0):

        # Integer is found, return index as a tuple
        if matrix[i][j] == integer:
            return (i, j)
            
        # If the last number of the sublist is smaller than integer, skip to next sublist
        if matrix[i][j] < integer:
            i += 1

        # Else, try iterate backwards through the sublist to find it
        else:
            j -= 1
    
    # Fail to find integer in the matrix
    return False
