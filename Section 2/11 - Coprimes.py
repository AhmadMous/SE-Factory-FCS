def coprime(a, b):
    # Returns a boolean value
    # Returns true if a and b are in fact coprime
    a_divisors = set()
    b_divisors = set()

    for i in range (1, a // 2 + 1):
        if a % i == 0:
            a_divisors.add(i)
            
    for j in range (1, b // 2 + 1):
        if b % j == 0:
            b_divisors.add(j)
            
    print(a_divisors.intersection(b_divisors))
            
def count_coprimes(n):
    