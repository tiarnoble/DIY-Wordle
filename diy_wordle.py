
import random
from colorama import Fore, Back, Style

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

    print('\n')
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

    elif (color == 'BLACK'):
        print(Back.BLACK + Fore.WHITE + '  ' + letter.upper(), end='  ')

    else:
        print(Back.WHITE + Fore.BLACK + '  ' + letter.upper(), end='  ')



def init_keyboard():

    keyboard = {
        'Q': "GRAY",
        'W': "GRAY",
        'E': "GRAY",
        'R': "GRAY",
        'T': "GRAY",
        'Y': "GRAY",
        'U': "GRAY",
        'I': "GRAY",
        'O': "GRAY",
        'P': "GRAY",
        'A': "GRAY",
        'S': "GRAY",
        'D': "GRAY",
        'F': "GRAY",
        'G': "GRAY",
        'H': "GRAY",
        'J': "GRAY",
        'K': "GRAY",
        'L': "GRAY",
        'Z': "GRAY",
        'X': "GRAY",
        'C': "GRAY",
        'V': "GRAY",
        'B': "GRAY",
        'N': "GRAY",
        'M': "GRAY"
    }

    return keyboard


def print_keyboard(keyboard):

    print()

    for key, color in keyboard.items():
        print_letter(key, color)
        if (key == 'P'):
            print(Style.RESET_ALL)
            print('\n   ', end='')
        elif (key == 'L'):
            print(Style.RESET_ALL)
            print('\n      ', end='')
        else:
            print(Style.RESET_ALL, end=' ')

    print()


def print_previous_guesses(previous_guesses):

    for guess in previous_guesses.values():
        for x in guess:
            print_letter(x[0], x[1])
            print(Style.RESET_ALL, end='   ')

        print('\n')


def run_game():
    """
    This method runs one full round of the game Wordle.
    :return: returns nothing
    """

    # read data
    possible_words_no_answers = read_possible_words('wordle-allowed-guesses.txt')
    possible_answers = read_possible_words('wordle-possible-answers.txt')

    possible_words = possible_words_no_answers + possible_answers

    # randomly choose secret word for this game
    secret_word = random.choice(possible_answers)

    keyboard = init_keyboard()

    previous_guesses = {}

    guess_number = 1
    while(1):

        # initialize list containing info on each letter
        secret_word_info = init_secret_word_info(secret_word)

        if guess_number > 1:
            print_keyboard(keyboard)

        print('\n')

        # prompt for word and read user input
        guess = input("Please type guess number " + str(guess_number) + " and click enter: ")

        print('\n')

        # make sure the guess is valid
        if valid_guess(guess, possible_words) == False:
            print("That is not a valid 5-letter word. Please try again.")
            continue

        if guess_number > 1:
            print_previous_guesses(previous_guesses)

        # check if the guess is correct
        if guess == secret_word:
            correct_guess(guess)
            return

        guess_list = []

        # update secret_word_info based on correct letters
        secret_word_info = update_letters_found(guess, secret_word, secret_word_info)

        # check each letter and print green, yellow, or gray for each letter
        for j in range(5):

            letter = guess[j]
            if letter == secret_word[j]:
                color = 'GREEN'

            elif letter in secret_word:
                yellow = False

                for k in range(5):
                    if secret_word_info[k][0] == letter and secret_word_info[k][1] == 'not found' and secret_word_info[k][2] == 'not accounted for':
                        color = 'YELLOW'
                        secret_word_info[k][2] = 'accounted for'
                        yellow = True
                        break

                if yellow == False:
                    color = 'BLACK'

            else:
                color = 'BLACK'

            print_letter(letter, color)
            guess_list.append((letter, color))
            keyboard[letter.upper()] = color

            print(Style.RESET_ALL, end='   ')

        # increment guess count
        guess_number += 1

        previous_guesses[guess_number] = guess_list

        print('\n')

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
          "BLACK: the letter is not in the word at all\n")
    print("If you haven't figured it out at the end I will reveal the word.")

    # start the game
    run_game()

    # print thank you message
    print("Thanks for playing!")
    return

if __name__ == "__main__":
    main()
