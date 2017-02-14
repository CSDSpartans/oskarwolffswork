def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    shared = []
    exclusive_1 = []
    exclusive_2 = []

    for key in d1.keys():
        if key in d2.keys():
            shared.append(key)

    for key in d1.keys():
        if key not in shared:
            exclusive_1.append(key)

    for key in d2.keys():
        if key not in shared:
            exclusive_2.append(key)

    intersect = {}
    for key in shared:
        intersect[key] = f(d1[key], d2[key])

    difference = {}
    for key in exclusive_1:
        difference[key] = d1[key]
    for key in exclusive_2:
        difference[key] = d2[key]

    return (intersect, difference)

def f(a, b):
    return a + b



d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}


print(dict_interdiff(d1, d2))
