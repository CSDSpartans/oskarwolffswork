'''
Numbers in Mandarin follow 3 simple rules.

There are words for each of the digits from 0 to 10.
For numbers 11-19, the number is pronounced as "ten digit", so for example, 16
would be pronounced (using Mandarin) as "ten six".

For numbers between 20 and 99, the number is pronounced as "digit ten digit",
so for example, 37 would be pronounced (using Mandarin) as "three ten seven". If
the digit is a zero, it is not included.
'''
trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''

    if len(us_num) == 1:
        return trans[us_num]
    elif us_num == '10':
        return 'shi'
    elif us_num[1] == '0':
        return trans[us_num[0]] + ' ' + trans['10']
    elif us_num[0] == '1':
        return trans['10'] + ' ' + trans[us_num[1]]
    else:
        return trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[1]]


# tests
print(convert_to_mandarin('36'), 'san shi liu')
print(convert_to_mandarin('20'), 'er shi')
print(convert_to_mandarin('16'), 'shi liu')
