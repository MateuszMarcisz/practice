cw = '''
Instructions
Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]
'''

def capitals(word):

    arr = []
    for i, el in enumerate(word):
        if el.isupper():
            arr.append(i)
    return arr

print(capitals("CodEWaRs"))
