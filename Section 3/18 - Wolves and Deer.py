# Thought process:
# - We will need to keep track of wolves, deer for every year n - 1 to be able to calculate them
# for year n, thus we will use lists to hold their numbers, where we index by year starting at 0
# - We need to hold greatest number of wolves in a variable
# - We increment one year at a time, updating "greatest" variable as necessary

def wolves_and_dear(deer_0, wolves_0, deer_growth, deer_predation, wolves_predation, wolves_decay, dt, n):

    # Track number of wolves, deer. Indexed by year starting with year = 0
    wolves = [wolves_0]
    deer = [deer_0]

    # Holds highest number of wolves found at one time, starts at value of first year
    greatest = wolves[0]
    
    # Iterate over years from 0 up to and including n to find greatest number of wolves ever present
    for i in range(1, n):

        # Find number of wolves and deer for year i
        wolvestemp = wolves[i - 1] + dt * (wolves_predation * wolves[i - 1] * deer[i - 1] - wolves_decay * wolves[i - 1])
        deertemp = deer[i - 1] + dt * (deer_growth * deer[i - 1] - deer_predation * deer[i - 1] * wolves[i - 1])

        # Append number of wolves and deer to the respective lists (automatically at index i)
        wolves.append(wolvestemp)
        deer.append(deertemp)

        # If number of wolves for this year is greater than old greatest, we have a new greatest
        if wolvestemp > greatest:
            greatest = wolvestemp
            
    return greatest
    pass