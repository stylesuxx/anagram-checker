#!/usr/bin/python
import sys, argparse

def main(args):
  print isPalindrome(args.words)

def isPalindrome(words):
  # One word: no palindrome
  if len(words) is 1:
    return False;

  # If one of the words has not the same length we certainly have no palindrome
  length = len(words[0])
  for word in words[1:]:
    if len(word) != length:
      return False

  # Now we can start checking for palindromes.
  # Count the letters of each word and save them in a dict.
  # Compare each dicts with each other.
  # Different amount of items means they can not be palindromes.
  # Compare the amount of every letter in one word with all the other words.
  # If one does not match we have no palindrome
  return True

parser = argparse.ArgumentParser(description='This description is shown when -h or --help are passed as arguments.')

parser.add_argument(dest = 'words',
                    metavar = 'STRING',
                    nargs = '+',
                    help = 'Strings to be checked if they are palindormes.')

args = parser.parse_args()
main(args)