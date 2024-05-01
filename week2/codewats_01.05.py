import string

codewars0105 = """KATA6
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"The_Stealth-Warrior" gets converted to "TheStealthWarrior" """


def to_camel_case(text):
    camel_case = []
    for i, j in enumerate(text):
        camel_case.append(j.capitalize()) if text[i - 1] in ('-', '_') else camel_case.append(j)
    remover = str.maketrans('', '', '-_')
    return ''.join(camel_case).translate(remover)
    # return "".join(camel_case).replace('_', '').replace('-', '')


# print(to_camel_case("the-stealth-warrior"))
# print(to_camel_case("The_Stealth_Warrior"))
# print(to_camel_case("The_Stealth-Warrior"))


"""KATA7In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which,
for the sake of simplicity, are named with letters from a to m.
The colors used by the printer are recorded in a control string. 
For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a,
 four times color b, one time color h then one time color a...
Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g.
aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
You have to write a function printer_error which given a string will return the error rate
of the printer as a string representing a rational whose numerator is the number of errors
and the denominator the length of the control string.
Don't reduce this fraction to a simpler expression.
The string has a length greater or equal to one and contains only letters from ato z.
Examples:
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"
s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
"""

def printer_error(s):
    count = sum(1 for i in s if i not in 'abcdefghijklm')
    # count = 0
    # for i in s:
    #     if i not in 'abcdefghijklm':
    #         count += 1
    return f'{count}/{len(s)}'


# print(printer_error("aaabbbbhaijjjm"))
# print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))

"""ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false"""
def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4, 6)


"""Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']"""

def solution(s):
    lst = []
    while len(s) > 1:
        lst.append(s[:2])
        s = s[2:]
    if len(s) == 1:
        lst.append(f"{s}_")
    return lst


# print(solution('abdec'))

"""Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
You can find some examples in the test fixtures.
"""
def make_readable(seconds):
    hh = (seconds // 3600)
    if len(str(hh)) == 1:
        hh = f'0{hh}'
    mm = (seconds // 60) % 60
    if len(str(mm)) == 1:
        mm = f'0{mm}'
    ss = seconds % 60
    if len(str(ss)) == 1:
        ss = f'0{ss}'
    return f'{hh}:{mm}:{ss}'


# print(make_readable(59))
# print(make_readable(66))
# print(make_readable(3599))
# print(make_readable(3600))
# print(make_readable(86400))
# print(make_readable(359999))
