cw = """Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: https://leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)
"""


def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i, j


# it could be done also like this:
# return next(((i, j) for i in range(len(numbers)) for j in range(i + 1, len(numbers)) if numbers[i] + numbers[j] == target), None)

# print(two_sum([1, 2, 3], 4))
# print(two_sum([3, 2, 4], 6))
# print(two_sum([3, 2, 4], 7))


"""You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)
Examples

[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3

"""


def stray(arr):
    return next(i for i in arr if arr.count(i) == 1)
    # for i in arr:
    #     if arr.count(i) == 1:
    #         return i


# print(stray([1, 1, 2]))
# print(stray([17, 17, 3, 17, 17, 17, 17]))
# print(stray([122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 622633, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848, 122848]))

