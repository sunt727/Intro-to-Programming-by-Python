# Problem Set 2, hangman.py
# Name: Tuo Sun
# Collaborators: None
# Time spent: 3

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    new_word = list(secret_word)
    for i in new_word:
        if i in letters_guessed:
            for x in [new_word.index(i)]:
                new_word[x] = ''

    return True if ''.join(new_word) == '' else False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters and underscores (_) that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_word = list(secret_word)
    for i in new_word:
        if i not in letters_guessed:
            for x in [new_word.index(i)]:
                new_word[x] = '_'

    return ''.join(new_word)




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which 
      letters have not yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(alphabet)):
        if alphabet[i] in letters_guessed:
            alphabet[i] = ''

    return ''.join(alphabet)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 10 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guesses_remaining = 10
    letters_guessed = []
    score = 0

    print('Welcome to Hangman! \nI am thinking of a word that is %d letters long.' % (len(secret_word)))

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        if guesses_remaining <= 1:
            print('------ \nYou have %d guess left. \nAvailable letters: %s' \
                  % (guesses_remaining, get_available_letters(letters_guessed)))
        else:
            print('------ \nYou have %d guesses left. \nAvailable letters: %s' \
              % (guesses_remaining, get_available_letters(letters_guessed)))

        guess = input('Please guess a letter: ').lower()
        print("Please guess a letter: " + guess)


        if guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Oops! That is not a valid letter: %s' % (get_guessed_word(secret_word, letters_guessed)))
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter: %s" % (get_guessed_word(secret_word, letters_guessed)))
        elif guess in secret_word:
            letters_guessed.append(guess)
            secret_word.replace(guess, '_')
            print("Good guess: %s" % (get_guessed_word(secret_word, letters_guessed)))
        elif guess in 'aeiou':
            guesses_remaining -= 2
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word: %s" % (get_guessed_word(secret_word, letters_guessed)))
        elif guess in 'bcdfghjklmnpqrstuvwxyz':
            guesses_remaining -= 1
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word: %s" % (get_guessed_word(secret_word, letters_guessed)))
        else:
            pass


    if is_word_guessed(secret_word, letters_guessed):
        score += len(set(secret_word)) * len(secret_word) + guesses_remaining
        print('------ \nCongratulations, you won!\nYour total score for this game is: %d' % (score))
    if guesses_remaining < 1:
        print("------ \nSorry, you ran out of guesses. The word was %s" % secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def hangman_with_help(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 10 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol #, you should reveal to the user one of the 
      letters missing from the word at the cost of 2 guesses. If the user does 
      not have 2 guesses remaining, print a warning message. Otherwise, add 
      this letter to their guessed word and continue playing normally.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guesses_remaining = 10
    letters_guessed = []
    score = len(set(secret_word)) * len(secret_word)

    def helper():

        set_word = set(secret_word)
        letters_left = list(get_available_letters(letters_guessed))

        choose_from = []

        for i in set_word:
            if i in letters_left:
                choose_from.append(i)

        new = random.randint(0, len(choose_from) - 1)
        exposed_letter = choose_from[new]
        letters_guessed.append(exposed_letter)



    print('Welcome to Hangman with help! \nI am thinking of a word that is %d letters long.' % (len(secret_word)))

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        if guesses_remaining <= 1:
            print('------ \nYou have %d guess left. \nAvailable letters: %s' \
                  % (guesses_remaining, get_available_letters(letters_guessed)))
        else:
            print('------ \nYou have %d guesses left. \nAvailable letters: %s' \
              % (guesses_remaining, get_available_letters(letters_guessed)))

        guess = input('Please guess a letter: ').lower()
        print("Please guess a letter: " + guess)

        if not str.isalpha(guess):
            if guesses_remaining < 2:
                print('Oops! Not enough guesses left: %s' % (get_guessed_word(secret_word, letters_guessed)))
            else:
                guesses_remaining -= 2
                helper()
                print('Letter revealed: %s' % (get_guessed_word(secret_word, letters_guessed)))
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter: %s" % (get_guessed_word(secret_word, letters_guessed)))
        elif guess in secret_word:
            letters_guessed.append(guess)
            secret_word.replace(guess, '_')
            print("Good guess: %s" % (get_guessed_word(secret_word, letters_guessed)))
        elif guess in 'aeiou':
            guesses_remaining -= 2
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word: %s" % (get_guessed_word(secret_word, letters_guessed)))
        elif guess in 'bcdfghjklmnpqrstuvwxyz':
            guesses_remaining -= 1
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word: %s" % (get_guessed_word(secret_word, letters_guessed)))
        else:
            pass
        
    if guesses_remaining < 1:
        print("------ \nSorry, you ran out of guesses. The word was %d" % secret_word)
    if is_word_guessed(secret_word, letters_guessed):
        print('------ \nCongratulations, you won!\nYour total score for this game is: %s' % (score + guesses_remaining))



# When you've completed your hangman_with_help function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass
    #secret_word = 'hi'
    # letters_guessed = ['a', 'p', 'm', 'l', 'e']
    #
    # print(get_guessed_word(secret_word, letters_guessed))
    # print(get_available_letters(letters_guessed))
    # print(is_word_guessed(secret_word, letters_guessed))

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_help(secret_word)
