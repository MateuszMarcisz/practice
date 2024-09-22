cw = """Digitwise addition is a special kind of addition where instead of adding 1 normally to the number, it adds 1 to every digit of that number. If the digit is a 9, we replace it with a "10" without carrying over to the next digit.

Examples:

123 -> 234

910 -> 1021

789 -> 8910
Program a function that takes two numbers, N and K, and outputs the number of digits in N after applying Digitwise addition K times. Since the answer can be very large, return the answer modulo 10 ** 9 + 7

Specifications: 1 <= N <= 10^9, 1 <= K <= 10^5

Example 1:

digitwise_addition(9812, 2) -> 6

# Explanation:
# 9812 -> 10923 -> 211034 -> 6 digits
Example 2:

digitwise_addition(9899, 3) -> 8

# Explanation:
# 9899 -> 1091010 -> 21102121 -> 32213232 -> 8 digits
Subtask 1: K <= 20, 30 tests

Subtask 2: K <= 50, 20 tests

Subtask 3: K <= 10^5, 50 tests"""


def digitwise_addition(n, k):
    n = [int(digit) for digit in str(n)]
    for i in range(k):
        nums = [digit + 1 for digit in n]
        n = [int(digit) for num in nums for digit in str(num)]
    return len(n) % (10 ** 9 + 7)


# print(digitwise_addition(9812, 2))
# print(digitwise_addition(9899, 3))

# this solution works but is too slow to pass the tests

"""Fellow code warrior, we need your help! We seem to have lost one of our sequence elements, and we need your help to retrieve it!

Our sequence given was supposed to contain all of the integers from 0 to 9 (in no particular order), but one of them seems to be missing.

Write a function that accepts a sequence of unique integers between 0 and 9 (inclusive), and returns the missing element.

Examples:
[0, 5, 1, 3, 2, 9, 7, 6, 4] --> 8
[9, 2, 4, 5, 7, 0, 8, 6, 1] --> 3"""


def get_missing_element(seq):
    seq = sorted(seq)
    for i in range(10):
        if i not in seq:
            return i


# print(get_missing_element([9, 2, 4, 5, 7, 0, 8, 6, 1]))
# print(get_missing_element([0, 5, 1, 3, 2, 9, 7, 6, 4]))
# print(get_missing_element([0, 5, 1, 3, 2, 8, 7, 6, 4]))


"""Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!"""


def find_missing_letter(chars):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z'
    ]

    start = alphabet.index(chars[0])
    end = alphabet.index(chars[-1])
    compare = alphabet[start:end]
    for i in compare:
        if i not in chars:
            return i


# print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
# print(find_missing_letter(['O', 'Q', 'R', 'S']))
