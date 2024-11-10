cw = """Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered.

Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

"""

from collections import Counter

def scramble(s1, s2):
    # for i in s2:
    #     if i in s1:
    #         s1 = s1.replace(i, '', 1)
    #     else:
    #         return False
    # return True

    # s1_lst = list(s1)
    # for i in s2:
    #     if i in s1_lst:
    #         s1_lst.remove(i)
    #     else:
    #         return False
    # return True

    s1_lst = list(s1)
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)

    for character, counter in counter_s2.items():
        if counter > counter_s1[character]:
            return False
    return True




print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))


