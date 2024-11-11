cw = '''As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0

2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

Another example (just to make sure it is clear):

gimme([5, 10, 14]) => 1

10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.
'''

import numpy as np


def gimme(input_array):
    return np.argsort(input_array)[1]
    # return inputArray.index(sorted(inputArray)[1])


# print(gimme([2, 3, 1]))
# print(gimme([5, 10, 14]))
# print(gimme([7, 12, 9]))

'''Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
Examples:

"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"

'''


# return ''.join(letter.upper() if idx % 2 == 0 else letter for idx, letter in enumerate(words))  # if the counting didn't reset after each word


def to_weird_case(words):
    # words_arr = words.split()
    # uppered = []
    # for word in words_arr:
    #     uppered.append(''.join(letter.upper() if idx % 2 == 0 else letter.lower() for idx, letter in enumerate(word)))
    # return ' '.join(uppered)

    return ' '.join(''.join(letter.upper() if idx % 2 == 0 else letter.lower() for idx, letter in enumerate(word)) for word in words.split())


#
# print(to_weird_case("String"))
# print(to_weird_case("Weird string case"))


'''An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
Examples

    "foefet" is an anagram of "toffee"

    "Buckethead" is an anagram of "DeathCubeK"

'''
# super simple one:
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

# way more efficient for long strings
# from collections import Counter
#
# def is_anagram(test, original):
#     return Counter(test.lower()) == Counter(original.lower())


print(is_anagram('Buckethead', 'DeathCubeK'))