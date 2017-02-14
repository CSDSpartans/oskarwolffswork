def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA

    returns the sum of the products of each pair
    '''
    listC = [a * b for a, b in zip(listA, listB)]
    return sum(listC)



listA = [1, 2, 3]
listB = [4, 5, 6]

print(dotProduct(listA, listB))  # this should be 32
