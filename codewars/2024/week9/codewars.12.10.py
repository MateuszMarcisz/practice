cw = '''Count the number of divisors of a positive integer n.

Random tests go up to n = 500000, but fixed tests go higher.
Examples (input --> output)

4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30

Note you should only return a number, the count of divisors. The numbers between parentheses are shown only for you to see which numbers are counted in each case.
'''


def divisors(n):
    # return sum(1 for number in range(1, n // 2 + 1) if n % number == 0) + 1

    # no point of returning 1 if condition is true, we can return true and sum will count as 1
    return sum(n % number == 0 for number in range(1, n // 2 + 1)) + 1


# this one is the optimized version:
# def divisors(n):
#     count = 0
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             count += 1
#             if i != n // i:
#                 count += 1
#     return count


# print(divisors(4))
# print(divisors(5))
# print(divisors(12))
# print(divisors(30))


'''Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.
'''


def break_chocolate(n, m):
    # return 0 if (n == 0 or m == 0 ) else (n * m) - 1
    return max(n * m - 1, 0)


# print(break_chocolate(5, 5))
# print(break_chocolate(4, 8))


'''Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Implement the function taking n and d as parameters and returning this count.
Examples:

n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25'''


def nb_dig(n, d):
    squares = [number ** 2 for number in range(n + 1)]
    return sum(str(x).count(str(d)) for x in squares)

print(nb_dig(10, 1))
print(nb_dig(25, 1))
print(nb_dig(25, 2))
