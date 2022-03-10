# Write a function that takes two positive numbers as parameters and returns True
# if the second number is the square root of the first number and False otherwise.

# Thought process:
# - Multiply the second number by itself to get a product
# - If the product equals the other number, then second number is a square root of the first number

def is_square_root(x, y):
    if (y * y) == x:
        return True
    else:
        return False
        