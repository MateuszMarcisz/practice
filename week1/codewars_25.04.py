import string


def sum_array(a):
    return sum(a)


#
# print(sum_array([1, 5.2, 4, 0, -1]))
# print(sum_array([3,5,6]))
# print(sum_array([]))

"""A square of squares

You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.
Task

Given an integral number, determine if it's a square number:

    In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages."""


def is_square(n):
    return False if n < 0 else (True if (n ** 0.5).is_integer() else False)


# print(is_square(5))
# print(is_square(9))

"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
Example: (Input --> Output)
"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

"""


def isIsogram(n):
    if n.isalpha():
        n = n.lower()
        z = []
        x = set()
        for i in n:
            z.append(i)
            x.add(i)
        return sorted(z) == sorted(list(x))
    else:
        return False


#
# print(isIsogram("moose"))
# print(isIsogram("abcdefghijkl"))
"""Make a function "add" that will be able to sum elements of list continuously and return a new list of sums.
For example:
add [1,2,3,4,5] == [1, 3, 6, 10, 15], because it's calculated like 
this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]
"""


def add(lst):
    new_lst = []
    sum_ = 0
    for i in lst:
        sum_ += i
        new_lst.append(sum_)
    return new_lst


#
# print(add([1, 2, 3, 4, 5]))
# print(add([5, 3, 9, 8]))
"""Oh no! Ghosts have reportedly swarmed the city. It's your job to get rid of them and save the day!
In this kata, strings represent buildings while whitespaces within those strings represent ghosts.
So what are you waiting for? Return the building(string) without any ghosts(whitespaces)!
Example:
"Sky scra per" -> "Skyscraper"
If the building contains no ghosts, return the string:
"You just wanted my autograph didn't you?"
"""


def ghostbusters(building):
    if " " not in building:
        return "You just wanted my autograph didn't you?"
    else:
        return "".join(building.split())


#
# print(ghostbusters("asdas asd asd"))

"""This time no story, no theory. The examples below show you how to write function accum:
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z."""


def accum(st):
    str = ""
    j = 0
    for i in st:
        j += 1
        str += (i.upper() + i.lower() * (j - 1)) + "-"
    return str[:-1]


# print(accum("acdeEzYYA"))
"""Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.
The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""


def xo(s):
    s = s.lower()
    if not "x" in s and not "o" in s:
        return True
    else:
        os = 0
        xs = 0
        for i in s:
            if i == "x":
                xs += 1
            if i == "o":
                os += 1
    return True if os == xs else False


# def xo(s): # można używać też count
#     s = s.lower()
#     return s.count('x') == s.count('o')

# print(xo("zpzpzpp"))
# print(xo('ooxx'))
# print(xo('xooox'))
def invert(lst):
    # lst1 = []
    # for i in lst:
    #     lst1.append(-i)
    # return lst1
    return [-x for x in lst]


# print(invert([0, 1, 3, 5, -7, 6, 4, -9]))
"""Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:
    "I love you"
    "a little"
    "a lot"
    "passionately"
    "madly"
    "not at all"
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.
"""


def how_much_i_love_you(nb_petals):
    z = nb_petals // 6
    if nb_petals > 6:
        nb_petals = nb_petals - (6 * z)
    lst = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return lst[nb_petals - 1]

    # to jest zdecydowanie ładniejsze poniżej:
    # return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]

    # print(how_much_i_love_you(1))
    # print(how_much_i_love_you(2))
    # print(how_much_i_love_you(10))
    # print(how_much_i_love_you(20))


def monkey_count(n):
    return [x for x in range(1, n + 1)]
    # lst = []
    # for i in range(1, n+1):
    #     lst.append(i)
    # return lst
    # return list(range(1, n + 1)) # to jest najelegantsze


# print(monkey_count(6))
"""All of the animals are having a feast! Each animal is bringing one dish. 
There is just one rule: the dish must start and end with the same letters as the animal's name. 
For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.
Write a function feast that takes the animal's name and dish as arguments and returns true or false
to indicate whether the beast is allowed to bring the dish to the feast.
Assume that beast and dish are always lowercase strings, and that each has at least two letters. 
beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. 
They will not contain numerals"""


def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


# print(feast("blue heron", "bln"))

"""Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false"""


def solution(text, ending):
    return text[len(text) - len(ending):] == ending
    # return text.endswith(ending)


# print(solution('abc', 'bc'))

"""Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" 
for the development and functioning of living organisms.
If you want to know more: http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
Your function receives one side of the DNA (string, except for Haskell); 
you need to return the other complementary side. 
DNA strand is never empty or there is no DNA at all (again, except for Haskell).
More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
Example: (input --> output)
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""


def DNA_strand(dna):
    # dct = {
    #     "A": "T",
    #     "T": "A",
    #     "C": "G",
    #     "G": "C"
    # }
    # complementary_dna = []
    # for i in dna:
    #     complementary_dna.append(dct[i])
    # return "".join(complementary_dna)
    return dna.translate(str.maketrans('ATCG', 'TAGC'))


# print(DNA_strand("ATTGC"))

"""Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types."""


def find_short(s):
    # s = s.split()
    # l = float('inf')
    # for i in s:
    #     if len(i) < l:
    #         l = len(i)
    # return l
    return min([len(i) for i in s.split()])
    # return min(map(len,s.split()))


# print(find_short("losowe słowa wpisałem aby było co liczyć"))

"""Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
Examples:
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd)."""


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


# print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""


def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# print(likes([]))
# print(likes(["Peter"]))
# print(likes(["Jacob", "Alex"]))
# print(likes(["Max", "John", "Mark"]))
# print(likes(["Alex", "Jacob", "Mark", "Max"]))
"""Write a function that takes in a string of one or more words, and returns the same string,
but with all words that have five or more letters reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.
Examples:
"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test" """


def spin_words(sentence):
    return " ".join([x[::-1] if len(x) > 4 else x for x in sentence.split()])
    # wierd = []
    # for i in sentence.split():
    #     if len(i) > 4:
    #         wierd.append(i[::-1])
    #     else:
    #         wierd.append(i)
    # return " ".join(wierd)


# print(spin_words("Hey fellow warriors"))
