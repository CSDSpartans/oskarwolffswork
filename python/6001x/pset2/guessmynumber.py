#!/usr/bin/env python3
'''
this is that number guessing game where you choose a number from 0 to 100 and
say if the guess is higher or lower

I have to worry about input handling :(
'''


def get_user_input(guess):
    print('Is your secret number ' + str(guess) + '?')
    user_input = ''
    while user_input not in ['c', 'h', 'l']:
        user_input = input("Enter 'h' if the guess is too high. Enter 'l' if \
the guess is too low. Enter 'c' if I guessed correctly. ")
    return user_input


correctly_guessed = False
high = 100
low = 0

while correctly_guessed is False:
    guess = int((high + low) / 2)

    user_input = get_user_input(guess)

    if user_input == 'c':
        correctly_guessed = True
        print('Game over, your secret number was ' + str(guess))
    elif user_input == 'h':
        high = guess
    elif user_input == 'l':
        low = guess
