# Problem Set 4B
# Name: Tuo Sun
# Collaborators: Sen Dai
# Time Spent: 4:00

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    is_word(word_list, 'bat') returns
    True
    is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''

        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dicts(self, shifts):
        '''
        Creates a list of dictionaries; each dictionary can be used to apply a
        cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. By shifted down, we mean 
        that if 'a' is shifted down by 2, the result is 'c.'

        The dictionary should have 52 keys of all the uppercase letters and
        all the lowercase letters only.

        shifts (list of integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a list of dictionaries mapping letter (string) to
                 another letter (string).
        '''

        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet = lower_alphabet.upper()
        shift_dicts = []
        for num in shifts:
            dict = {}
            for i in range(26):
                dict[lower_alphabet[i]] = (lower_alphabet * 2)[i + num]
                dict[upper_alphabet[i]] = (upper_alphabet * 2)[i + num]
            shift_dicts.append(dict)
        return shift_dicts

    def apply_shift(self, shift_dicts):
        '''
        Applies the Caesar Cipher to self.message_text with letter shifts 
        specified in shift_dict. Creates a new string that is self.message_text, 
        shifted down the alphabet by some number of characters, determined by 
        the shift value that shift_dict was built with.       
        
        shift_dict: list of dictionaries; each dictionary with 52 keys, mapping
            lowercase and uppercase letters to their new letters
            (as built by build_shift_dict)

        Returns: the message text (string) with every letter shifted using the
            input shift_dicts 

        '''
        text_list = list(self.message_text)
        i, j = 0, 0
        while i < len(text_list):
            if j == len(shift_dicts):
                j = 0
            if text_list[i].isalpha():
                text_list[i] = shift_dicts[j][text_list[i]]
            i += 1
            j += 1

        return ''.join(text_list)


class PlaintextMessage(Message):
    def __init__(self, text, shifts):
        '''
        Initializes a PlaintextMessage object.       
        
        text (string): the message's text
        shifts (list of integers): the list of shifts associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shifts (list of integers, determined by input shifts)
            self.encryption_dicts (list of dictionaries, built using shifts)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")
        self.shifts = shifts
        self.encryption_dicts = self.build_shift_dicts(shifts)
        self.encrypted_message_text = self.apply_shift(self.encryption_dicts)

    def get_shifts(self):
        '''
        Used to safely access self.shifts outside of the class
        
        Returns: self.shifts
        '''

        return self.shifts

    def get_encryption_dicts(self):
        '''
        Used to safely access a copy self.encryption_dicts outside of the class
        
        Returns: a COPY of self.encryption_dicts
        '''
        copy_dicts = self.build_shift_dicts(self.shifts).copy()
        return copy_dicts

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class
        
        Returns: self.encrypted_message_text
        '''
        return self.encrypted_message_text

    def change_shifts(self, shifts):
        '''
        Changes self.shifts of the PlaintextMessage, and updates any other 
        attributes that are determined by the shift list.        
        
        shifts (list of length 2): the new shift that should be associated with this message.
        [0 <= shift < 26]

        Returns: nothing
        '''
        self.shifts = shifts
        self.encryption_dicts = self.build_shift_dicts(shifts)
        self.encrypted_message_text = self.apply_shift(self.encryption_dicts)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text
        
        a CiphertextMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible combination of shift
        values and finding the "best" one. 
        We will define "best" as the list of shifts that creates the maximum number
        of valid English words when we use apply_shift(shifts)on the message text. 
        If [a, b] are the original shift values used to encrypt the message, then we 
        would expect [(26 - a), (26 - b)] to be the best shift values for
        decrypting it.

        Note: if multiple lists of shifts are equally good, such that they all create 
        the maximum number of valid words, you may choose any of those lists
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value list used to decrypt the message
        and the decrypted message text using that shift value
        '''

        a, b, num = 0, 0, 0
        num_dict = {}

        for a in range(27):
            for b in range(27):
                shift_dicts = self.build_shift_dicts([(26-a), (26-b)])
                decrypt_txt = self.apply_shift(shift_dicts)
                valid_word_list = []
                for word in decrypt_txt.split(' '):
                    if is_word(self.valid_words, word):
                        valid_word_list.append(word)

                num_dict[len(valid_word_list)] = [(26-a), (26-b)]
                num = max(num, len(valid_word_list))

        best_shift = num_dict[num]

        return best_shift, self.apply_shift(self.build_shift_dicts(best_shift))


def test_plaintext_message():
    '''
    Write two test cases for the PlaintextMessage class here. 
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what 
    case(s) it is testing. 
    '''

    #### Example test case (PlaintextMessage) #####

    # This test is checking encoding a lowercase string with punctuation in it.
    # plaintext = PlaintextMessage('hello!', [2,3])
    # plaintext1 = PlaintextMessage('jhnoq!', [24, 23])
    # print('Expected Output: jhnoq!')
    # print('Actual Output:', plaintext.get_encrypted_message_text())
    # print('Actual Output:', plaintext1.get_encrypted_message_text())
    pass

def test_ciphertext_message():
    '''
    Write two test cases for the CiphertextMessage class here. 
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what 
    case(s) it is testing. 
    '''

    #### Example test case (CiphertextMessage) #####
    
    #This test is checking decoding a lowercase string with punctuation in it.
    ciphertext = CiphertextMessage('tojhcsj, qrh,')
    print('Expected Output:', ([2, 3], 'hello!'))
    print('Actual Output:', ciphertext.decrypt_message())
    pass

def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your CiphertextMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    story_txt = CiphertextMessage(get_story_string())
    return story_txt.decrypt_message()


if __name__ == '__main__':

    # Uncomment these lines to try running your test cases 
    # test_plaintext_message()
    # test_ciphertext_message()

    # Uncomment these lines to try running decode_story_string()
    # best_shift, story = decode_story()
    # print("Best shift:", best_shift)
    # print("Decoded story: ", story)
    pass 
