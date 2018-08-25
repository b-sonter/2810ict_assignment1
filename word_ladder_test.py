import unittest
import word_ladder

#class test_isPrime(unittest.TestCase):
#    def test_prime(self):
#        self.assertTrue(isPrime.is_prime(5))
#        self.assertTrue(isPrime.is_prime(0))

class test_word_ladder(unittest.TestCase):

    #check dictionary inputs
    def test_check_dict(self):
        self.assertEqual(word_ladder.read_dict(""), "The file you have asked for cannot be found, try dictionary.txt")

    def test_same(self):
        self.assertTrue(word_ladder.same("hell", "help") == 3)


if __name__ == '__main__':
    unittest.main()
