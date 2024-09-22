may20th = """Given an array of integers, return a new array with each value doubled.
For example:
[1, 2, 3] --> [2, 4, 6]
"""


def maps(a):
    return [x * 2 for x in a]
    # return list(map(lambda x: x * 2, a))


# print(maps([1, 2, 3, 4, 5, 6]))
"""Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
"""


def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2


# print(lovefunc(1, 4))
# print(lovefunc(2, 4))

# done multpiple of simple ones in cw directly

"""Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
"""


def find_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)


# print(find_average([1, 2, 3]))

"""Well met with Fibonacci bigger brother, AKA Tribonacci.
As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)
If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata"""


def tribonacci(signature, n):
    if n == 0:
        return []
    else:
        tribarray = signature
        for i in range(3, n):
            tribarray.append(tribarray[i - 1] + tribarray[i - 2] + tribarray[i - 3])
        return tribarray[:n]


# print(tribonacci([1, 1, 1], 10))
# print(tribonacci([0, 0, 1], 10))
# print(tribonacci([0, 1, 1], 10))
# print(tribonacci([1, 0, 0], 10))
# print(tribonacci([1, 2, 3], 10))
# print(tribonacci([300, 200, 100], 0))
# print(tribonacci([0.5, 0.5, 0.5], 30))

"""Create function fib that returns n'th element of Fibonacci sequence (classic programming task)."""


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    else:
        lst = [1, 1]
        for i in range(2, n):
            lst.append(lst[i - 1] + lst[i - 2])
        return lst[n - 1]


# print(fibonacci(70))
# print(fibonacci(6))
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))


"""Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
Create a function which translates a given DNA string into RNA.
For example:
"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.
"""


def dna_to_rna(dna):
    # trans_table = str.maketrans('ATCG', 'AUCG')
    # return dna.translate(trans_table)
    return dna.replace('T', 'U')


# print(dna_to_rna('GCAT'))

"""The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""


def rgb(r, g, b):
    varz = [r, g, b]
    for i in range(len(varz)):
        if varz[i] < 0:
            varz[i] = 0
        if varz[i] > 255:
            varz[i] = 255
    r_hexa = hex(varz[0]).upper()
    g_hexa = hex(varz[1]).upper()
    b_hexa = hex(varz[2]).upper()
    return r_hexa[2:].zfill(2) + g_hexa[2:].zfill(2) + b_hexa[2:].zfill(2)


# print(rgb(-90, -90, 999))


"""Create a function with two arguments that will return an array of the first n multiples of x.
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array or list ( depending on language ).
Examples
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
"""


def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


# print(count_by(3, 5))

"""If you can't sleep, just count sheep!!
Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers."""


def count_sheep(n):
    return "".join([f'{x} sheep...' for x in range(1, n + 1)])


# print(count_sheep(3))
