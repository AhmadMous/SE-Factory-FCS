# Thought process:
# - Number of digits of n is number of digits of 1+ n // 10
# - Base case is when n == 0, that's where number of digits returns 0
# - Recursive loop ends when n == 0


def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)