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

"""The goal of this exercise is to convert a string to a new string where each character in the new string is "(" 
if that character appears only once in the original string, or ")" 
if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.
Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" """


def duplicate_encode(word):
    word = word.lower()
    wordz = ''.join("(" if word.count(i) == 1 else ")" for i in word)
    # wordz = ""
    # for i in word:
    #     if word.count(i) == 1:
    #         wordz += "("
    #     else:
    #         wordz += ")"
    return wordz


# print(duplicate_encode("din"))
# print(duplicate_encode("recede"))
# print(duplicate_encode("Success"))
# print(duplicate_encode("(( @"))

"""You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones -- 
everytime you press the button it sends you an array of one-letter strings representing directions to walk 
(eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction)
 and you know it takes you one minute to traverse one city block, 
 so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
 (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
Note:
you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
It will never give you an empty array (that's not a walk, that's standing still!)."""


def is_valid_walk(walk):
    return True if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(
        walk) == 10 else False


# print(is_valid_walk(['n', 's', 'w', 'e', 'n', 's', 'w', 'e', 'n', 's']))
"""Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.
For example (Input --> Output):
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)"""


def persistence(n):
    count = 0
    while n >= 10:
        new_n = 1
        for number in str(n):
            new_n *= int(number)
        n = new_n
        count += 1
    return count

    # n = str(n)
    # count = 0
    # while len(n) > 1:
    #     for i in range(len(n)-1):
    #         count += 1
    #         if "0" in n:
    #             return count
    #         n = "".join([f"{i}*" for i in n])[:-1]
    #         n = eval(n)
    #         n = str(n)
    # else:
    #     return count
    # numberz = ""
    # for i in n:
    #     numberz += f"{i}*"
    # while len(numberz) > 1:
    #     return eval(numberz)



# print(persistence(337874))
# print(persistence(4))
# print(persistence(11))
# print(persistence(39))
# print(persistence(1584))
# print(persistence(999))
# print(persistence(191805))
