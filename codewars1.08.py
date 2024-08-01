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


print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(4))


# this one was cool:
# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
