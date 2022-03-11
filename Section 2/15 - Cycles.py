def cycles(indices):
    visited = set()
    cycles = []

    for start_ind in indices:

        if start_ind in visited:
            continue

        path = [start_ind]
        next_ind = indices[start_ind]

        while start_ind != next_ind:
            path.append(next_ind)
            next_ind = indices[next_ind]
        else:
            cycles.append(path)
            visited |= set(path)
    return cycles