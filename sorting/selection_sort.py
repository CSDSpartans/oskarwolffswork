# selection sort algorithms
# note: there is a copy of this file in the 6001x/pset6 folder

# I'm too lazy to explain how this sort works, so just read the code

unsorted_list = [4, 2, 5, 2, 6, 3, 5, 7, 1]


# recursive version
def selection_recur(l):
    L = l[:]
    # swap items to make the first item in the list the least item
    for index in range(1, len(L)):
        if L[index] < L[0]:
            L[0], L[index] = L[index], L[0]

    # if the list only has 2 items, then it's sorted, so return it
    if len(L) == 2:
        return L
    # otherwise, simplify the problem by calling the function without the first item
    else:
        return [L[0]] + selection_recur(L[1:])

# the complexity of this algorithm is O(n**2) if n is the length of the list


print(selection_recur(unsorted_list))


# non-recursive version
def selection(l):
    L = l[:]  # because I don't want to mutate the original list
    suffix = 0  # this marks the part that has already been sorted

    while suffix != len(L):  # while the whole list hasn't been sorted
        # swap items to make the first item the least item
        for item in range(suffix, len(L)):
            if L[item] < L[suffix]:
                L[item], L[suffix] = L[suffix], L[item]
        suffix += 1  # next time through, ignore the now sorted item

    return L

# the complexity of this algorithm is O(n**2) if n is the length of the list


print(selection(unsorted_list))


# yay, they both work!
# They also both have the same complexity, so it's down to whichever is more
# readable.

# They actually both follow the same principle, simplifying the problem by
# making the unsorted part of the list shorter and shorter

# I think I prefer the recursive version, but it could be confusing to someone
# who doesn't quite get recursion (it's a pretty hard concept to grasp at first)
