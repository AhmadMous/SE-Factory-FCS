# Returns a list of the lowest k integers in the l
# for example lowest([1,2,3, -1,-2,-3], 2) returns [-3, -2]
# hint: use queue

from collections import deque
def lowest(l, k):
    list_min = list_max = l[0]
	for elements in l:

