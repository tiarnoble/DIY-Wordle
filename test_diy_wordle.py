
import unittest
import diy_wordle

class TestDIYWordle(unittest.TestCase):

    def test_read_possible_words(self):

        possible_words = diy_wordle.read_possible_words('wordle-possible-answers.txt')
        self.assertEqual(len(possible_words), 12972, "did not read th correct number of words from the file")

        self.assertEqual(possible_words[500], "ardri", "not the correct word at index 500")

        self.assertEqual(possible_words[8000], "pases", "not the correct word at index 8000")

    def test_valid_guess(self):

        poss_words = ["happy", "block", "sting", "quote"]

        # test null guess
        guess = None
        val = diy_wordle.valid_guess(guess, poss_words)
        self.assertEqual(val, False, "valid_guess failed test")

        # test wrong length
        guess = "orange"
        val = diy_wordle.valid_guess(guess, poss_words)
        self.assertEqual(val, False, "valid_guess failed test")

        # test non-letters
        guess = "l0oks"
        val = diy_wordle.valid_guess(guess, poss_words)
        self.assertEqual(val, False, "valid_guess failed test")

        # test not possible word
        guess = "xpajw"
        val = diy_wordle.valid_guess(guess, poss_words)
        self.assertEqual(val, False, "valid_guess failed test")

        # test valid word
        guess = "sting"
        val = diy_wordle.valid_guess(guess, poss_words)
        self.assertEqual(val, True, "valid_guess failed test")

    def test_init_secret_word_info(self):

        secret_word = "happy"
        secret_word_info = diy_wordle.init_secret_word_info(secret_word)
        ans = [['h', 'not found', 'not accounted for'],
               ['a', 'not found', 'not accounted for'],
               ['p', 'not found', 'not accounted for'],
               ['p', 'not found', 'not accounted for'],
               ['y', 'not found', 'not accounted for']]

        self.assertEqual(secret_word_info, ans, "init_secret_word_info failed test")

    #def test_update_letters_found(self):



        #
        #
        # guess = a
        # secret_word = a
        # secret_word_info = a
        # x = update_letters_found(guess, secret_word, secret_word_info)

    #def test_run_game(self):
        #
        #
        # self.assertEqual(rectangle.get_area(), 6, "incorrect area")