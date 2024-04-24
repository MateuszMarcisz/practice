""" In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
 Examples
 high_and_low("1 2 3 4 5")  # return "5 1"
 high_and_low("1 2 -3 4 5") # return "5 -3"
 high_and_low("1 9 3 4 -5") # return "9 -5" """


def high_and_low(numbers):
    numberz = [int(x) for x in numbers.split()]
    return str(sorted(numberz)[-1]) + " " + str(sorted(numberz)[0])
    # return f"{max(numberz)} {min(numberz)}" # this one also works and is simpler


# print(high_and_low("0 2 3 -5 14 5 17 12"))
"""Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321"""


def descending_order(num):
    return int("".join(sorted([x for x in str(num)], reverse=True)))


# print(descending_order(123456789))
# print(descending_order(145268889963))

"""You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, 
return the middle character. If the word's length is even, return the middle 2 characters.
#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
#Input
A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.
#Output
The middle character(s) of the word represented as a string."""


def get_middle(s):
    # if len(s) % 2 == 0:
    #     return s[len(s)//2-1:len(s)//2+1]
    # else:
    #     return s[len(s)//2]
    return s[len(s) // 2 - 1:len(s) // 2 + 1] if len(s) % 2 == 0 else s[len(s)//2]


# print(get_middle("testing"))
# print(get_middle("middle"))

