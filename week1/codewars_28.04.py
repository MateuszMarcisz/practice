codewars2804 = """Given two integers a and b, which can be positive or negative,
find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.
Note: a and b are not ordered!
Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)"""


def get_sum(a, b):
    if a == b:
        return a
    sum_ = 0
    lst = sorted([a, b])
    for i in range(lst[0], lst[1] + 1):
        sum_ += i
    return sum_


# I should have just used min and max in the range instead of sorting


# print(get_sum(1, 2))
# print(get_sum(2, 1))
# print(get_sum(1, -1))
# print(get_sum(6, 0))
# print(get_sum(2, 2))

"""Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
i.e. friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output."""


def friend(x):
    return [i for i in x if len(i) == 4]


# print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
# print(friend(["Ryan", "Kieran", "Mark"]))

"""Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, 
containing distinct letters - each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" """  # this description could be better

def longest(a1, a2):
    c = [x for x in set(a1+a2)]
    return "".join(sorted(c))

#     return "".join(sorted(set(a1 + a2)))
# sorted will transform set into list!


# print(longest(a1 = "xyaabbbccccdefww", a2 = "xxxxyyyyabklmopq"))