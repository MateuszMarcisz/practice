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

