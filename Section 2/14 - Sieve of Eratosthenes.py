def sieve_of_eratosthenes(n):
    #  this function must return a list of prime numbers that are below or equal to an input integer n.
    
    if n == 0 or n == 1:
        sieve = []
        return sieve
        
    sieve = [False, False]
    for i in range(2, n+1):
        sieve.append(True)
        
    for j in range(2, n+1):
        if sieve[j] == True:
            for k in range(2*j, n+1, j):
                sieve[k] = False
                
    primes = []
    for m in range(2, n+1):
        if sieve[m] == True:
            primes.append(m)
        
    return primes
    pass