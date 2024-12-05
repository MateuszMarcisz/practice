cw = '''
Description:
The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age,  oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

For example (Input --> Output):

[1, 2, 10, 8] --> [8, 10]
[1, 5, 87, 45, 8, 8] --> [45, 87]
[1, 3, 10, 0]) --> [3, 10]
'''


def two_oldest_ages(ages):
    return sorted(ages)[-2:]


# print(two_oldest_ages([1, 2, 10, 8]))

'''
Description:
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is:

"  *\n ***\n*****\n ***\n  *\n"
'''


def diamond(n):
    if n % 2 == 0 or n < 0:
        return None

    diamond = ''
    for i in range(1, n + 1, 2):
        diamond += ' ' * ((n - i) // 2) + '*' * i + '\n'

    for i in range(n - 2, 0, -2):
        diamond += ' ' * ((n - i) // 2) + '*' * i + '\n'

    return diamond


# print(diamond(0))
# print(diamond(4))
# print(diamond(1))
# print(diamond(3))
# print(diamond(5))
