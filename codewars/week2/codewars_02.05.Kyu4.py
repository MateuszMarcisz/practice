kyu4 = """Your task in order to complete this Kata is to write a function which formats a duration,
given as a number of seconds, in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
It is much easier to understand with an example:
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.
Note that spaces are important.
Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, 
a positive integer and one of the valid units of time, separated by a space.
The unit of time is used in plural if the integer is greater than 1.
The components are separated by a comma and a space (", "). 
Except the last component, which is separated by " and ", just like it would be written in English.
A more significant units of time will occur before than a least significant one.
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
A component will not appear at all if its value happens to be zero.
 Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
A unit of time must be used "as much as possible". It means that the function should not return 61 seconds,
but 1 minute and 1 second instead.
Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
"""


def format_duration(seconds):
    # sorry for the potato code, it's my first month of programming
    time = []

    y = seconds // 31536000
    if y == 0:
        pass
    elif y == 1:
        fy = '1 year'
        time.append(fy)
    else:
        fy = f'{y} years'
        time.append(fy)

    d = (seconds // 86400) % 365
    if d == 0:
        pass
    elif d == 1:
        fd = '1 day'
        time.append(fd)
    else:
        fd = f'{d} days'
        time.append(fd)

    h = (seconds // 3600) % 24
    if h == 0:
        pass
    elif h == 1:
        fh = '1 hour'
        time.append(fh)
    else:
        fh = f'{h} hours'
        time.append(fh)

    m = (seconds // 60) % 60
    if m == 0:
        pass
    elif m == 1:
        fm = '1 minute'
        time.append(fm)
    else:
        fm = f'{m} minutes'
        time.append(fm)

    s = seconds % 60
    if s == 0:
        pass
    elif s == 1:
        fs = '1 second'
        time.append(fs)
    else:
        fs = f'{s} seconds'
        time.append(fs)

    if len(time) == 0:
        return 'now'
    elif len(time) == 1:
        return time[0]
    elif len(time) == 2:
        return time[0] + ' and ' + time[1]
    else:
        return ', '.join(time[:-1]) + ' and ' + time[-1]

# someone had rly nice one
# times = [("year", 365 * 24 * 60 * 60),
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]
#
# def format_duration(seconds):
#
#     if not seconds:
#         return "now"
#
#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)
#
#         seconds = seconds % secs
#
#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

# print(format_duration(0))
# print(format_duration(1))
# print(format_duration(60))
# print(format_duration(62))
# print(format_duration(120))
# print(format_duration(1220))
# print(format_duration(3600))
# print(format_duration(3662))
# print(format_duration(86400))
# print(format_duration(86400*2))
# print(format_duration(86400*3 + 99))
# print(format_duration(15731080))
# print(format_duration(253374061))
# print(format_duration(132030240))
# print(format_duration(31536000))
# print(format_duration(31536002))
# print(format_duration(31536000*2))
