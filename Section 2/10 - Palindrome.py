def palindrome(input_str):
    n = len(input_str)
    if n == 1:
        return True
    for ch in range((n+1)//2):
        if input_str[ch] != input_str[-1-ch]:
            return False
    return True

def max_sub_palindrome(input_str):
    strlen = len(input_str)
    if strlen == 1:
        return input_str[0]
        
    elif palindrome(input_str):
        return input_str

    else:
        for i in range(0, strlen):
            if len(input_str[:strlen-1-i]) == 1:
                return input_str[:strlen-1-i]
            else:
                for j in range(1+i):
                    if palindrome(input_str[j:strlen -i+j]):
                        return input_str[j:strlen-i+j]