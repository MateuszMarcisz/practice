cw = """You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.
Example(Input1, Input2 --> Output):
6, 10 --> 32
3, 3 --> 9
Note: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.
"""


def area_or_perimeter(l, w):
    return l ** 2 if l == w else 2 * l + 2 * w


"""It's the academic year's end, fateful moment of your school report. 
The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
Return the average of the given array rounded down to its nearest integer.
The array will never be empty.
"""


def get_average(marks):
    return sum(marks) // len(marks)


"""Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
"""


def sum_mix(arr):
    return sum(int(x) for x in arr)


# print(sum_mix([9, 3, '7', '3']))


"""Write function RemoveExclamationMarks which removes all exclamation marks from a given string."""


def remove_exclamation_marks(s):
    return s.replace("!", "")


"""Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
If you liked this kata, check out part 2!!
"""


def expanded_form(num):
    num = str(num)
    lst = []
    for i in range(len(num)):
        lst.append(int(num[i] + '0' * len(num[i:-1])))
    return ' + '.join(str(x) for x in lst if x != 0)


# print(expanded_form(70304))
