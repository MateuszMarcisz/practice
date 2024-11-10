from _curses import window

cw = """Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

"""


def number(lines):
    return [f'{i + 1}: {x}' for i, x in enumerate(lines)]


# print(number(['a', 'b', 'c']))


"""A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing)?
Three conditions must be met for a valid experiment:

    Float parameter "h" in meters must be greater than 0
    Float parameter "bounce" must be greater than 0 and less than 1
    Float parameter "window" must be less than h.

If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
Note:

The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.
Examples:

- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled).
"""


def bouncing_ball(h, bounce, window):
    if h <= 0 or window >= h or bounce <= 0 or bounce >= 1:
        return -1
    counter = 1
    h *= bounce
    while h > window:
        h *= bounce
        counter += 2
    return counter


# print(bouncing_ball(3, 0.66, 1.5))
# print(bouncing_ball(3, 1, 1.5))
# print(bouncing_ball(30, 0.66, 1.5))
# print(bouncing_ball(30, 0.75, 1.5))


"""Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
Example:

["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""


def remove_every_other(my_list):
    return [x for x in my_list[::2]]


# print(remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep", "beep", 'sreeep']))

"""Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
Example 1:

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]
Example 2:

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []
Notes:

    Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
    In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
    Beware: In some languages r must be without duplicates.

"""


def in_array(array1, array2):
    string2 = " ".join(array2)
    # lst = []
    # for i in array1:
    #     if i in string2:
    #         lst.append(i)
    return sorted(set(i for i in array1 if i in string2))
    # return sorted(set(lst))

# print(in_array(["arp", "live", "strong", "arp"], ["lively", "alive", "harp", "sharp", "armstrong"]))
# print(in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))
# print(in_array(["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))
