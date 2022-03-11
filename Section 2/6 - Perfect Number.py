# Thought process:
# - If b divides a, then a % b == 0
# - All divisors of a are equal to or less than k = (a // 2) + 1
# - Loop over numbers less than a adding their value to a sum
# - If sum == number then it is perfect, return True, else return False

def perfect(number):
   # Declare a variable sum and initialize it to zero
    sum = 0

    for divisor in range(1, ((number // 2) + 1)):
        if number % divisor == 0:
            sum += divisor
 
    return sum == number
