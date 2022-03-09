def cubic_root(n):
	# n is a positive integer
	# Write your answer here
	##pass
	exact = True
	if n == 1 or n == 0:
	    greatest = n
	    print
	else:
	    for i in range(n):
	        if i*i*i > n:
	            greatest = i - 1 
	            exact = False
	            break
	        elif i*i*i ==  n:
	            greatest = i
	            break
	grtstr = str(greatest)
	if exact:
	   outstr = grtstr + ", exact!"
	   print(outstr)
	else:
	   outstr = grtstr + ", not exact with difference " + str(n - greatest*greatest*greatest)
	   print(outstr)
	    
