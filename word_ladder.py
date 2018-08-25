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
while True:
    try:
        #take user input for dictionary to be read
        f = open(input('Please enter dictionary name: '), 'r')
        #move onto rest of program
        break
    except FileNotFoundError:
        #if file name not correct, repeat message until correct
        print("The file you have asked for cannot be found, try dictionary.txt")

#read dictionary from correct filename
lines = f.readlines()


""" Take user input for the start and target words-
Takes inputs while checking that they are invalid
inputs
"""
while True:
  start = input("Enter start word: ")
  target = input("Enter target word: ")

  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  break



#list of words not to be used

#option to ask for the shortest path

#counts how many letters in each word are in the same position
def same(item, target):
  return len([item for (item, target) in zip(item, target) if item == target])


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

  list = sorted([(same(w, target), w) for w in list], reverse=True)

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

#Count steps for path
count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")
