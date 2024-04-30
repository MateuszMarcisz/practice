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




