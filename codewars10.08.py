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


"""Don't give me five!

In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12

The result may contain fives. ;-)
The start number will always be smaller than the end number. Both numbers can be also negative!

I'm very curious for your solutions and the way you solve it. Maybe someone of you will find an easy pure mathematics solution.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
"""


def dont_give_me_five(start, end):
    return len([i for i in range(start, end + 1) if '5' not in str(i)])


# print(dont_give_me_five(1, 9))
# print(dont_give_me_five(4, 17))
# print(dont_give_me_five(91, 163))

"""The number 898989 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 89=81+9289 = 8^1 + 9^289=81+92

The next number in having this property is 135135135:

See this property again: 135=11+32+53135 = 1^1 + 3^2 + 5^3135=11+32+53
Task

We need a function to collect these numbers, that may receive two integers aaa, bbb that defines the range [a,b][a, b][a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.
Examples

Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

If there are no numbers of this kind in the range [a,b][a, b][a,b] the function should output an empty list.

90, 100 --> []

Enjoy it!!
"""


def sum_dig_pow(a, b):
    lst = []
    for i in range(a, b + 1):
        compare = []
        for j in range(1, len(str(i)) + 1):
            compare.append(int(str(i)[j - 1]) ** j)
            if i == sum(compare):
                lst.append(i)
    return lst

# print(sum_dig_pow(1, 10))
# print(sum_dig_pow(2, 10))
# print(sum_dig_pow(2, 100))
# print(sum_dig_pow(95, 1000))
