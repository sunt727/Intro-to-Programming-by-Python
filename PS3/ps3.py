# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Tuo Sun
# Collaborators : None
# Time spent    : 8

import math
import random
import string
from unittest import mock
import sys

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def test_play_game(word_list, hands, replaced_letter = None):
    """
    Allows you to play a series of pre-specified hands. 
    Will allow you to play your game (i.e. your functions/code) while 
    specifying what hands you want the computer to deal, and optionally
    what letter should be "chosen" to be added in the hand
    when you call substitute_hand. This function should help you debug your
    code/any failing play_game test cases.
    
    To use this function run your ps3.py and call the function as shown
    in example usage.
    
    ----ARGUMENTS----
    word_list: list of lowercase strings of valid words
    hands: list of dictionaries of the hands you want to play in order
    ---OPTIONAL ARGUMENTS-- (if you do not wish to use these you
                              don't need to pass them in)
                              
    replaced_letter: string letter that you want substitute_hand
                     to chose as a new letter
                     
    Example usage w/o substitution:
    Suppose you want to play the game with two hands shown below.
    h1 = {'a':1, 'b':1, 'c':1, 'e':1, '@': 1}
    h2 = {'z':1, 'y':1, 'u':1, 'a':1, '@': 1}
    hands = [h1,h2]
    test_play_game(word_list, hands)

    Example usage w/ substitution:
    Suppose you want to play the game with two hands shown below and you want
    the "random" letter chosen by substitute hand to be "t".
    h1 = {'a':1, 'b':1, 'c':1, 'e':1, '@': 1}
    h2 = {'z':1, 'y':1, 'u':1, 'a':1, '@': 1}
    hands = [h1,h2]
    letter = 't'
    test_play_game(word_list, hands, letter)
    
    """
    def replace_letter_mock(hand, letter):
        """
        Replaces the chosen letter with replaced_letter
        """
        num = hand[letter]
        del hand[letter]
        hand[replaced_letter] = num
        return hand
    deal_hand_function = sys.modules[__name__].deal_hand 
    substitute_hand_function = sys.modules[__name__].substitute_hand
    sys.modules[__name__].deal_hand = mock.Mock(side_effect=hands)
    if replaced_letter:
        sys.modules[__name__].substitute_hand = mock.Mock(side_effect=replace_letter_mock)
    play_game(word_list)
    sys.modules[__name__].substitute_hand = substitute_hand_function
    sys.modules[__name__].deal_hand = deal_hand_function

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only 
    contain lowercase letters, so you will have to handle uppercase and mixed 
    case strings appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            2, or
            5*wordlen + 8*(wordlen - n), where wordlen is the length of the 
            word and n is the hand length when the word was played.

    Letters are scored as in Scrabble: A is worth 1, B is worth 3, 
    C is worth 3, D is worth 2, E is worth 1, and so on (provided in 
    SCRABBLE_LETTER_VALUES above).

    word: string
    n: int >= 0
    returns: int >= 0
    """

    wordlen, low_word, sum_points = len(word), word.lower(), 0

    for letter in low_word:
        sum_points += SCRABBLE_LETTER_VALUES.get(letter, 0)

    return sum_points * max(2, (5*wordlen + 8*(wordlen - n)))

#
# Make sure you understand how this function works and what it does!
#
#print(get_word_score('weed', 6))

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    y = random.randint(num_vowels, n-1)

    for i in range(num_vowels, n):
        if i != y:
            x = random.choice(CONSONANTS)
            hand[x] = hand.get(x, 0) + 1
        else:
            hand['@'] = 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    new_hand = hand.copy()

    for letter in word.lower():
        if int(new_hand.get(letter, 0)) > 1:
            new_hand[letter] -= 1
        elif int(new_hand.get(letter, 0)) == 1:
            del new_hand[letter]

    return new_hand

# hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# new_hand = update_hand(hand, 'quail')
# print(new_hand)
# display_hand(new_hand)
# display_hand(hand)
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand (that is, there are enough of
    each letter in the hand to construct the word). Otherwise,
    returns False.
    Does not mutate hand or word_list.

    For Problem #4, returns True if replacing the wildcard @ with
    a consonant forms a word in word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word_dict = {}
    low_word = word.lower()
    valid = False

    if '@' in low_word:
        for i in CONSONANTS:
            replace_word = low_word.replace('@', i)
            if replace_word in word_list:
                valid = True
    else:
        if low_word in word_list:
            valid = True

    if valid:
            for l in set(low_word):
                word_dict[l] = list(low_word).count(l)

            for i in list(word_dict.keys()):
                if i not in low_word or word_dict.get(i, 0) > hand.get(i, 0):
                    valid = False

    return valid

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    return sum(list(hand.values()))


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing
      the string '*END*' instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    tot_score = 0
    is_end_game = False
    new_hand = hand.copy()

    while not is_end_game:

        n = calculate_handlen(new_hand)
        if n <= 0:
            is_end_game = True
        else:
            print('Current Hand: ', end=" ")
            display_hand(new_hand)
            print('Enter word, or "*END*" to indicate that you are finished:', end=' ')
            user_word = str(input())
            user_word_l = user_word.lower()

            if user_word == "*END*":
                print("Total score for this hand: %d points" % (tot_score))
                is_end_game = True

            else:
                if is_valid_word(user_word_l, new_hand, word_list):
                    new_score = get_word_score(user_word_l, n)
                    tot_score += new_score
                    print('"%s" earned %d points. Total: %d points' % (user_word, new_score, tot_score))
                else:
                    print("That is not a valid word. Please choose another word.")
                new_hand = update_hand(new_hand, user_word_l)



    return tot_score

    #raise NotImplementedError #remove this line when you implement this function
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

        # Display the hand

        # Ask user for input

        # If the input is *END*:

            # End the game (break out of the loop)


        # Otherwise (the input is not *END*):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)

            # update the user's hand by removing the letters of their inputted word


    # Game is over (user entered '*END*' or ran out of letters),
    # so tell user the total score

    # Return the total score


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """

    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from VOWELS if the user chooses a VOWEL and
    CONSONANTS if the user chooses a CONSONANT). The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    You can assume that letter is in the hand. Users can not substitute
    the wildcard, so you can also assume letter is not '@'.

    If the user substitutes a VOWEL, they should only get back a VOWEL.
    If a user substitutes a CONSONANT, they should only get back a CONSONANT.

    Has no side effects: does not mutate hand.


    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'

    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand. The new letter should not be 'a','e', 'i','o', or 'u'
    as a consonant should only be subsituted for a consonant.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    substitute_hand = hand.copy()

    key_list, key_vowe, key_cons = list(substitute_hand.keys()), VOWELS, CONSONANTS

    for l in key_list:
        if l in VOWELS:
            key_vowe = key_vowe.replace(l,'')
        elif l in CONSONANTS:
            key_cons = key_cons.replace(l,'')

    if letter.isalpha():
        if letter in VOWELS:
            r = random.choice(key_vowe)
        elif letter in CONSONANTS:
            r = random.choice(key_cons)
        substitute_hand[r] = substitute_hand.get(letter, 0)
        del substitute_hand[letter]

    return substitute_hand

