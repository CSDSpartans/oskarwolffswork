# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean
      True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def getGuessedWord(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    output = ''
    for letter in secret_word:
        if letter in letters_guessed:
            output += letter
        else:
            output += '_ '
    return output


def getAvailableLetters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    available = [letter for letter in alphabet if letter not in letters_guessed]
    return ''.join(available)


def gameWon(letters_guessed, secret_word):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def gameLost(mistakes_made):
    if mistakes_made == 8:
        return True
    else:
        return False


def gameOver(letters_guessed, secret_word, mistakes_made):
    if gameWon(letters_guessed, secret_word) or gameLost(mistakes_made):
        return True
    else:
        return False


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = ''
    mistakes_made = 0
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('-------------')

    while not gameOver(letters_guessed, secret_word, mistakes_made):
        print('You have', 8 - mistakes_made, 'guesses left.')
        print('Available letters: ', getAvailableLetters(letters_guessed))
        choice = input('Please guess a letter: ').lower()
        if choice not in getAvailableLetters(letters_guessed):
            print("Oops! You've already guessed that letter:", getGuessedWord(secret_word, letters_guessed))
        else:
            letters_guessed += choice
            if choice in secret_word:
                print('Good guess:', getGuessedWord(secret_word, letters_guessed))
            else:
                print('Oops! That letter is not in my word:', getGuessedWord(secret_word, letters_guessed))
                mistakes_made += 1

        print('-------------')

    if gameWon(letters_guessed, secret_word):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secret_word while you're testing)

secret_word = chooseWord(wordlist).lower()
hangman(secret_word)
