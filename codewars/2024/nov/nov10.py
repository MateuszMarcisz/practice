cw = '''Your task is to write a function which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
'''


def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))


# print(sequence_sum(2, 5, 2))
# print(sequence_sum(2, 6, 2))
# print(sequence_sum(2, 2, 2))
# print(sequence_sum(6, 4, 2))


'''Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
'''

import math


def round_to_next5(n):
    return math.ceil(n / 5) * 5


#
# print(round_to_next5(0), 0)
# print(round_to_next5(2), 5)
# print(round_to_next5(3), 5)
# print(round_to_next5(5), 5)
# print(round_to_next5(7), 10)
# print(round_to_next5(12), 15)
# print(round_to_next5(666), 670)
# print(round_to_next5(-1), 0)
# print(round_to_next5(-5), -5)


'''Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
'''


def solution(nums):
    # return [] if nums is None else sorted(nums)
    return sorted(nums) if nums else []


print(solution([1, 2, 3, 10, 5]))
print(solution(None))
