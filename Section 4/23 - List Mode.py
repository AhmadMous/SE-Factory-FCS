# Thought process:
# - Create a dictionary with keys as numbers from list, with value being frequency

def mode(l):
    maxval = 0
    maxkey = 0
    freq = {}
    
    # Loop over list items counting occurences
    for element in l:
        if element in freq:
            freq[element] += 1
        else:
	        freq[element] = 1

    # Loop over items in dictionary and keep track of highest val, and associated key
    for element in freq:
        if freq[element] > maxval:
            maxval = freq[element]
            maxkey = element
            
    return maxkey