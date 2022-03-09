def perfect(number):
    #The variable "value" represent the value of the integer number entered by the user
    #Decalre a bool variable isperfect and initialize it to false
    is_perfect = False
   # Declare a variable sum and initialize it to zero
    sum = 0
    #1- Check if "number" is non-positive.
    if number < 0 :
        positive = False
    else:
        positive = True
    #2- If not, find the proper divisors of "number" and find their sum
    outstr = ''
    sum = 0
    if positive == True:
        for i in range(1, ((number//2)+1)):
            if number%i == 0:
                outstr += ' + ' + str(i)
                sum += i
   #-3- Check if their sum is equal to "number"  
    if sum == number:
        is_perfect = True
    return is_perfect
