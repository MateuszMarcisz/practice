lst = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13]]
print(lst)
lst1 = []
for x in lst:
    for y in x:
        lst1.append(y)

print(lst1)

lst2 = [y for x in lst for y in x]

print(lst2)

tup = (1, 2, 3, 4, 5)
print(tup)
a, b, c, d, e = tup
print(a, b, c, d, e)
a, b, *c = tup
print(a, b, c)

tup1 = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11))
print(tup1)

tup2 = tuple()
for x in tup1:
    for y in x:
        tup2 += (y,)

print(tup2)

tup3 = tuple(y for x in tup1 for y in x)
print(tup3)
