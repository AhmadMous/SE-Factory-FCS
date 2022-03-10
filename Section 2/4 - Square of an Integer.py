# Square a number by successive additions.
# You are given as input the integer n, which you can assume is not negative.
# That is, n >= 0
# Use successive additions to return the sum in the following format (n+n+n..+n) n-times
# This function will return a string, instead of outputting to the terminal.

# Thought process:
# - The output should be in the form of '4 + 4 + 4 + 4 = 16'
# - and it should work for 0, as in '0 = 0'
# - Thus we start with string value of input number not 0
# - And we loop adding " + " + input_string each time for 1 time less than input number
# - Finally, we add ' = ' + string value of the total to the resultant string

def sum(input_number):

    # Create bindings for total, result_string, and input_string
    input_string = str(input_number)
    total = input_number * input_number
    result_string = input_string

    # Add the input string to the resultant string input_number - 1 times
    for number in range(input_number - 1):
        result_string += ' + '
        result_string += input_string

    # Add ' = ' + string value of the total to the resultant string
    result_string += ' = ' + str(total)

    return result_string