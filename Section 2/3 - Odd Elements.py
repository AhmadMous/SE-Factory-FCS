# Implement a  function that takes a positive number n as parameters,
# and returns the sum of odd integers less than or equal to n.

# Thought process:
# - Initiate a variable to hold a value of odd number as we iterate over them
# - Initiate a variable to hold value of sum of odd numbers we passed so far
# - Iterate up to n, adding 2 to the odd number each time, finally return the sum

# Note: this could be done with a for loop like option 2

def odd_sum(n):
    counter = 1
    sum = 0
    # option 1:
    while (n >= counter):
        sum += counter
        counter += 2

    # option 2:
    # for number in range(1, n+1, 2):
        # sum += number
    return sum