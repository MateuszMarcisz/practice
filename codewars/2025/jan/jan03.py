cw = '''
Create a function that will return true if the input is in the following date time format 01-09-2016 01:20 and false if it is not.

This Kata has been inspired by the Regular Expressions chapter from the book Eloquent JavaScript.
'''

# from datetime import datetime
#
#
# def date_checker(date):
#     try:
#         datetime.strptime(date, '%d-%m-%Y %H:%M')
#         return True
#     except ValueError:
#         return False


'''The example above didn't work as the kata is completely misleading.
The date itself doesn't have to be valid so checking for the datetime will not work. 
Random bs tests checks for month 47th or hours like 97:78, etc. 
'''

import re


def date_checker(date):
    pattern = r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$'
    return bool(re.match(pattern, date))


# print(date_checker("01-09-2016 01:20"))
# print(date_checker("01-09-2016 01;20"))
# print(date_checker("01-09_2016 01:20"))
# print(date_checker("01-09 2016 01:20"))
# print(date_checker("01-09 2016"))

'''
Your dad doesn't really get punctuation, and he's always putting extra commas in when he posts.
You can tolerate the run-on sentences, as he does actually talk like that, but those extra commas have to go!

Write a function that takes a string as an argument and returns a string with the extraneous commas removed.
The returned string should not end with a comma or have any trailing whitespace.
'''
import re


def dad_filter(string):
    return re.sub(r',+', ',' , string).strip().strip(',')

print(dad_filter("all this,,,, used to be trees,,,,,,"))
print(dad_filter("Dead or alive,,,, you're coming with me,,,   "))