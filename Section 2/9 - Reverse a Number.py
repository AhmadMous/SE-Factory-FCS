def reverse_digits(n):
    if ((n%10)==n):
        return n
    else:
        return (n%10)*10**((len(str(n)))-1) + reverse_digits(n//10)