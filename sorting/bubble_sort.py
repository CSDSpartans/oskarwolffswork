# bubble sort

unsorted_list = [4, 2, 5, 2, 6, 3, 5, 7, 1]


def bubble_sort(l):
    L = l[:]  # because I don't want to mutate the original
    sorted = False
    while not sorted:
        sorted = True
        for index in range(len(L) - 1):
            if L[index] > L[index + 1]:
                sorted = False
                L[index], L[index + 1] = L[index + 1], L[index]
    return L

# the complexity of this algorithm is O(n**2) if n is the length of the list


print(bubble_sort(unsorted_list))
