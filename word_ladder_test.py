######################################################
# Word Ladder unittest - tests based on inputs
# for word_ladder program
#
#
# Assignment compeleted by Brianna Sonter | s2930629
####################################################

import unittest
import word_ladder

class test_word_ladder(unittest.TestCase):

    #test shortest path check for user inputs
    def test_shortest(self):
        #check for a yes input
        self.assertTrue(word_ladder.shortest("y"))
        #check for a no input
        self.assertFalse(word_ladder.shortest("n"))


    def test_start_check(self):
        #valid input
        self.assertEqual(word_ladder.start_check("lead"), "lead")
        self.assertEqual(word_ladder.start_check("hide"), "hide")

    def test_target_check(self):
        #valid input
        self.assertEqual(word_ladder.start_check("gold"), "gold")
        self.assertEqual(word_ladder.start_check("seek"), "seek")


    def test_same(self):
        #test to see if program counts the right amount of same letters
        self.assertEqual(word_ladder.same("hell", "help"), 3)
        self.assertEqual(word_ladder.same("hide", "seek"), 0)
        self.assertEqual(word_ladder.same("lead", "gold"), 1)
        self.assertEqual(word_ladder.same("super", "duper"), 4)

    def test_build(self):
        #invalid inputs for build will retrun false
        self.assertFalse(word_ladder.build("asdsf", "asdfsdf", "msdfsdfh", []))


    def test_find(self):
        #invalid inputs will return false
        self.assertFalse(word_ladder.find("sdfsdf", "sdad", "sdfsdf", "sdfsd", "sdfsdf"))


if __name__ == '__main__':
    unittest.main()
