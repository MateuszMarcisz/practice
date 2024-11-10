cw = """Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.

In Roman numerals:

    1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
    2008 is written as 2000=MM, 8=VIII; or MMVIII.
    1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""


def solution(n):
    roman_numbers_table = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic_numbers_table = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    translated_string = ''

    for number in range(0, len(arabic_numbers_table)):
        while arabic_numbers_table[number] <= n:
            n -= arabic_numbers_table[number]
            translated_string += roman_numbers_table[number]

    return translated_string


# print(solution(1990))
# print(solution(2008))
# print(solution(1666))

# Alternative apporach that should be slightly faster (although we dont have big numbers so it doesnt matter)
def solution2(n):
    roman_numerals = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    translated_string = ''

    for roman, value in roman_numerals:
        while n >= value:
            n -= value
            translated_string += roman

    return translated_string


"""Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
Example:

"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      ->  400
"XC"      ->   90
"XL"      ->   40
"I"       ->    1

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""


def solution(roman: str) -> int:
    roman_translator = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    numbers = [roman_translator[char] for char in roman]
    result = 0

    for number in range(len(numbers) - 1):
        if numbers[number] < numbers[number + 1]:
            result -= numbers[number]
        else:
            result += numbers[number]
    result += numbers[len(numbers) - 1]

    return result


# print(solution("MM"))
# print(solution("MDCLXVI"))
# print(solution("M"))
# print(solution("CD"))
# print(solution("XC"))
# print(solution("V"))
# print(solution("MCMXC"))
# print(solution("MMVIII"))
# print(solution("I"))
# print(solution("IV"))
# print(solution("IX"))

"""Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

    1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
    2008 is written as 2000=MM, 8=VIII; or MMVIII
    1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
Examples

to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1

Help

+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+

"""


class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        roman_numbers_table = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        arabic_numbers_table = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        translated_string = ''

        for number in range(0, len(arabic_numbers_table)):
            while arabic_numbers_table[number] <= val:
                val -= arabic_numbers_table[number]
                translated_string += roman_numbers_table[number]

        return translated_string

    @staticmethod
    def from_roman(roman_num: str) -> int:
        roman_translator = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        numbers = [roman_translator[char] for char in roman_num]
        result = 0

        for number in range(len(numbers) - 1):
            if numbers[number] < numbers[number + 1]:
                result -= numbers[number]
            else:
                result += numbers[number]
        result += numbers[len(numbers) - 1]

        return result


"""We all know about Roman Numerals, and if not, here's a nice introduction kata. And if you were anything like me, you 'knew' that the numerals were not used for zeroes or fractions; but not so!

I learned something new today: the Romans did use fractions and there was even a glyph used to indicate zero.

So in this kata, we will be implementing Roman numerals and fractions.

Although the Romans used base 10 for their counting of units, they used base 12 for their fractions. The system used dots to represent twelfths, and an S to represent a half like so:

    1/12 = .
    2/12 = :
    3/12 = :.
    4/12 = ::
    5/12 = :.:
    6/12 = S
    7/12 = S.
    8/12 = S:
    9/12 = S:.
    10/12 = S::
    11/12 = S:.:
    12/12 = I (as usual)

Further, zero was represented by N
Kata

Complete the method that takes two parameters: an integer component in the range 0 to 5000 inclusive, and an optional fractional component in the range 0 to 11 inclusive.

You must return a string with the encoded value. Any input values outside the ranges given above should return "NaR" (i.e. "Not a Roman" :-)
Examples

roman_fractions(-12)     #=> "NaR"
roman_fractions(0, -1)   #=> "NaR"
roman_fractions(0, 12)   #=> "NaR"
roman_fractions(0)       #=> "N"
roman_fractions(0, 3)    #=> ":."
roman_fractions(1)       #=> "I"
roman_fractions(1, 0)    #=> "I"
roman_fractions(1, 5)    #=> "I:.:"
roman_fractions(1, 9)    #=> "IS:."
roman_fractions(1632, 2) #=> "MDCXXXII:"
roman_fractions(5000)    #=> "MMMMM"
roman_fractions(5001)    #=> "NaR"

"""


def roman_fractions(integer, fraction=None):
    if fraction:
        if fraction < 0 or fraction > 11:
            return 'NaR'
    if integer < 0 or integer > 5000:
        return 'NaR'

    roman_numbers_table = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic_numbers_table = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    translated_string = ''

    if integer == 0 and (fraction is None or fraction == 0):
        translated_string = 'N'
    else:
        for number in range(0, len(arabic_numbers_table)):
            while arabic_numbers_table[number] <= integer:
                integer -= arabic_numbers_table[number]
                translated_string += roman_numbers_table[number]

    fraction_to_symbol = {
        1 : '.',
        2 : ':',
        3 : ':.',
        4 : '::',
        5 : ':.:',
        6 : 'S',
        7 : 'S.',
        8 : 'S:',
        9 : 'S:.',
        10 : 'S::',
        11 : 'S:.:',
    }
    if fraction:
        translated_string += fraction_to_symbol[fraction]

    return translated_string

print(roman_fractions(-12))
print(roman_fractions(0, -1))
print(roman_fractions(0, 12))
print(roman_fractions(0))
print(roman_fractions(1))
print(roman_fractions(1, 5))
print(roman_fractions(1, 9))
print(roman_fractions(1632, 2))
print(roman_fractions(5000))
print(roman_fractions(5001))


