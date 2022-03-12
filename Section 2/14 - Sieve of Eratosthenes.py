# Thought process:
# - Create case for n in {0, 1} and return an empty list
# - For other cases, create a sieve of length n with values set to True but first 2 indices
# - Iterate over numbers, if it's a prime, change every multiple to False
# - After this is done for all numbers, only prime numbers are left set to True, they have no divisors
# - Append the prime numbers into a list and return it

def sieve_of_eratosthenes(n):

    # There are no prime numbers that are equal to 1 or 0
    if n in {0, 1}:
        return []
        
    # Create the sieve filling 0 and 1 indices as False and the rest up to n as True
    sieve = [False, False]
    for i in range(2, n + 1):
        sieve.append(True)

    # Iterate over indices of sieve
    for i in range:

        # If i is index of prime
        if sieve[i] == True:
            
            # Change all multiples of i to False, starting with 2i
            for j in range(2 * i, (n + 1 // 2) + 1, i):
                sieve[j] = False

    # Create a new list to hold and append prime values into
    primes = []

    # If a number returns true when used as an index in the sieve, then it's prime
    for number in range(2, (n + 1 // 2) + 1):
        if sieve[number] == True:
            primes.append(number)
        
    return primes
    pass