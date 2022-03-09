# Implement a function that takes two integers as a
# parameter and returns a string with the sum of the two numbers.
# Example: for a=2 and b=3
# Expected output: 2+3=5

# Thought process:
# - Add the two numbers to get the sum
# - Cast the 2 input numbers and the sum into strings
# - Concatanate the casted strings into required format and return the resultant string

def calculate_sum(a, b):
    sum = a + b
    return str(a) + "+" + str(b) + "=" + str(sum)