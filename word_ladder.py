######################################################
# Word Ladder - a ladder-gram program that
# transforms a source word into a target word in
# the least number of steps
#
# All words must exist in the supplied dictionary,
# dictionary.text
#
# Assignment compeleted by Brianna Sonter | s2930629
####################################################

#Import regular expressions library
import re

""" Open the dictionary with exception handling -
Takes file to be opened, if file is invalid FileNotFoundError
will repeat until a valid filename is entered.
"""
def check_dict():
    while True:
        try:
            #take user input for dictionary to be read
            f = input('Please enter dictionary name: ')
            return read_dict(f)
            #move onto rest of program
            break
        except FileNotFoundError:
            #if file name not correct, repeat message until correct
            print("The file you have asked for cannot be found, try dictionary.txt")

#open file from correct filename
def read_dict(file):
    return open(file, 'r')

#read dictionary from correct filename
dict = check_dict()
lines = dict.readlines()


""" Functions to check user inputs -
Makes sure that the user inputs are strings, words longer then 2 letters,
and the target word is the same length as the starting word.
Lets user know when their input is invalid.
"""
# Shortest Path Option
def shortest(spath):
    while True:
        #user wants shortest path
        if spath.lower() == 'y':
            return True
            break
        #user does not want shortest path
        elif spath.lower() == 'n':
            return False
            break
        #user puts in wrong input
        else:
            spath = input("Input must either be Y for yes or N for no. \nWould you like to use the shortest path (Y/N)? ")

#check if start word is valid
def start_check(s):
    while True:
        #user does not put in a word longer than 2 letters
        if len(s) < 2:
            s = input("You must input words with 2 or more letters. \nEnter start word: ")

        #user puts in valid input
        elif s.isalpha():
            return s
            break

        #user puts in charaters other than letters
        else:
            s = input("You must input words with letters only. \nEnter start word: ")

#check if target word is valid
def target_check(t):
    while True:
        #user puts in correct input
        if not t.isalpha():
            t = input("You must input words with letters only. \nEnter start word: ")

        #user does not put in a word the same length as the start word
        elif len(t) != len(start):
            t = input("You must input word the same length as your start word. \nEnter start word: ")

        #user puts in valid input
        else:
            return t
            break


""" Take user inputs and creates a word list of all possible
words that could be used in the ladder-gram - under the conditions
of whether or not the user wants the shortest path and certain words
avoided
"""
while True:
    #find out if user wants shortest path
    spath = input("Would you like to use the shortest path (Y/N)? ")
    shortest_path = shortest(spath)

    #user input of the starting word
    s = input("Enter start word: ")
    start = start_check(s)

    #user input of the target word
    t = input("Enter target word: ")
    target = target_check(t)

    #input for list of words to be avoided
    avoid1 = input("Would you like to include a list of words to avoid (Y/N)? ")

    while True:
        if avoid1.lower() == 'y':
            #creates list of words to be avoided
            avoid2 = input("Enter list of words you would like to avoid: ")
            avoid_list = avoid2
            break

        elif avoid1.lower() == 'n':
            #if no words wish to be added, list is left empty
            avoid_list = []
            break

            #user puts in wrong input
        else:
            avoid1 = input("Input must either be Y for yes or N for no. \nWould you like to include a list of words to avoid (Y/N)? ")

    #empty word list for word transformations
    words = []
    #find words read dictionary
    for line in lines:
        word = line.rstrip()
        #find words of the same length and leave out words user wants to avoid
        if len(word) == len(start) and word not in avoid_list:
            #add words to the word list
            words.append(word)

    break


""" Logic to Formulate ladder-gram -
Goes through all possibilities depending on user inputs to create the
ladder-gram. Finds how many letters are in the same position, builds the
path and then finds the path.
"""
#counts how many letters in each word are in the same position
def same(item, target):
  return len([i for (i, t) in zip(item, target) if i == t])

#searches for words in word_list to produce a match and return a corresponding
# matchObject instance.
def build(pattern, words, seen, word_list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in word_list]

#Find path for the laddergram output
def find(word, words, seen, target, path):
    #create empty list for word path
    word_list = []

    #build list of all possible variations
    for i in range(len(word)):
        word_list += build(word[:i] + "." + word[i + 1:], words, seen, word_list)
    if len(word_list) == 0:
        return False

    #steps taken if shortest path is chosen
    if shortest_path == True:
        word_list = sorted([(same(w, target), w) for w in word_list], reverse=True)

    #steps taken if shortest path is NOT chosen
    else:
        word_list = sorted([(same(w, target), w) for w in word_list])

    #take out uncommon letters to find best path
    uncommon = ["x", "y", "z"]
    #remove words with uncommon letters
    for (match, item) in word_list:
        for letter in uncommon:
            if letter in item:
                word_list.remove((match, item))
        #select best possible words for path list
        if match >= len(target) -1:
            if match == len(target) - 1:
                path.append(item)
            return True
        #add words to seen dictionary to avoid duplicates
        seen[item] = True

    #removes and returns last item in list
    for (match, item) in word_list:
        path.append(item)
        if find(item, words, seen, target, path):
            return True
        path.pop()


""" Final output for the ladder-gram -
Counts number of steps taken to get from the start to the target word. Outputs
the count and the word path taken
"""
#Create count
count = 0

#create a path starting from the start word
path = [start]
seen = {start : True}

#use path finding function
if find(start, words, seen, target, path):
    #add target word on the end of the path list
    path.append(target)
    #print count and path
    print(len(path) - 1, path)
    #allows user to click enter to close program - shows result if not running
    # in shell
    exit = input("\npress enter to exit")
#if no path exists tell user
else:
    print("No path found")
