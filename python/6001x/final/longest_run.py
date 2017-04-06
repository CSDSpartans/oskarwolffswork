def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # hooray for bad code!
    # it somehow works, but I'm really not proud of what I've done here

    # find longest increasing run
    longest_increasing = []
    current_run = [L[0]]
    inc_start_index = 0
    start_index = 0

    for index in range(1, len(L)):
        if L[index] >= L[index - 1]:
            current_run.append(L[index])
        else:
            if len(current_run) > len(longest_increasing):
                longest_increasing = current_run[:]
                inc_start_index = start_index
                start_index = index
            current_run = [L[index]]
    if len(current_run) > len(longest_increasing):
        longest_increasing = current_run[:]
        inc_start_index = start_index

    # find longest decreasing run
    longest_decreasing = []
    current_run = [L[0]]
    dec_start_index = 0
    start_index = 0

    for index in range(1, len(L)):
        if L[index] <= L[index - 1]:
            current_run.append(L[index])
        else:
            if len(current_run) > len(longest_decreasing):
                longest_decreasing = current_run[:]
                dec_start_index = start_index
                start_index = index
            current_run = [L[index]]
    if len(current_run) > len(longest_decreasing):
        longest_decreasing = current_run[:]
        dec_start_index = start_index

    # figure out which one to use
    if len(longest_increasing) > len(longest_decreasing):
        return sum(longest_increasing)
    elif len(longest_decreasing) > len(longest_increasing):
        return sum(longest_decreasing)
    else:
        if inc_start_index < dec_start_index:
            return sum(longest_increasing), inc_start_index, 'inc', dec_start_index
        else:
            return sum(longest_decreasing), dec_start_index, 'dec', inc_start_index


print(longest_run([1, 2, 3, 2, -1]))
