# for sql current date in sql server:

# WHERE CAST(order_date AS DATE) = CAST(GETDATE() AS DATE)

# for sql previous day date in sql server:

# WHERE CAST(xxx AS DATE) = CAST(DATEADD(DAY, -1, GETDATE()) AS DATE);


# in other sql dbs just xxx = CURRENT_DATE
# and for previous days:
# WHERE order_date = CURRENT_DATE - INTERVAL '1 day'; postgre
# WHERE order_date = CURDATE() - INTERVAL 1 DAY; mysql
# WHERE order_date = CURRENT_DATE - 1; sqlite


# examples for the only working days:


# POSTGRE

# SELECT *
# FROM orders
# WHERE order_date =
#     CASE
#         WHEN EXTRACT(DOW FROM CURRENT_DATE) = 1 THEN CURRENT_DATE - INTERVAL '3 days' -- Monday: go back to Friday
#         ELSE CURRENT_DATE - INTERVAL '1 day' -- any other day: go back to the previous day
#     END;


# SQLite

# SELECT *
# # FROM orders
# # WHERE order_date =
# #     CASE
# #         WHEN strftime('%w', CURRENT_DATE) = '1' THEN CURRENT_DATE - 3 -- Monday: go back to Friday
# #         ELSE CURRENT_DATE - 1 -- any other day: go back to the previous day
# #     END;


# SQL server

# SELECT *
# FROM orders
# WHERE order_date =
#     CASE
#         WHEN DATEPART(WEEKDAY, GETDATE()) = 2 THEN CAST(DATEADD(DAY, -3, GETDATE()) AS DATE) -- Monday: go back to Friday
#         ELSE CAST(DATEADD(DAY, -1, GETDATE()) AS DATE) -- any other day: go back to the previous day
#     END;