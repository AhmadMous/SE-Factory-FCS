def count_digits(n):
    if n == 0:
        return 0
    elif (n//10) == 0:
        return 1
    else:
        return 1 + count_digits(n//10)