cw = '''
Given an array containing only integers, add all the elements and return the binary equivalent of that sum.

If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.

Note: The sum of an empty array is zero.

[1, 2]      --> "11"
[1, "a", 2] --> false / False (depending on the language)
'''

def arr2bin(arr):
    if not all(isinstance(_, int) for _ in arr):
        return False
    return bin(sum(arr))[2:]


# print(arr2bin([1, 2, 3]))
# print(arr2bin([1,2,3,4,5]))
# print(arr2bin([1,2,-1,-2]))
# print(arr2bin([1,'a',2]))

'''
Description:
Given an array of positive integers, replace every element with the least greater element to its right. If there is no greater element to its right, replace it with -1. For instance, given the array

[8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28],

the desired output is

[18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1].

Your task is to create a function that takes in an array as its argument, manipulates the array as described above, then return the resulting array.

Note: Return a new array, rather than modifying the passed array.
'''


def array_manip(array):
    new_arr = []
    for idx, num in enumerate(array):
        greater_elements = [n for n in array[idx + 1:] if n > num]

        if greater_elements:
            new_arr.append(min(greater_elements))
        else:
            new_arr.append(-1)

    return new_arr



print(array_manip([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]))