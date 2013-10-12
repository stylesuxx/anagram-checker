#!/usr/bin/python
import sys, signal, argparse
from itertools import permutations

def signal_handler(signal, frame):
        print 'Exiting...'
        sys.exit(0)

def main(args):
  base = args.base.lower()
  words = args.words
  words.append(base)

  if len(words) > 1:
    print isAnagram(words)
  else:
    printAnagrams(base)
    
# Print all possible anagrams of base
# We print it instead of saving it to a list because we
# would run out of memory when generating anagrams from
# longer input
def printAnagrams(base):
  for p in permutations(base):
    print ''.join(p)

# Check if the given list of words are anagrams of each
# other.
def isAnagram(words):
  # Just one word: no Anagram
  if len(words) is 1:
    return False;

  # If one of the words has not the same length we certainly have no anagram
  length = len(words[0])
  for word in words[1:]:
    if len(word) != length:
      return False

  # Count the letters of each word and save them in a dict.
  dicts = {}
  for word in words:
    dicts[word] = {}
    current = dicts[word]
    for char in word:
      if current.has_key(char):
        current[char] = current[char] + 1
      else:
        current[char] = 1

  # Get the first element from list, this will be the reference element
  # to check against.
  first = words.pop()
  first = dicts[first]
  
  # Compare each dicts with each other.
  # Different amount of items means they can not be anagrams.
  length = len(first)
  for d in words:
    if len(dicts[d]) != length:
      return False 

  # Compare the amount of every letter in one word with all the other words.
  # If one does not match we have no anagram
  for d in words:
    current = dicts[d]
    for c in first:
      if not current.has_key(c) or first[c] != current[c]:
        return False

  # All inputs are anagram of each other
  return True

parser = argparse.ArgumentParser(description='Generates anagrams if one string is provided, otherwise checks if all strings are anagrams of each other. Identical strings are treated as anagrams as well.')

parser.add_argument(dest = 'base',
                    metavar = 'BASE',
                    help = 'The string to generate anagrams or check other strings against.')

parser.add_argument(dest = 'words',
                    metavar = 'STRING',
                    nargs = '*',
                    help = 'Strings to be checked.')

signal.signal(signal.SIGINT, signal_handler)
args = parser.parse_args()
main(args)