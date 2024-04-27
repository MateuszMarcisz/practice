zad1 = """Write a function that takes an integer as input,
and returns the number of bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case"""


def count_bits(n):
    return bin(n).count('1')


# print(count_bits(1234))

"""You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer.
Write a method that takes the array as an argument and returns this "outlier" N.
Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)"""


def find_outlier(integers):
    # that is too much, but I had to do it haha
    return [x for x in integers if x % 2 == 0][0] if len([x for x in integers if x % 2 == 0]) == 1 else \
    [x for x in integers if x % 2 == 1][0]
    # even = [x for x in integers if x % 2 == 0]
    # odd = [x for x in integers if x % 2 == 1]
    # return even[0] if len(even) == 1 else odd[0]


# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

"""Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    zeros = lst.count(0)
    lst = [x for x in lst if x != 0]
    for i in range(zeros):
        lst.append(0)
    return lst


# print(move_zeros([1, 0, 1, 2, 0, 1, 3, 0, 0, 12, 166]))
