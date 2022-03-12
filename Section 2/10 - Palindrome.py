# Thought process:
# - A palindrome string is equal to its reverse, thus all characters from
# the right of the midpoint charachter have a mirror element in the left
# - If the whole string is a palindrome then the whole string is the maximum sub palindrome
# else, try to find palindrome whose length is 1 character smaller.
# Try this repeatedly till you find one or it becomes 1 character, which is a palindrome by default
# e.g. stabba, try for stabba, then stabb, tabba, then stab, tabb, abba => palindrome found!

def palindrome(string):
    
    # Iterate up to the midpoint of the string
    n = len(string)
    for char in range(n // 2):

        # If any character does not have an equal opposite index charachter, return False
        if string[char] != string[-1 - char]:
            return False

    # If every character has a mirror image, then return True
    return True

def max_sub_palindrome(string):

    # Iterate over different lengths of substrings
    strlen = len(string)
    for i in range(strlen):

        # Iterate over all substrings of length strlen - i, meaning it starts with whole string for i == 0
        for j in range(1 + i):
            substring = string[j : strlen - i + j]
            if palindrome(substring):
                return substring