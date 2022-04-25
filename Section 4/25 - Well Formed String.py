# Thought process:
# - It is enough to create a stack and add every opening special char to the stack
# - We can pop each special char when we encounter a matching closing char
# - If we encounter a closing char that doesn't match last opening char in stack, then it isn't well formed
# - If we iterate over all input string and all the opening chars have been popped by matching closing chars -> well formed

def well_formed(s):

    # Stack to keep track of special character
    specials_stack = []

    # Lists of special closing and opening character
    opening_chars = ['[', '{', '(']
    closing_chars = [']', '}', ')']

    # Creating dict with opening chars as keys and closing chars as values
    specials = dict()
    for i in range(3):
        specials[opening_chars[i]] = closing_chars[i]


    # Iterate over character of input string
    for char in s:

        # If it is an opening character, add it to the stack
        if char in opening_chars:
            specials_stack.append(char)

        # Closing character and matches the last item in the stack, pop it
        elif len(specials_stack) != 0 and specials[specials_stack[-1]] == char:
            specials_stack.pop()

        # Closing character that doesn't match last opening char in the stack -> not well formed
        elif char in closing_chars:
            return False
    
    # If when we are done iterating, the stack is empty -> well formed
    if specials_stack == []:
        return True
    else:
        return False


# Function to test our implementation
def test_well_formed():

    # IO paits for testing
    test_pairs = [('aaa[bbbc]ee', True), ('', True), ('{[]}}', False)]

    # Test every value
    for i in range(len(test_pairs)):
        if test_pairs[i][1] == well_formed(test_pairs[i][0]):
            print('Success for: ' + test_pairs[i][0])
        else:
            print('Failure for: ' + test_pairs[i][0] + ' expected: ' + test_pairs[i][1] + ' actual: ' + well_formed(test_pairs[i][0]))

test_well_formed()