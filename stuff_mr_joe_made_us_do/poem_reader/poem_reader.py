#!/usr/bin/env python3

# this program should read the poem, numbering each line
# challenge: count each stanza in the poem

poem_file = "poem.txt"

try:
    file = open(poem_file, 'r').readlines()
except IOError:
    raise "Error: File does not appear to exist."
    quit()

file = file[4:]
line_count = 1
stanza_count = 2

print('stanza 1\n')

for line in file:
    if line == '\n':
        print('\nstanza', stanza_count, '\n')
        stanza_count += 1
    else:
        print(line_count, line, end='')
        line_count += 1
