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