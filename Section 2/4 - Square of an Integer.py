def sum(user_input):
    sumsqr = user_input*user_input
    total = 0
    inputstr = str(user_input)
    sumstr = ''
    if user_input == 0:
        sumstr = str(0)
    else: 
        for i in range(user_input):
            total += user_input
            sumstr += inputstr
            if total < sumsqr:
                sumstr += ' + '
    sumstr += ' = ' + str(total)
    return sumstr
        