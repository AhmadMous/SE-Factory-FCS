# Thought process:
# - highest integer whose cube is equal or under n is the integer 1 less than that
# whose cube is above n
# - Thus we can loop over numbers under n, breaking out of the loop when
# the cube of the number is equal or above n
# - We also needs bindings to hold string values of some calculations, and
# whether the root is exact or there is a difference

def cubic_root(n):
	# Handles cases for n in {0, 1}, exact is state of cubic root with respect to n
	exact = True
	greatest_root = n

	# Iterate over numbers less than n for cases where n > 1, break out of loop when root is found
	if n > 1:
		for i in range(n):

			# If i to the power 3 is higher than 1, greatest root is 1 less than that, change exact to False
			if i * i * i > n:
				greatest_root = i - 1
				exact = False
				break

			elif i * i * i ==  n:
				greatest_root = i
				break
	
	# Create bindings for string values of root and difference
	root_string = str(greatest_root)
	difference_string = str(n - greatest_root * greatest_root * greatest_root)

	# Create the string which will be returned, according
	if exact:
		resultant_string = root_string + ", exact!"
	else:
		resultant_string = root_string + ", not exact with difference " + difference_string

	print(resultant_string)