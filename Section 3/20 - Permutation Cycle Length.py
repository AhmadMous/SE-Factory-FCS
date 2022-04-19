# Thought process:
# - We need to apply the permutation to the list repeatedly till it matches original list
# - To permute the list, we need to loop over it, permuting one element at a time
# - But if we permute it using itself, changes will affect permutations undesirably

def permutation_cycle_length(permutation):

    # Save the original list by copying it, get length for looping over list
    originallist = permutation[:]
    n = len(permutation)

    # Counter which increments every iteration of the while loop, counting permutations
    counter = 0

    while(True):

        # Temporary list to permute "permutation" list non-destructively
        temp = permutation[:]
        for i in range(n):
            permutation[i] = temp[originallist[i]]
        counter += 1
        
        # When permutation finally equals origin list, return counter
        if permutation == originallist:
            return counter
    pass