# Thought process:
# - Sum from 1 to n is equal to n + sum from 1 to n - 1
# - A base case is when n == 0, where it automatically returns n
# - The recursive loop ends when n is equal to 0

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)