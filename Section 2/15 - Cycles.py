# Thought process:
# - You want to keep track of indices you visit, a list or dict can be used, but we will use a set for convenience
# - Every element is part of a cycle, and we can indefinetly set index = indices[index],
# this allows us to use a while loop safely and break when the index returns to our selected index
# - We can use this while loop for all but previously visited indices, so we iterate over all but,
# indices we have visited before, which we keep track of in a set 

def cycles(indices):

    # Create a set for visited indices, and a list to hold lists of cycles
    visited = set()
    cycles = []

    # Iterate over indices of given list
    for start_ind in indices:

        # Skip indices that are already visited
        if start_ind in visited:
            continue

        # Create a path starting with start index and ending with index it leads to
        path = [start_ind]
        next_ind = indices[start_ind]

        # "Grow" that path till next_index becomes equal to start_index
        while start_ind != next_ind:
            path.append(next_ind)
            next_ind = indices[next_ind]
        
        # Then close that cycle path, and append it to cycles list
        else:
            cycles.append(path)

            # This is where set helps, if a number is a cycle with itself, it only adds that index once
            visited |= set(path)
    return cycles