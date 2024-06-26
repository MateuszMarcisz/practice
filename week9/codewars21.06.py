cw = """Clock shows h hours, m minutes and s seconds after midnight.
Your task is to write a function which returns the time since midnight in milliseconds.Example:
h = 0
m = 1
s = 1
result = 61000
Input constraints:
    0 <= h <= 23
    0 <= m <= 59
    0 <= s <= 59
"""


def past(h, m, s):
    return s * 1000 + m * 60000 + h * 3600000


# print(past(0,1,1))
# print(past(1,1,1))
# print(past(0,0,0))


"""There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.
You receive an array with your peers' test scores. Now calculate the average and compare your score!
Return true if you're better, else false!
Note:
Your points are not included in the array of your class's points. Do not forget them when calculating the average score!"""


def better_than_average(class_points, your_points):
    class_points.append(your_points)
    return True if sum(class_points) / len(class_points) < your_points else False


# print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
# print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))


"""You will get an array of numbers.
Every preceding number is smaller than the one following it.
Some numbers will be missing, for instance:
[-3,-2,1,5] //missing numbers are: -1,0,2,3,4
Your task is to return an array of those missing numbers:
[-1,0,2,3,4]
"""


def find_missing_numbers(arr):
    if arr:
        full_arr = [x for x in range(arr[0], arr[-1] + 1)]
        return [x for x in full_arr if x not in arr]
    else:
        return []


# print(find_missing_numbers([-3, -2, 1, 4]))
# print(find_missing_numbers([0]))
# print(find_missing_numbers([]))


"""Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
For example, the score of abad is 8 (1 + 2 + 1 + 4).
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    if not x:
        return ''
    else:
        alphabet = "_abcdefghijklmnopqrstuvwxyz"
        lst = x.split()
        points_lst = []
        for word in lst:
            points = 0
            for letter in word:
                points += alphabet.index(letter)
            points_lst.append(points)
        # return points_lst
        return lst[points_lst.index(max(points_lst))]


# print(high('man i need a taxi up to ubud'))
# print(high('take me to semynak'))
# print(high('what time are we climbing up the volcano'))
# print(high('oabpvf yxa qxdokwdt wpuovkem kkcvrx rbcjgf kxb mlaz bkhf npw xiakslg dynjhxsfkg gmkg uvfefg orpf hmye'))

