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
    return int('0b'+a, 2)


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

def delete_nth(order,max_e):
    lst = []
    for i in order:
        if lst.count(i) < max_e:
            lst.append(i)
    return lst


print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))