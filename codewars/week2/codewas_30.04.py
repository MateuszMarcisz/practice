codewars304 = """Introduction

The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
Task Given a year, return the century it is in. Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28
Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here"""


def century(year):
    return year // 100 if year % 100 == 0 else year // 100 + 1


# print(century(1700))
"""Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
For example:
time = 3 ----> litres = 1
ime = 6.7---> litres = 3
time = 11.8--> litres = 5"""


def litres(time):
    return time // 2


"""Some numbers have funny properties. For example:
    89 --> 8¹ + 9² = 89 * 1
    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given two positive integers n and p, we want to find a positive integer k, if it exists,
such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.
In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :
(ap+bp+1+cp+2+dp+3+...)=n∗k(a^p + b^{p + 1} + c^{p + 2} + d^{p + 3} + ...) = n * k(ap+bp+1+cp+2+dp+3+...)=n∗k
If it is the case we will return k, if not return -1.
Note: n and p will always be strictly positive integers.
Examples:
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1
n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k
n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51"""


def dig_pow(n, p):
    str_for_eval = ""
    for i in str(n):
        str_for_eval += f"+{i}**{p}"
        p += 1
    return eval(str_for_eval) // n if eval(str_for_eval) % n == 0 else -1


def dig_pow(n, p):
    sum_ = sum(int(j) ** (p + i) for i, j in enumerate(str(n)))
    return sum_ // n if sum_ % n == 0 else -1

    # sum_ = sum(int(j) ** (p + i) for i, j in enumerate(str(n)))
    # lst = []
    # for i, j in enumerate(str(n)):
    #     lst.append(int(j) ** (p + i))
    # return sum(lst)

    # return sum_ // n if sum_ % n == 0 else -1


# print(dig_pow(89, 1))
# print(dig_pow(89, 2))
# print(dig_pow(695, 2))
# print(dig_pow(46288, 3))


"""A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
Ignore numbers and punctuation."""


def is_pangram(s):
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'}
    return alphabet == {letter for letter in s.lower() if letter.isalpha()}
    # to_compare = set()
    # for letter in s.lower():
    #     if letter.isalpha():
    #         to_compare.add(letter)
    # return to_compare == alphabet


# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("The quic52435k br245own fox jumps o1245ver thwqee lazy dog"))

"""You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.
For example:
Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.
Note: Please remember that in most languages the index of an array starts at 0.
Input
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
Output
The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.
Note
If you are given an array with multiple answers, return the lowest correct index.
"""


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i+1]) == sum(arr[i:]):
            return i
    return -1


# print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
# print(find_even_index([0, 0, 0, 0, 0, 0, 0]))

def pig_it(text):
    return " ".join([(i[1:]+i[:1]+'ay') if i.isalpha() else i for i in text.split()])
    # pigs = []
    # for i in text.split():
    #     pigs.append(i[1:]+i[:1]+'ay') if i.isalpha() else pigs.append(i)
    # return " ".join(pigs)


# print(pig_it('Pig latin is cool'))
# print(pig_it('Hello world !'))

"""Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
The function takes a name as its only argument, and returns one of the following strings:
name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings."""

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0] in 'rR' else f"{name} does not play banjo"
    # if name[0] in 'rR':
    #     return f"{name} plays banjo"
    # else:
    #     return f"{name} does not play banjo"

# print(are_you_playing_banjo("Roman"))
# print(are_you_playing_banjo(("roman")))
# print(are_you_playing_banjo("NotRoman"))

"""You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.
Examples:(Input --> Output)
121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square"""

def find_next_square(sq):
    if sq**0.5 == int(sq**0.5):
        while True:
            sq += 1
            if sq**0.5 == int(sq**0.5):
                return sq
    return -1

# print(find_next_square(121))
# print(find_next_square(625))
# print(find_next_square(114))