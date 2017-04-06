# bogo sort

# aka: stupid sort, random sort, monkey sort, shotgun sort, etc.

import random

unsorted_list = [4, 2, 5, 2, 6, 3, 5, 7, 1]


def bogo_sort(l):
    L = l[:]  # because I don't want to mutate the list
    sorted = False
    while not sorted:
        random.shuffle(L)  # this is why it's called 'stupid sort'

        # basically just test if the list is sorted
        for index in range(1, len(L)):
            if L[index] < L[index - 1]:
                sorted = False
                break
            sorted = True

    return L


# the complexity of this algorithm is O(?)

# (this means that it's unbounded, or that the algorithm may
# never actually finish sorting)


print(bogo_sort(unsorted_list))
