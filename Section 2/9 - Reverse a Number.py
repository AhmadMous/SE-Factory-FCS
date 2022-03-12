# Thought process:
# - Reversing a number means first digit becomes last, 2nd digit becomes second to last, and so on
# - We thus need to be able to now digit count of a number, we need a function for that
# - We find reverse number by building a new number of exact same number of digits and start building that from left to right
# - e.g. 954 => 400 + reverse of 95 => 459
# - Thus we multiply 4 for example by 10 ** (number of digits - 1) to get 400 from 954, and so on

def reverse_digits(n):

    # Using count digits from last excercise, note: Iterative is faster
    def count_digits(n):
        if n == 0:
            return 0
        else:
            return 1 + count_digits(n // 10)

    # Base case: if n is 1 digit, return n
    if ((n % 10) == n):
        return n

    # Getting left most digit with 0s to its right, then adding reverse of what's left after division by 10
    else:
        left_digit = (n % 10) * 10 **(count_digits(n) - 1)
        return left_digit + reverse_digits(n // 10)