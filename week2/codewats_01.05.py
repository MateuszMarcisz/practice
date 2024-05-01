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