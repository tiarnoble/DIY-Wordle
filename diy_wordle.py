
import random
from colorama import Fore, Back, Style
import unittest

def read_possible_words(filename):
    """
    This method reads the given file where each line is a single valid 5-letter
    Wordle word and returns the words as a list.
    :param filename: name of the text file containing the valid words
    :return: list of the valid words
    """

    file = open(filename, 'r')
    words = file.readlines()
    clean_words = [word.strip() for word in words]
    return clean_words

def valid_guess(guess, possible_words):
    """
    This method determines and returns whether or not the given guess is valid.
    :param guess: the word that the user guessed (String)
    :return: True if the guess is valid, False otherwise
    """

    if guess is None or len(guess) != 5 or guess.isalpha() == False or guess not in possible_words:
        valid = False
    else:
        valid = True

    return valid

def init_secret_word_info(secret_word):
    """
    This method initializes a list that will hold info on each letter in the secret word.
    :param secret_word: secret word for this game
    :return: list containing 5 lists, each containing a letter (String),
    whether or not the letter was correctly guessed (String),
    and whether or not the letter has been accounted for by another letter
    which will be marked as yellow

    example:
    input: "happy"
    output:
    [
    ['h', 'not found', 'not accounted for']
    ['a', 'not found', 'not accounted for']
    ['p', 'not found', 'not accounted for']
    ['p', 'not found', 'not accounted for']
    ['y', 'not found', 'not accounted for']
    ]
    """

    secret_word_info = []
    for letter in secret_word:
        secret_word_info.append([letter, 'not found', 'not accounted for'])

    return secret_word_info

def update_letters_found(guess, secret_word, secret_word_info):
    """
    Updates the 'found' values for each letter that was guessed correctly
    :param guess: word guessed by user
    :param secret_word: secret word for this round
    :param secret_word_info: list containing info on letters in secret word
    :return: updated secret_word_info
    """

    for k in range(5):
        if guess[k] == secret_word[k]:
            secret_word_info[k][1] = 'found'

    return secret_word_info

def correct_guess(guess):
    """
    Prints all letters as green and tells the user they are correct.
    :param guess: correct guess given by user
    :return: returns nothing
    """

    for m in guess:
        print_letter(m, 'GREEN')
        print(Style.RESET_ALL, end='   ')

    print()
    print("Congrats! You guessed the word!")

def print_letter(letter, color):
    """
    Prints the given letter in the correct format given the color
    :param letter: letter to print
    :param color: color to use as background
    :return: returns nothing
    """

    if (color == 'GREEN'):
        print(Back.GREEN + '  ' + letter.upper(), end='  ')

    elif (color == 'YELLOW'):
        print(Back.YELLOW + '  ' + letter.upper(), end='  ')

    else:
        print(Back.BLACK + Fore.WHITE + '  ' + letter.upper(), end='  ')

def run_game():
    """
    This method runs one full round of the game Wordle.
    :return: returns nothing
    """

    # read data
    possible_words = read_possible_words('valid-wordle-words.txt')

    # randomly choose secret word for this game
    secret_word = random.choice(possible_words)

    guess_number = 1
    while(1):

        # initialize list containing info on each letter
        secret_word_info = init_secret_word_info(secret_word)

        # prompt for word and read user input
        print()
        guess = input("Please type guess number " + str(guess_number) + " and click enter: ")

        # make sure the guess is valid
        if valid_guess(guess, possible_words) == False:
            print("That is not a valid 5-letter word. Please try again.")
            continue

        # check if the guess is correct
        if guess == secret_word:
            correct_guess(guess)
            return

        # update secret_word_info based on correct letters
        secret_word_info = update_letters_found(guess, secret_word, secret_word_info)

        # check each letter and print green, yellow, or gray for each letter
        for j in range(5):

            letter = guess[j]
            if letter == secret_word[j]:
                print_letter(letter, 'GREEN')

            elif letter in secret_word:
                yellow = False

                for k in range(5):
                    if secret_word_info[k][0] == letter and secret_word_info[k][1] == 'not found' and secret_word_info[k][2] == 'not accounted for':
                        print_letter(letter, 'YELLOW')
                        secret_word_info[k][2] = 'accounted for'
                        yellow = True
                        break

                if yellow == False:
                    print_letter(letter, 'GRAY')

            else:
                print_letter(letter, 'GRAY')

            print(Style.RESET_ALL, end='   ')

        # increment guess count
        guess_number += 1

        # check if user has run out of guesses
        if (guess_number > 6):
            print(Style.RESET_ALL)
            print("Nice try!")
            print("The secret word was: " + secret_word.upper())
            return

def main():

    # print welcome message, explain how to play
    print("Welcome to DIY Wordle!\n")
    print("You will have six tries to guess the five-letter word.\n"
          "Each letter in each guess will appear in one of three colors:\n"
          "GREEN: the letter is in the correct place\n"
          "YELLOW: the letter is in the word but not in that place \n"
          "GRAY: the letter is not in the word at all\n")
    print("If you haven't figured it out at the end I will reveal the word.")

    # start the game
    run_game()

    # print thank you message
    print("Thanks for playing!")
    return

if __name__ == "__main__":
    main()

# class TestDIYWordle(unittest.TestCase):
#
#     def test_read_possible_words(self):
#
#         possible_words = read_possible_words('valid-wordle-words.txt')
#         self.assertEqual(len(possible_words), 12972, "did not read th correct number of words from the file")
#
#         self.assertEqual(possible_words[500], "ardri", "not the correct word at index 500")
#
#         self.assertEqual(possible_words[8000], "pases", "not the correct word at index 8000")
#
#     def test_valid_guess(self):
#
#         poss_words = ["happy", "block", "sting", "quote"]
#
#         # test null guess
#         guess = None
#         val = valid_guess(guess, poss_words)
#         self.assertEqual(val, False, "valid_guess failed test")
#
#         # test wrong length
#         guess = "orange"
#         val = valid_guess(guess, poss_words)
#         self.assertEqual(val, False, "valid_guess failed test")
#
#         # test non-letters
#         guess = "l0oks"
#         val = valid_guess(guess, poss_words)
#         self.assertEqual(val, False, "valid_guess failed test")
#
#         # test not possible word
#         guess = "xpajw"
#         val = valid_guess(guess, poss_words)
#         self.assertEqual(val, False, "valid_guess failed test")
#
#         # test valid word
#         guess = "sting"
#         val = valid_guess(guess, poss_words)
#         self.assertEqual(val, True, "valid_guess failed test")
#
#     def test_init_secret_word_info(self):
#
#         secret_word = "happy"
#         secret_word_info = init_secret_word_info(secret_word)
#         ans = [['h', 'not found', 'not accounted for'],
#                ['a', 'not found', 'not accounted for'],
#                ['p', 'not found', 'not accounted for'],
#                ['p', 'not found', 'not accounted for'],
#                ['y', 'not found', 'not accounted for']]
#
#         self.assertEqual(secret_word_info, ans, "init_secret_word_info failed test")
#
#     #def test_update_letters_found(self):
#
#
#
#         #
#         #
#         # guess = a
#         # secret_word = a
#         # secret_word_info = a
#         # x = update_letters_found(guess, secret_word, secret_word_info)
#
#     #def test_run_game(self):
#         #
#         #
#         # self.assertEqual(rectangle.get_area(), 6, "incorrect area")