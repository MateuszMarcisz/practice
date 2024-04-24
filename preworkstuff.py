# ex1
from random import randint


def stars():
    rows = 5
    columns = 10
    for row in range(rows):
        print('*' * columns)


#stars()

# ex2

def pinetree():
    size = randint(3, 9)
    for i in range(size+1):
        print('*' * i)


# pinetree()
