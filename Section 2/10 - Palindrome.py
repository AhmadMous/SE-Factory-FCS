def palindrome(string):
    n = len(string)
    for char in range(n // 2):
        if string[char] != string[-1 - char]:
            return False
    return True

def max_sub_palindrome(string):
    strlen = len(string)
    if palindrome(string):
        return string

    else:
        for i in range(0, strlen):
            x = string[:strlen-1-i]
            if len(x) == 1:
                return x
            else:
                for j in range(1+i):
                    y = string[j:strlen-i+j]
                    if palindrome(y):
                        return y