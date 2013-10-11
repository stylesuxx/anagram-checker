#### Anagram checker and generator
If only one string is passed, all possible anagrams of this string are generated.
If multiple strings are passed, all strings are checked if they are anagrams of each other.

```
usage: anagram_checker.py [-h] BASE [STRING [STRING ...]]

Generates anagrams if one string is provided, otherwise checks if all strings
are anagrams of each other. Identical strings are treated as anagrams as well.

positional arguments:
  BASE        The string to generate anagrams or check other strings against.
  STRING      Strings to be checked.

optional arguments:
  -h, --help  show this help message and exit
```
