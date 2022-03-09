def list_jumps(jumps):
    length = len(jumps)
    for index in range(length):
        destination = index + jumps[index]
        if destination > length:
            print('out-of-bounds')
    print('cycle')