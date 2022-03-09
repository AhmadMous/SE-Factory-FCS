def odd_sum(n):
    counter = 1
    sum = 0
    while (n>=counter):
        sum += counter
        counter += 2
    return sum