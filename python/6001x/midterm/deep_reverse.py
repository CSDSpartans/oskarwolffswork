def deep_reverse(a):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    L.reverse()
    for sublist in L:
        sublist.reverse()


b = [[0, 1, 2], [1, 2, 3]]

deep_reverse(b)
print(L)
