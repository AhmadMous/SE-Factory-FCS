# Thought process:
# - To proof two strings "a" and "b" are permutations of each other, it is sufficient to
# proof they are the same length and all characters of a can be found in b
# Note: There are actually cases where this fails, where number of characters of both
# are the same and present in both but frequency of repetition is different
# - For permutations list, we know that output[i] = input[permutation[i]]
# - We must thus find index in input string of characters of output string and set
# value of permutation list variable to that of the input string, at index equal to that of 
# the character of output string

def is_permutation(str1, str2):

    # Different lengths => not permutations
    if len(str1) != len(str2):
        return False
        
    # Character in one string but not in the other => not permutations
    for char in str1:
        if char not in str2:
            return False
            
    # Same lengths and characters => permutations
    return True
    pass

def get_permutation_list(input_str, output_str):

    # Permutation list which we will build starting from index 0
    perm_list = []

    # We loop over output string for every character "char"
    for char in output_str:

        # Get index of that character in input string
        for i in range(len(input_str)):

            # Append its index to permutation list, make sure its not already in perm_list to avoid doubles
            if char == input_str[i] and i not in perm_list:
                perm_list.append(i)
                break
    return perm_list
    pass

