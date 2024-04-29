codewars2804 = """Given two integers a and b, which can be positive or negative,
find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.
Note: a and b are not ordered!
Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)"""


def get_sum(a, b):
    if a == b:
        return a
    sum_ = 0
    lst = sorted([a, b])
    for i in range(lst[0], lst[1] + 1):
        sum_ += i
    return sum_


# I should have just used min and max in the range instead of sorting


# print(get_sum(1, 2))
# print(get_sum(2, 1))
# print(get_sum(1, -1))
# print(get_sum(6, 0))
# print(get_sum(2, 2))

"""Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
i.e. friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output."""


def friend(x):
    return [i for i in x if len(i) == 4]


# print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
# print(friend(["Ryan", "Kieran", "Mark"]))

"""Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, 
containing distinct letters - each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" """  # this description could be better


def longest(a1, a2):
    c = [x for x in set(a1 + a2)]
    return "".join(sorted(c))


#     return "".join(sorted(set(a1 + a2)))
# sorted will transform set into list!


# print(longest(a1 = "xyaabbbccccdefww", a2 = "xxxxyyyyabklmopq"))


"""Create a function that checks if a number n is divisible by two numbers x AND y.
All inputs are positive, non-zero numbers."""


def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


# not even worth bothering to check this one lol

"""Implement a function which convert the given boolean value into its string representation.
Note: Only valid inputs will be given.
"""


def boolean_to_string(b):
    # return 'False' if b == False else 'True'
    return str(b)


# what are those

"""Your classmates asked you to copy some paperwork for them. 
You know that there are 'n' classmates and the paperwork has 'm' pages.
Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
Example:
n= 5, m=5: 25
n=-5, m=5:  0 """


def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m


# zZzZzZzZ
"""There is a bus moving in the city which takes and drops some people at each bus stop.
You are provided with a list (or array) of integer pairs. 
Elements of each pair represent the number of people that get on the bus (the first item)
and the number of people that get off the bus (the second item) at a bus stop.
Your task is to return the number of people who are still on the bus after the last bus stop (after the last array).
Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus,
they are probably sleeping there :D Take a look on the test cases:
Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. 
So the returned integer can't be negative.
The second value in the first pair in the array is 0, since the bus is empty in the first bus stop."""


def number(bus_stops):
    # c = 0
    # for i in bus_stops:
    #     c += i[0] - i[1]
    return sum(i[0] - i[1] for i in bus_stops)


# print(number([[5, 0], [10, 12], [5, 2]]))

"""Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it. "a" = 1, "b" = 2, etc.
Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )"""


def alphabet_position(text):
    positions = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                 'x': 24, 'y': 25, 'z': 26}
    return " ".join([str(positions[i]) for i in text.lower() if i.isalpha()])


# return " ".join([str(positions[i]) if i.isalpha() else i for i in text.lower()]) # IGNORE IT IF IT IS NOT CHARACTER


# print(alphabet_position("The sunset se99ts at twelve o' clock."))

"""A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits,
each raised to the power of the number of digits in a given base.
In this Kata, we will restrict ourselves to decimal (base 10).
For example, take 153 (3 digits), which is narcissistic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:
Your code must return true or false (not 'true' and 'false') 
depending upon whether the given number is a Narcissistic number in base 10.
This may be True and False in your language, e.g. PHP.
Error checking for text strings or other invalid inputs is not required, 
only valid positive non-zero integers will be passed into the function."""

def narcissistic(value):
    return eval("".join(f"+{i}**{len(str(value))}" for i in str(value))) == value
# eturn value == sum(int(x) ** len(str(value)) for x in str(value)) # takie coś ktoś miał i jest lepsze
#     ktoś miał też takie w sumie dużo prostsze
#     value = str(value)
#     size = len(value)
#     sum = 0
#     for i in value:
#         sum += int(i) ** size
#     return sum == int(value)


# print(narcissistic(153))
# print(narcissistic(1653))
