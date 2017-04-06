# merge sort

unsorted_list = [4, 2, 5, 2, 6, 3, 5, 7, 1]


# this is a helper function for merge_sort.  it merges two lists
def merge(l1, l2):
    L1, L2 = l1[:], l2[:]  # I don't want to mutate the lists
    result = []
    while len(L1) > 0 and len(L2) > 0:
        if L1[0] < L2[0]:
            result.append(L1.pop(0))
        else:
            result.append(L2.pop(0))
    if len(L1) > 0:
        result += L1
    elif len(L2) > 0:
        result += L2
    return result

# the complexity of this function is O(n)


def merge_sort(l):
    L = l[:]  # because I don't want to mutate the original
    if len(L) < 2:  # base case:
        return(L[:])
    else:
        middle = len(l) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

# the complexity of this algorithm is O(n log(n)) if n is the length of the list

# that's because merge_sort() itself is O(log(n)), and calls merge(), which is O(n)


print(merge_sort(unsorted_list))
