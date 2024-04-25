def sum_array(a):
    return sum(a)


#
# print(sum_array([1, 5.2, 4, 0, -1]))
# print(sum_array([3,5,6]))
# print(sum_array([]))

"""A square of squares

You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.
Task

Given an integral number, determine if it's a square number:

    In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages."""


def is_square(n):
    return False if n < 0 else (True if (n ** 0.5).is_integer() else False)


# print(is_square(5))
# print(is_square(9))

"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
Example: (Input --> Output)
"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

"""


def isIsogram(n):
    if n.isalpha():
        n = n.lower()
        z = []
        x = set()
        for i in n:
            z.append(i)
            x.add(i)
        return sorted(z) == sorted(list(x))
    else:
        return False


#
# print(isIsogram("moose"))
# print(isIsogram("abcdefghijkl"))
"""Make a function "add" that will be able to sum elements of list continuously and return a new list of sums.
For example:
add [1,2,3,4,5] == [1, 3, 6, 10, 15], because it's calculated like 
this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]
"""


def add(lst):
    new_lst = []
    sum_ = 0
    for i in lst:
        sum_ += i
        new_lst.append(sum_)
    return new_lst

#
# print(add([1, 2, 3, 4, 5]))
# print(add([5, 3, 9, 8]))
"""Oh no! Ghosts have reportedly swarmed the city. It's your job to get rid of them and save the day!
In this kata, strings represent buildings while whitespaces within those strings represent ghosts.
So what are you waiting for? Return the building(string) without any ghosts(whitespaces)!
Example:
"Sky scra per" -> "Skyscraper"
If the building contains no ghosts, return the string:
"You just wanted my autograph didn't you?"
"""
def ghostbusters(building):
    if " " not in building:
        return "You just wanted my autograph didn't you?"
    else:
        return "".join(building.split())

#
# print(ghostbusters("asdas asd asd"))

"""This time no story, no theory. The examples below show you how to write function accum:
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z."""
def accum(st):
    str = ""
    j = 0
    for i in st:
        j = j + 1
        str += (i.upper() + i.lower()*(j-1)) + "-"
    return str[:-1]


# print(accum("acdeEzYYA"))

