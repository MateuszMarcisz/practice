cw = """Thanks for checking out my kata - in the below problem - the highest n can be is 200.
Example summation of a number - summation of the number 5 1+2+3+4+5 = 15 summation of the number 6 1+2+3+4+5+6 = 21
You are sat with two frogs on a log, Chris and Tom. They are arguing about who ate the most flies (Poor flies, but what you going to do!). Chris says "I ate the summation of n number of flies!".
Tom replies "Take half the number you ate then round it down and work out the summation of that, that is how many I ate"!
Cat then hops onto the log looking pleased with herself "Well, I ate the summation of both your dinners combined." Loz who came late to this meeting of amphibians is very confused, he asks "So how many did each of you eat?"
Write a function called frogContest which returns a string "Chris ate {number} flies, Tom ate {number} flies and Cat ate {number} flies"
{number} is the integer value of the amount of flies eaten by each.
"""


def frog_contest(flies):
    chris = sum(x for x in range(1, flies + 1))
    tom = sum(x for x in range(1, chris // 2 + 1))
    cat = sum(x for x in range(1, chris + tom + 1))
    return f"Chris ate {chris} flies, Tom ate {tom} flies and Cat ate {cat} flies"


# print(frog_contest(5))

"""Create a function that returns the sum of the digits formed from the first and last digits, all the way to the center of the number."""


def closing_in_sum(n):
    n = str(n)
    # lst = [x for x in n]
    # lst1 = sum(int(n[i]+n[-i-1]) for i in range((len(n))//2))
    # lst2 = sum([int(n[i]+n[-i-1]) for i in range((len(n))//2)]+[int(n[len(n)//2])])
    return sum(int(n[i]+n[-i-1]) for i in range((len(n))//2)) if len(n) % 2 == 0 else sum([int(n[i]+n[-i-1]) for i in range((len(n))//2)]+[int(n[len(n)//2])])


# print(closing_in_sum(1039))
# print(closing_in_sum(2520))
# print(closing_in_sum(121))
# print(closing_in_sum(5332824166496569))
