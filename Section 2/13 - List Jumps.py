# Thought process:
# - We want to repeatedly jump between indices for an unknown amount of times,
# thus we need a while loop to do so
# - We want to keep track of visited indices, this can be done by using a set, dictionary, or list
# - We return, breaking out of the loop, when we go out of bounds, or when we reach a previously visited index
# - Note: negative indexing is not allowed in this excercise, meaning 0 and list's length - 1 are the bounds of indices


def list_jumps(jumps):

    # Holds value of current index, starts at 0
    index = 0

    # Holds the length of the list
    length = len(jumps)

    # Keeps track of visited indices
    visited = []
    
    # Jump between indices, till you reach a previously visited index, or go out of bounds
    while True:
        if index >= length or index < 0:
            return 'out-of-bounds'

        if index in visited:
            return 'cycle'
            
        else:
            visited.append(index)
            index += jumps[index]