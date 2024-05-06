codewars0605 = """The museum of incredibly dull things
The museum of incredibly dull things wants to get rid of some exhibits.
Miriam, the interior architect, comes up with a plan to remove the most boring exhibits.
She gives them a rating, and then removes the one with the lowest rating.
However, just as she finished rating all exhibits, she's off to an important fair,
so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one.Fair enough.
Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with the lowest index.
If you get an empty array/list, return an empty array/list.
Don't change the order of the elements that are left.
Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]"""


def remove_smallest(numbers):
    if not numbers:
        return numbers
    srambers = numbers[0:-1]
    srambers.remove(min(srambers))
    return srambers


# print(remove_smallest([5, 3, 2, 1, 4]))

"""Story

Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.
Task
Write a function that returns both the minimum and maximum number of the given list/array.
Examples (Input --> Output)
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]
Remarks
All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.
"""


def min_max(lst):
    return [min(lst), max(lst)]


# print(min_max([1, 2, 3, 4, 5]))

"""Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime" """

def divisors(integer):
    lst = [i for i in range(1, integer+1) if integer % i == 0]
    # for i in range(1,integer+1):
    #     if integer % i == 0:
    #         lst.append(i)
    return lst[1:-1] if len(lst) > 2 else f"{integer} is prime"


# print(divisors(12))
# print(divisors(25))
# print(divisors(13))