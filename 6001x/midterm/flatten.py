# a quick note:
# functions really shouldn't be defined inside of other functions
# I only did this because I needed to submit my code in a single function

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    def is_flat(object):
        if type(object) is not list:
            return True

        for item in aList:
            if type(item) is list:
                return False

        return True

    def single_flatten(alist):
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

    if is_flat(aList):
        return aList
    else:
        return flatten(single_flatten(aList))






print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

print(flatten([1, 2]))
