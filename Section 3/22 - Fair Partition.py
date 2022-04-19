# Thought process:
# - Best possibility (target) is when each list to have sum equal to sum(ratings)/2
# - Greedy pairution: sort the list and iterate over the sorted list from 
# the biggest to smallest numbers, adding the number to the team with lesser ratings, this failed the tests
# - Alternative option: Slower but better, recursive DFS to find best combinations
# - Utilized option: Generate all possible combinations where the 2 lists compliment each other
# - Each item is either in combo1 or isn't, therefore we have 2**N possibilities
# - We can cover every combination by using bits to indicate if item of that bit's index is included or not
# - It is enough to measure difference between sum of one list and target to find best option

def partition(ratings):
    # ratings: a list of integers
    """
    This function must return a tuple of 2 lists.
    The 2 lists are your partition of ratings, the goal is to minimize the difference between the teams' cumulative rating
    """
    # Helper generator that generates the power set, pair by pair
    def powerSet(items):

        # enumerate the 2**N possible combinations
        N = len(items)
        for i in range(2 ** N):

            # List to hold combinations, items are split between the 2 lists
            pair = ([], [])

            # Iterate over the items of the input list, appending to appropriate list of the tuple
            for j, item in enumerate(items):
                pair[(i >> j) & 1].append(item)

            yield pair

    target = sum(ratings)/2
    smallest = (0, 0)
    best_difference = target

    # Generate pairs one by one
    for value in powerSet(ratings):

        # Finding difference between sum of list values of pair, and target number
        difference = abs(target - sum(value[0]))

        # Pair is a perfect match, return it
        if difference == 0:
            return value

        # Keep track of pair who is closest to target rating per team
        if best_difference > difference:
            best_difference = difference
            smallest = value

    return smallest