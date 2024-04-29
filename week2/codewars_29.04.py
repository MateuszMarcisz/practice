codewars_2904 = """Implement the function unique_in_order which takes as argument a sequence
and returns a list of items without any elements with the same value next to each other
and preserving the original order of elements.
For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]"""


def unique_in_order(sequence):
    lst = []
    count = 1
    for i in sequence:
        if count == len(sequence):
            lst.append(i)
            break
        lst.append(i) if sequence[count - 1] != sequence[count] else None
        count += 1
    return lst


# someone had nicer solution:
# res = []
# for item in sequence:
#     if len(res) == 0 or item != res[-1]:
#         res.append(item)
# return res
# print(unique_in_order('AAAABBBCCDAABBB'))
# print(unique_in_order('ABBCcAD'))
# print(unique_in_order([1, 2, 2, 3, 3]))
# print(unique_in_order((1, 2, 2, 3, 3)))

"""The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
They would like your help with an application form that will tell prospective members which category they will be placed
To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.
Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]"""


def open_or_senior(data):
    return ['Senior' if i[0] > 54 and i[1] > 7 else 'Open' for i in data]
    # lst = []
    # for i in data:
    #     if i[0] > 54 and i[1] > 7:
    #         lst.append('Senior')
    #     else:
    #         lst.append('Open')
    # return lst


# print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))

"""Can you find the needle in the haystack?
Write a function findNeedle() that takes an array full of junk but containing one "needle"
After your function finds the needle it should return a message (as a string) that says:
"found the needle at position " plus the index it found the needle, so:
Example(Input --> Output)
["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" """


def find_needle(haystack):
    # for i in haystack:
    #     if i == "needle":
    #         return haystack.index(i)

    return f"found the needle at position {haystack.index('needle')}"


# print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.
Courtesy of projecteuler.net (Problem 1)"""


def solution(number):
    return sum(i for i in range(1, number) if i % 3 == 0 or i % 5 == 0) if number > 0 else 0
    # if number < 0:
    #     return 0
    # else:
    #     numbers = []
    #     for i in range(1, number):
    #         if i % 3 == 0 or i % 5 == 0:
    #             numbers.append(i)
    # return sum(numbers)


# print(solution(10))
"""In this kata you will create a function that takes a list of non-negative integers
and strings and returns a new list with the strings filtered out.
Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]"""


def filter_list(l):
    return [i for i in l if isinstance(i, int)]
    # lst = []
    # for i in l:
    #     lst.append(i) if isinstance(i, int) else None
    # return lst


# print(filter_list([1,2,'aasf','1','123',123]))


"""Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).
For example,
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]"""


def count_sheeps(sheep):
    # TODO May the force be with you
    return sheep.count(True)


# print(count_sheeps([True, True, True, False,
#                     True, True, True, True,
#                     True, False, True, False,
#                     True, False, False, True,
#                     True, True, True, True,
#                     False, False, True, True]))
