cw = """Complete the solution so that it reverses all of the words within the string passed in.
Words are separated by exactly one space and there are no leading or trailing spaces.
Example(Input --> Output):
"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
"""


def reverse_words(s):
    return ' '.join(s.split()[::-1])


# print(reverse_words("The greatest victory is that which requires no battle"))


"""Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
    Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.
Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
"""


def count_smileys(arr):
    count = 0
    if len(arr) == 0:
        return count
    for i in range(len(arr)):
        if len(arr[i]) == 2:
            if (';' in arr[i][0] or ':' in arr[i][0]) and (')' in arr[i][1] or 'D' in arr[i][1]):
                count += 1
        if len(arr[i]) == 3:
            if (';' in arr[i][0] or ':' in arr[i][0]) and (')' in arr[i][2] or 'D' in arr[i][2]) and (
                    '-' in arr[i][1] or '~' in arr[i][1]):
                count += 1
    return count


# print(count_smileys([':)', ';(', ';}', ':-D']))
# print(count_smileys([';D', ':-(', ':-)', ';~)']))
# print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

"""nice solutions:
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
    
or:   
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count
"""

"""I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.
P.S. Each array includes only integer numbers. Output is a number too.
"""


def array_plus_array(arr1, arr2):
    return sum(arr1 + arr2)


# print(array_plus_array([1, 2, 3], [4, 5, 6]))
# print(array_plus_array([-1, -2, -3], [-4, -5, -6]))
# print(array_plus_array([0, 0, 0], [4, 5, 6]))

"""Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
For example: ["3:1", "2:2", "0:1", ...]
Points are awarded for each match as follows:
    if x > y: 3 points (win)
    if x < y: 0 points (loss)
    if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.
Notes:
    our team always plays 10 matches in the championship
    0 <= x <= 4
    0 <= y <= 4
"""


def points(games):
    pts = 0
    for game in games:
        if game[0] == game[2]:
            pts += 1
        if game[0] > game[2]:
            pts += 3
    return pts


# print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))
# print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4']))


"""Task
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.
Mind the input validation.
Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
"""


def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 2 else 0


# print(sum_array([3, 5]))
# print(sum_array([6, 2, 1, 8, 10]))
# print(sum_array([-6, 20, -1, 10, -12]))
# print(sum_array([None]))
# print(sum_array([]))
