import string

cw = """Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
"""


def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    result = []
    plus = 0
    neg = 0
    for i in arr:
        if i > 0:
            plus += 1
        if i < 0:
            neg += i
    result.extend([plus, neg])
    return result


# print(count_positives_sum_negatives([]))
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))


"""Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.
Examples

"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

"""

# def valid_braces(s):
#     matching_brace = {')': '(', ']': '[', '}': '{'}
#     stack = []
#     for char in s:
#         if char in matching_brace.values():
#             stack.append(char)
#         elif char in matching_brace:
#             if stack and stack[-1] == matching_brace[char]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             return False
#     return not stack
#
#
# print(valid_braces(("(){}[]")))
# print(valid_braces(("([{}])")))
# print(valid_braces(("(}")))

"""
Task
Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).
1+41​+71​+101​+131​+161​+

You will need to figure out the rule of the series to complete this.
Rules

    You need to round the answer to 2 decimal places and return it as String.

    If the given value is 0 then it should return "0.00".

    You will only be given Natural Numbers as arguments.

Examples (Input --> Output)

n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

"""


def series_sum(n):
    if n == 0:
        return "0.00"
    lst = []
    for i in range(1, n + 1):
        lst.append(1 / (3 * i - 2))
    return f"{sum(lst):.2f}"


print(series_sum(0))
print(series_sum(1))
print(series_sum(2))
print(series_sum(5))
print(series_sum(3))
print(series_sum(6))
print(series_sum(11))
