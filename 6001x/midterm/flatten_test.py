def flatten(alist):
    '''
    return a flattened version (one level only) of list
    '''

    new_list = []

    for item in alist:
        if type(item) is list:
            for element in item:
                new_list.append(element)
        else:
            new_list.append(item)

    return new_list

print(flatten([1, 2]))

print(type([3, 4]) is list)
