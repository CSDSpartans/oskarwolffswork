'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order.

For example, if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.

For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

s = 'azcbobobegghakl'


def is_alphabetical(string):
    if ''.join(sorted(string)) == string:
        return True
    else:
        return False


best_segment = 'z'

for index in range(len(s)):
    count = 0
    segment = ''
    while is_alphabetical(segment):
        try:
            segment += s[index + count]
        except:
            pass
        count += 1

        if count > len(s):
            break

    if not is_alphabetical(segment):
        segment = segment[:-1]

    if len(segment) > len(best_segment):
        best_segment = segment

print('Longest substring in alphabetical order is: ' + best_segment)
