    doing this slowly will result in : your code took too long to execute


def coprime(a, b):

    lowest = a if a < b else b
    highest = a if a >= b else b

    def GCD(larger, smaller):
        if smaller == 0:
            return larger
        else:
            return GCD(smaller, larger % smaller)
        
    if GCD(highest, lowest) == 1:
        return True
    else:
        return False
    
            
def count_coprimes(n):
    coprimes = 0
    for number in range(1, n+1):
        if coprime(n, number):
            coprimes += 1
    return coprimes