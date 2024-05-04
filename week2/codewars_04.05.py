codewars0405 = """Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  "" """


def order(sentence):
    lst = sentence.split()
    order = []
    for i in range(len(lst)):
        for word in lst:
            if str(i + 1) in word:
                order.append(word)
    return " ".join(order)


#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))  # -.-

# print(order("is2 Thi1s T4est 3a"))
# print(order("4of Fo1r pe6ople g3ood th5e the2"))
# print(order(""))

"""There is an array with some numbers. All numbers are equal except for one. Try to find it!
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance."""


def find_uniq(arr):
    if arr[0] != arr[1] and arr[0] != arr[2]:
        return arr[0]
    for i in range(len((arr))):
        if arr[i] != arr[i + 1]:
            return arr[i + 1]


# def find_uniq(arr):
#     a = sorted(arr)
#     return a[0] if a[0] != a[1] else a[-1]

# print(find_uniq([1, 1, 1, 2, 1, 1]))
# print(find_uniq([0, 0, 0.55, 0, 0]))
# print(find_uniq([2, 0, 0, 0, 0]))

"""Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length and false in any other case.
(In this case, all triangles must have surface greater than 0 to be accepted).
Examples:
Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false """


def is_triangle(a, b, c):
    if a <= 0 and b <= 0 and c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# print(is_triangle(7, 2, 2))

def binary_array_to_number(arr):
    a = "".join(str(num) for num in arr)
    return int('0b' + a, 2)


# print(binary_array_to_number([1, 0, 1, 1]))
# print(binary_array_to_number([1, 1, 1, 1]))
# print(binary_array_to_number([0, 1, 1, 0]))

def reverse_words(text):
    return ' '.join([i[::-1] for i in text.split(' ')])


# print(reverse_words("This is    an example!"))

def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


# print(odd_or_even([0]))
# print(odd_or_even([0, 1, 4]))
# print(odd_or_even([0, -1, 5]))
# print(odd_or_even([]))

"""Enough is enough!

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been,
and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions,
since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.
He tells them that he will only sit for the session if they show the same motif at most N times.
Luckily, Alice and Bob are able to encode the motif as a number. 
Can you help them to remove numbers such that their list contains each number only up to N times,
without changing the order?
Task
Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, 
and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].
"""


def delete_nth(order, max_e):
    lst = []
    for i in order:
        if lst.count(i) < max_e:
            lst.append(i)
    return lst


# print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))

"""Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.
Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Requirements
    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
    NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
Example
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    # lst = [i for i in range(1, num+1) if num % i == 0]
    # return True if len(lst) < 3 else False


# print(is_prime(9))
# print(is_prime(2))
# print(is_prime(-1))
# print(is_prime(73))
# print(is_prime(75))
# print(is_prime(41))
# print(is_prime(5099))
"""ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
"""


def rot13(message):
    trans_alphabet = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                   'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM')
    return message.translate(trans_alphabet)


# print(rot13("Test"))

"""The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(s):
    counting = {}
    for i in s:
        if i not in counting:
            counting[i] = s.count(i)
    return counting

# print(count('aba'))
# print(count('abc'))
# print(count('abcaaab'))
# print(count(''))

"""The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!
Here's the deal:
    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""
def generate_hashtag(s):
    if not s:
        return False
    lst = ''.join(s.title().split())
    return '#'+lst if len(lst) < 140 else False

print(generate_hashtag("Hello there thanks for trying my Kata"))
print(generate_hashtag('cokolwiek'))
print(generate_hashtag(''))

