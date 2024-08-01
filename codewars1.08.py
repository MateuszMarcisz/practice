cw = """Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ", 
  "*****"
]

And a tower with 6 floors looks like this:
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
"""


# def tower_builder(n_floors):
#     tower = []
#     for i in range(n_floors):
#         tower.append(" " * ((n_floors - i) - 1) + (2 * i + 1) * '*' + " " * ((n_floors - i) - 1))
#
#     return tower
#
#
# print(tower_builder(3))

def tower_builder(n_floors):
    return [(" " * ((n_floors - i) - 1) + (2 * i + 1) * '*' + " " * ((n_floors - i) - 1)) for i in range(n_floors)]


# print(tower_builder(1))
# print(tower_builder(2))
# print(tower_builder(3))
# print(tower_builder(4))

# this one was cool:
# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


"""At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.

More generally given parameters:

p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

the function nb_year should return n number of entire years needed to get a population greater or equal to p.

aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
"""


def nb_year(p0, percent, aug, p):
    years = 0
    while p > p0:
        p0 = int(p0 + (p0 * percent / 100) + aug)
        years += 1
    return years


# print(nb_year(1500, 5, 100, 5000))
# print(nb_year(1500000, 2.5, 10000, 2000000))
# print(nb_year(1500000, 0.25, 1000, 2000000))


"""Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:
case 	return
name equals owner 	'Hello boss'
otherwise 	'Hello guest'"""


def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


"This kata is about multiplying a given number by eight if it is an even number and by nine otherwise."


def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


"""Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
Examples (Input -> Output)

* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5

Notes

    You may consider that there will not be any empty arrays/vectors.

"""


def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)


"""Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

"""

"""After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
"""


def rental_car_cost(d):
    return 40 * d - 50 if d >= 7 else 40 * d - 20 if d >= 3 else 40 * d


# print(rental_car_cost(1))
# print(rental_car_cost(4))
# print(rental_car_cost(8))

# this is how you can write it shorter:
# def rental_car_cost(d):
#     return d * 40 - (d > 2) * 20 - (d > 6) * 30


def grow(arr):
    a = 1
    for i in range(len(arr)):
        a *= arr[i]
    return a

# print(grow([1, 2, 3, 4]))

# the same can be achieve using math.prod(), so it would be just return math.prod(arrr)
