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
secretWord = 'apple'

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if lettersGuessed == []:
        return False
    lettersWord = []
    for let in secretWord:
        if let in lettersWord:
            pass
        else:
            lettersWord.append(let)
    for let in lettersGuessed:
        if let in lettersWord:
            lettersWord.remove(let)
    if lettersWord == []:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    lettersWord = []
    word = ''
    for let in secretWord:
        if let in lettersWord:
            pass
        else:
            lettersWord.append(let)
    for let in secretWord:
        if let in lettersGuessed:
            word = word + let
        else: word = word + '_ '
    return word
            


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    remainingLetters = list(string.ascii_lowercase)
    for let in lettersGuessed:
        remainingLetters.remove(let)
    return str(''.join(remainingLetters))
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    lettersWord = []
    mistakesMade = 0
    for let in secretWord:
        if let in lettersWord:
            pass
        else:
            lettersWord.append(let)
    print('Welcome to the game, Hangman!')
    print('The secret word has ' + str(len(secretWord)) + ' letters in it.')
    #, end='')
    while isWordGuessed(secretWord, lettersGuessed) == False:
        print('-----------')
        print('You have ' + str(8-mistakesMade) +' guesses remaining.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        if guess.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            continue
        if len(guess.lower()) > 1 or len(guess.lower()) == 0:
            print('You have to guess one letter! Try again.')
            continue
        lettersGuessed.append(guess.lower())
        if guess.lower() not in secretWord:
            mistakesMade += 1
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            if mistakesMade == 8:
                print('-----------')
                print('Sorry! You lost. The secret word was ' + str(secretWord) + '.')
                break
        else:
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('-----------')
                print('Congratulations! The secret word was ' + str(secretWord) + '.')
                break
        
           
            
        






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
