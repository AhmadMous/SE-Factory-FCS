# Thought process:
# - We can find if two numbers are coprimes by iterating up to the smaller of the two,
# till we make sure there are no common divisors of both but 1, however doing this will result
# in a message saying the code took too long to compute when attempting to count coprimes
# - An alternate way of find if 2 numbers are coprimes is by attempting to find the GCD, if it is
# equal to 1, then they are coprimes. A fast way of finding GCD is by using Euclid's algorithm which
# is taught in discrete mathematics. It is also mentioned in "Grokking Algorithms" book
# - You can read about Euclid's algorithm here : https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm


def coprime(a, b):

    # Find which of the two is higher and which is smaller
    lowest = a if a < b else b
    highest = a if a >= b else b

    # Euclid's algorithm for GCD
    def GCD(larger, smaller):
        if smaller == 0:
            return larger
        else:
            return GCD(smaller, larger % smaller)
        
    # IF GCD == 1, coprimes
    if GCD(highest, lowest) == 1:
        return True
    else:
        return False
    
            
def count_coprimes(n):

    # Variable to hold numbers of coprimes found, which will be returned by the function
    coprimes = 0

    # Iterate over numbers up to n + 1 to find all coprimes for k starting from 1 and up to n inclusive
    for number in range(1, n + 1):
        if coprime(n, number):
            coprimes += 1
            
    return coprimes