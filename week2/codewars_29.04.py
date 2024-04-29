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
