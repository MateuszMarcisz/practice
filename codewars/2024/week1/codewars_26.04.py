import string

codewars_26_04 = """Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2"""


def digital_root(n):
    while len(str(sum([int(i) for i in str(n)]))) > 1:
        n = sum([int(i) for i in str(n)])
        return sum([int(i) for i in str(sum([int(i) for i in str(n)]))])
    else:
        return sum([int(i) for i in str(n)])


# print(digital_root(493193768768))
# print(digital_root(942))
# print(digital_root(16))

# lst = [[1,2,3,4,5,6],[9,3,4,5,6,7,8]]
# for x in lst:
#     for y in x:
#         print(y)
#
# print([x for x in lst])
# print([y for x in lst for y in x])

"""Jack really likes his number five:
the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:
  3 -->    15  (  3 * 5¹)
 10 -->   250  ( 10 * 5²)
200 --> 25000  (200 * 5³)
  0 -->     0  (  0 * 5¹)
 -3 -->   -15  ( -3 * 5¹)"""


def multiply(n):
    return n * 5 ** (len(str(n))) if n > -1 else n * 5 ** (len(str(n)) - 1)


# print(multiply(-3))
# print(multiply(3))
# print(multiply(10))
# print(multiply(200))

# """Given a logarithm base X and two values A and B, return a sum of logratihms with the base X:
# log⁡XA+log⁡XB \log_XA + \log_XB logX​A+logX​B."""

import math


def logs(x, a, b):
    return math.log(a * b, x)


#
# print(logs(10, 1000, 10))

# 1000 = 10^3,
# log10(1000) = 3

"""Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.
Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""


def create_phone_number(n):
    # z = []
    # for num in n[:3]:
    #     z.append(str(num))
    # return "".join(z)
    return f'({"".join(str(num) for num in n[:3])}) {"".join(str(num) for num in n[3:6])}-{"".join(str(num) for num in n[6:])}'
    # return f"{"".join(str(num) for num in n[:3]}, n[3:6], n[6:]"
    # return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# """Make me slow! Calling makeMeSlow() should take at least 7 seconds."""
# def make_me_slow():
#     for i in range(9999999999999999999999999999999999999999999999999999999999):
#         print(i)
"""#Make them bark
You have been hired by a dogbreeder to write a program to keep record of his dogs.
You've already made a constructor Dog, so no one has to hardcode every puppy.
The work seems to be done. It's high time to collect the payment.
..hold on! The dogbreeder says he wont pay you, until he can make every dog object .bark().
Even the ones already done with your constructor. 
"Every dog barks" he says. He also refuses to rewrite them, lazy as he is.
You can't even count how much objects that bastard client of yours already made.
He has a lot of dogs, and none of them can .bark().
Can you solve this problem, or will you let this client outsmart you for good?
Practical info:
    The .bark() method of a dog should return the string 'Woof!'.
    The contructor you made (it is preloaded) looks like this:
class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age
Hint: A friend of yours just told you about how javascript handles classes diferently from other programming languages. 
He couldn't stop ranting about "prototypes", or something like that. Maybe that could help you..."""

# class Dog(object):
#     def __init__(self, name, breed, sex, age):
#         self.name = name
#         self.breed = breed
#         self.sex = sex
#         self.age = age
#         self.bark = self.bark
#
#     @staticmethod
#     def bark():
#         return "Woof!"
#
#
# zeus = Dog('Zeus', 'Dobermann', 'male', '4')
# print(zeus.bark(), "Woof!")
# print(Dog.bark())

"""Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.
Please use the following function names:
addition = add
multiply = multiply
division = divide (both integer and float divisions are accepted)
modulus = mod
exponential = exponent
subtraction = subt"""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def subt(a, b):
    return a - b


"""Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


# print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

"""Your goal in this kata is to implement a difference function, 
which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]"""


def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)
    return a
    # return [x for x in a if x not in b]


# print(array_diff([1, 2, 2, 2, 3], [2, 1]))
# print(array_diff([1, 2], [1]))


"""Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice"""


def duplicate_count(text):
    text = text.lower()
    count = 0
    for i in set(text):
        if text.count(i) > 1:
            count += 1
    return count


# print(duplicate_count("indivisibility"))
# print(duplicate_count("ABBA"))
# print(duplicate_count("Indivisibilities"))

"""Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013).
Jaden is also known for some of his philosophy that he delivers via Twitter. 
When writing on Twitter, he is known for almost always capitalizing every word. 
For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.
Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real" """


def to_jaden_case(string):
    return " ".join([x.capitalize() for x in string.split()])


# return string.title() for some reasons capitalize T in aren't


# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

"""Usually when you buy something, you're asked whether your credit card number, phone number
or answer to your most secret question is still correct. 
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
Your task is to write a function maskify, which changes all but the last four characters into '#'.
Examples (input --> output):
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""
// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!" """


def maskify(cc):
    return '#' * len(cc[:-4]) + cc[-4:]

# print(maskify("Nananananananananananananananana Batman!"))