#print(substitute_hand({'h':1, 'e':1, 'l':2, 'o':3}, 'e'))


def play_game(word_list):
    """
    Allow the user to play a series of hands.

    * Asks the user to input a total number of hands to play.

    * Accumulates the score for each hand into a total score for the
      entire series.

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done ONCE during the entire game. Once
      the substitute option is used, the user should not be asked if they want
      to substitute letters for the rest of the game.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand (i.e. the better of the two
      is added to the total score for the game).  This can only be done ONCE
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

    * NOTE: if you replay a hand, you do NOT get the option to substitute
      a letter - you must play whatever hand you just had. If you subsitute a
      letter before you replay, you must use the updated hand with the
      subsituted letter when replaying.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    tot_score = 0
    scores = {}
    is_end_game = False

    print('Enter total number of hands:', end=' ')
    limit_times = int(input())
    hand = deal_hand(HAND_SIZE)
    new_hand = hand.copy()
    replay_times, substitute_times, play_times = 0, 0, 0

    while play_times <= limit_times:


        if is_end_game and play_times <= limit_times:
            scores[play_times] = max(scores.get(play_times, 0), tot_score)
            tot_score = 0
            if replay_times == 0:
                print('---------- \nWould you like to replay the hand?', end=' ')
                replay = str(input()).lower()
                if replay == 'yes':
                    replay_times += 1
                    play_times -= 1
                else:
                    if play_times < limit_times:
                        hand = deal_hand(HAND_SIZE)
                    else:
                        play_times += 1
            else:
                if play_times < limit_times:
                    hand = deal_hand(HAND_SIZE)
                else:
                    play_times += 1

            new_hand = hand.copy()
            is_end_game = False

        while (is_end_game is False) and play_times <= limit_times:

            if substitute_times == 0 and replay_times == 0:
                print('Current Hand: ', end=" ")
                display_hand(new_hand)
                print('Would you like to substitute a letter?', end=' ')
                is_substitute = str(input()).lower()
                if is_substitute != 'no':
                    if is_substitute == 'yes':
                        is_substitute = str(input()).lower()
                    if len(list(is_substitute)) > 1:
                        is_substitute = random.choice(list(is_substitute))
                    hand = substitute_hand(hand, is_substitute)
                    new_hand = hand.copy()
                    substitute_times += 1

            while is_end_game is False:
                if calculate_handlen(new_hand) == 0:
                    play_times += 1
                    is_end_game = True
                else:
                    print('Current Hand: ', end=" ")
                    display_hand(new_hand)
                    print('Enter word, or "*END*" to indicate that you are finished:', end=' ')
                    user_word = str(input())
                    user_word_l = user_word.lower()

                    if user_word == "*END*":
                        print("Total score for this hand: %d points" % (tot_score))
                        play_times += 1
                        is_end_game = True

                    else:
                        if is_valid_word(user_word_l, new_hand, word_list):
                            new_score = get_word_score(user_word_l, calculate_handlen(new_hand))
                            tot_score += new_score
                            print('"%s" earned %d points. Total: %d points' % (user_word, new_score, tot_score))
                        else:
                            print("That is not a valid word. Please choose another word.")
                        new_hand = update_hand(new_hand, user_word_l)

    sum_score = sum(list(scores.values()))
    print("---------- \nTotal score over all hands: ", sum_score)
    return sum_score
    

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
# While debugging, you may want to TEMPORARILY comment out play_game(word_list)

if __name__ == '__main__':
    word_list = load_words()


    #hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    #word = "HELLO"
    # word = 'EVIL'
    #hand =  {'a': 1, 'c': 1, 'i': 1, 'p': 1, 'r': 1, 't': 1, '@': 1}
    # print(is_valid_word(word, hand, word_list))
    # print(calculate_handlen(hand))
    #
    #play_game(word_list)
    hands = [{'a': 1, 'c': 1, 'i': 1, 'p': 1, 'r': 1, 't': 1, '@': 1}]
    test_play_game(word_list, hands, replaced_letter='d')
    #play_hand(hand, word_list)