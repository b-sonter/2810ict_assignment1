######################################################
# Word Ladder - a ladder-gram program that
# transforms a source word into a target word in
# the least number of steps
#
# All words must exist in the supplied dictionary,
# dictionary.text
#
# Code fixed by Brianna Sonter | s2930629
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
        if spath.lower() == 'y':
            return True
            break

        elif spath.lower() == 'n':
            return False
            break
        else:
            spath = input("Input must either be Y for yes or N for no. \nWould you like to use the shortest path (Y/N)? ")


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
    start = input("Enter start word: ")

    #user input of the target word
    target = input("Enter target word: ")

    #input for list of words to be avoided
    avoid1 = input("Would you like to include a list of words to avoid (Y/N)? ")
    if avoid1 == 'Y':
        #creates list of words to be avoided
        avoid_list = input("Enter list of words you would like to avoid: ")
    else:
        #if no words wish to be added, list is left empty
        avoid_list = []

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
  return len([item for (item, target) in zip(item, target) if item == target])

def hamming(item, target):
    return sum(i != t for i, t in zip(item, target))

#
def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

#Find path
def find(word, words, seen, target, path):

    list = []

    for i in range(len(word)):
        list += build(word[:i] + "." + word[i + 1:], words, seen, list)

    if len(list) == 0:
        return False

    if shortest_path == True:
        list = sorted([(hamming(w, target), w) for w in list])
    else:
        list = sorted([(same(w, target), w) for w in list])

    for (match, item) in list:
        if match >= len(target) - 1:
            if match == len(target) - 1:
                path.append(item)
            return True
        seen[item] = True

    for (match, item) in list:
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
#if no path exists tell user
else:
    print("No path found")
