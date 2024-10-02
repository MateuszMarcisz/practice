from operator import index

cw = """Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does, he wants to know how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a desired sum of money 'D'.

The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly. After paying taxes 'T' for the year the new sum is re-invested.

Note to Tax: not the invested principal is taxed, but only the year's accrued interest

Example:

  Let P be the Principal = 1000.00      
  Let I be the Interest Rate = 0.05      
  Let T be the Tax Rate = 0.18      
  Let D be the Desired Sum = 1100.00


After 1st Year -->
  P = 1041.00
After 2nd Year -->
  P = 1083.86
After 3rd Year -->
  P = 1128.30

Thus Mr. Scrooge has to wait for 3 years for the initial principal to amount to the desired sum.

Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.

Assumption: Assume that Desired Principal 'D' is always greater than the initial principal. However it is best to take into consideration that if Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.
"""


def calculate_years(principal, interest, tax, desired):
    if principal >= desired:
        return 0
    interest_taxed = interest * (1 - tax)
    years = 0
    while principal < desired:
        principal += principal * interest_taxed
        years += 1
    return years

#     better solution:
#     if principal >= desired:
#         return 0
#     effective_rate = interest * (1 - tax)
#     years = math.log(desired / principal) / math.log(1 + effective_rate)
#     return math.ceil(years)



# print(calculate_years(100, 0.05, 0.05, 120))
# print(calculate_years(1000, 0.05, 0.18, 1100))

"""Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.
"""

from collections import Counter

def first_non_repeating_letter(s):

    # low_s = s.lower()
    # for letter in low_s:
    #     if low_s.count(letter) == 1:
    #         idx = low_s.index(letter)
    #         return s[idx]
    # return ""

    # the best solution:
    counts = Counter(s.lower())
    for letter in s:
        if counts[letter.lower()] == 1:
            return letter
    return ""



print(first_non_repeating_letter('moonmEn'))