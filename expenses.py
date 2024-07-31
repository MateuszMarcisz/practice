from datetime import datetime, timedelta
from statistics import median


# Zadanie
# Wyznacz medianę wydatków do pierwszej niedzieli (włącznie) każdego miesiąca (np. dla 2023-09 i 2023-10 są to dni 1, 2, 3 wrz i 1 paź).
# Należy zastosować rozwiązanie zgodnie z poniższym pseudokodem.


# expenses = {
#     "2023-01": {
#         "01": {
#             "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
#             "fuel": [2100.22]
#         },
#         "09": {
#             "food": [11.9],
#             "fuel": [190.22]
#         }
#     },
#     "2023-02": {
#         "03": {
#             "food": [5, 10.5, 3],
#             "fuel": [50]
#         },
#         "05": {
#             "food": [20],
#             "fuel": [30]
#         }
#     },
#     "2023-03": {
#         "07": {
#             "food": [20, 11.9, 30.20, 11.9]
#         },
#         "04": {
#             "food": [10.20, 11.50, 2.5],
#             "fuel": []
#         }
#     },
#     "2023-04": {
#         "02": {
#             "food": [15.30, 5.20],
#             "fuel": [25.75]
#         },
#         "06": {
#             "food": [7.80, 12.50],
#             "fuel": [60.45]
#         }
#     },
#     "2023-05": {
#         "27": {
#             "food": [8.60, 14.50],
#             "fuel": [55.20]
#         },
#         "19": {
#             "food": [8.60, 74.50],
#             "fuel": [55.20]
#         },
#         "09": {
#             "food": [89.60, 14.50],
#             "fuel": [559.20]
#         },
#         "01": {
#             "food": [23.50, 19.90],
#             "fuel": [75.80]
#         },
#         "05": {
#             "food": [16.40, 21.10],
#             "fuel": [85.30]
#         },
#         "07": {
#             "food": [8.60, 14.50],
#             "fuel": [55.20]
#         },
#     }
# }
#
# expenses = {
#     "2023-01": {
#         "01": {
#             "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
#             "fuel": [210.22]
#         },
#         "09": {
#             "food": [11.9],
#             "fuel": [190.22]
#         }
#     },
#     "2023-03": {
#         "07": {
#             "food": [20, 11.9, 30.20, 11.9]
#         },
#         "04": {
#             "food": [10.20, 11.50, 2.5],
#             "fuel": []
#         }
#     },
#     "2023-04": {}
# }


def solution(expenses):
    expenses_till_first_sundays = []

    for month in expenses:
        year, month_number = map(int, month.split('-'))
        month_expenses = []
        days_in_month = sorted(expenses[month].keys())

        first_day_of_month = datetime(year, month_number, 1)
        first_sunday_of_month = first_day_of_month
        while first_sunday_of_month.weekday() != 6:
            first_sunday_of_month += timedelta(days=1)
        first_sunday_day = first_sunday_of_month.day

        for day_str in days_in_month:
            day = int(day_str)
            if day > first_sunday_day:
                break
            for category in expenses[month][day_str]:
                month_expenses.extend(expenses[month][day_str][category])
        expenses_till_first_sundays.extend(month_expenses)

    if expenses_till_first_sundays:
        # print(expenses_till_first_sundays)
        return median(expenses_till_first_sundays)
    else:
        return None


# print(solution(expenses))

# print(sorted(['01', '02', '003']))
