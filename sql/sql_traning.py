from sql.db_config import connect_to_db


def connect_and_query(query):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # Execute and handle the query
        cursor.execute(query)

        # Fetch and print results if it's a SELECT query
        # if query.strip().lower().startswith("select"):
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No results found.")

        # Commit changes for modifying queries
        connection.commit()

    except Exception as error:
        print("Error:", error)

    finally:
        # Clean up by closing the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    # query = """
    # CREATE TABLE users (
    #     id SERIAL PRIMARY KEY,
    #     username VARCHAR(50) NOT NULL,
    #     email VARCHAR(100) NOT NULL,
    #     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    # );
    # """
    # connect_and_query(query)

    # show all public tables
    #     query = "SELECT * FROM information_schema.tables WHERE table_schema = 'public';"
    #     connect_and_query(query)

    # create some users for testing
    #     query = """
    #     INSERT INTO users (username, email)
    #     VALUES
    #         ('alice', 'alice@example.com'),
    #         ('bob', 'bob@example.com'),
    #         ('carol', 'carol@example.com'),
    #         ('mati', 'mati@example.com'),
    #         ('aga', 'aga@example.com');
    #     """
    #     connect_and_query(query)

    # show all users
    # query = "SELECT * FROM users;"
    # connect_and_query(query)

    # create table Products

    # query = """
    # CREATE TABLE products (
    # id serial PRIMARY KEY,
    # name VARCHAR(255) NOT NULL,
    # price DECIMAL(10,2) NOT NULL,
    # stock INT DEFAULT 0
    # )
    # """
    # connect_and_query(query)
    #
    # # create table orders
    #
    # query = """
    # CREATE TABLE orders (
    # id serial PRIMARY KEY,
    # user_id INT NOT NULL,
    # order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    # FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    # )
    # """
    # connect_and_query(query)
    #
    # #create table Order Details
    #
    # query = """
    # CREATE TABLE order_details (
    # id serial PRIMARY KEY,
    # order_id INT NOT NULL,
    # product_id INT NOT NULL,
    # quantity INT NOT NULL,
    # price DECIMAL(10,2) NOT NULL,
    # FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
    # FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
    # )
    # """
    # connect_and_query(query)
#     # TODO: 1. List all users who have placed at least one order.
#     query = '''SELECT DISTINCT user_id from orders'''
#     connect_and_query(query)
#     query = '''
#     SELECT DISTINCT username from users
#     JOIN orders ON orders.user_id = users.id
#     '''
#     connect_and_query(query)
#
# # TODO: 2. Retrieve all orders placed by a user with a specific user_id (e.g., user_id = 13).
#     query = '''
#     SELECT * FROM orders WHERE user_id = 13;
#     '''
#     connect_and_query(query)
#
# # TODO: 3. Display the total quantity ordered for each product by product_id.
#     query = '''
# SELECT product_id, SUM(quantity)
# FROM order_details
# GROUP BY product_id
# ORDER BY product_id
#     '''
#     connect_and_query(query)
# TODO: 4. Find the total amount spent per user (sum of price * quantity for each order).
#     query = '''
#     SELECT
# 	-- order_details.order_id,
# 	STRING_AGG(DISTINCT orders.id::TEXT, ', ') AS order_ids,
# 	orders.user_id,
# 	users.username,
# 	SUM(order_details.quantity * order_details.price) as total_amount_spent
# FROM
# 	order_details
# JOIN
# 	orders
# ON
# 	order_details.order_id = orders.id
# JOIN
# 	users
# ON
# 	orders.user_id = users.id
# GROUP BY
# 	-- order_details.order_id,
# 	orders.user_id,
# 	users.username
# ORDER BY username
#     '''
#     connect_and_query(query)

# TODO: 5. Identify the most purchased product by quantity (highest total quantity across all orders).
#     query = '''
#     SELECT
# 	products.name,
# 	SUM(order_details.quantity) as total_quantity
# FROM order_details
# JOIN products
# ON order_details.product_id = products.id
# GROUP BY products.name
# ORDER BY total_quantity DESC
# LIMIT 1
#     '''
#     connect_and_query(query)

# TODO: 6. List the total number of orders placed on a specific date (e.g., '2023-01-01').

#     query = '''
# SELECT COUNT(*)
# FROM orders
# WHERE DATE(order_date) = '2024-11-15';
#     '''
#     connect_and_query(query)

# TODO: 7. Join users and orders to display each user's name alongside their order_id.
#     query = '''
#     SELECT orders.id, users.username
# FROM orders
# JOIN users
# ON orders.user_id = users.id;
#     '''
#     connect_and_query(query)

# TODO: 8. Find the details of all products ordered by a specific user (e.g., user_id = 29).
#     query = '''
# SELECT order_details.*, orders.user_id
# FROM order_details
# JOIN
# orders
# ON order_details.order_id = orders.id
# WHERE orders.user_id = 29;
#     '''
#     connect_and_query(query)

# TODO: 9. Retrieve the total spending per order, including the order_id and user_id (sum of price * quantity).
#     query = '''
# SELECT order_id, orders.user_id, SUM(price * quantity) AS total_per_order
# FROM order_details
# JOIN orders ON order_details.order_id = orders.id
# GROUP BY order_id, orders.user_id
# ORDER BY order_id;
#     '''
#     connect_and_query(query)

# TODO: 10. Identify users who have placed more than 2 orders.

#     query = '''
#     SELECT user_id, users.username, COUNT(orders.id) as number_of_orders
# FROM orders
# JOIN users ON user_id = users.id
# GROUP BY user_id, users.username
# HAVING COUNT(orders.id) > 2;
#     '''
#     connect_and_query(query)

# TODO: 11. Find users who have never placed an order (i.e., no order_id associated with them).

# '''    -- SELECT users.id, username
# -- FROM users
# -- WHERE users.id NOT IN (
# -- SELECT user_id FROM orders
# -- )
# '''
#
# '''
# -- SELECT users.id, username
# -- FROM users
# -- LEFT JOIN orders ON users.id = orders.user_id
# -- WHERE orders.user_id IS NULL;'''

#     query = '''
# SELECT users.id, username
# FROM users
# WHERE NOT EXISTS (
#     SELECT 1
#     FROM orders
#     WHERE orders.user_id = users.id
# );'''
#     connect_and_query(query)

# TODO: 12. List all products purchased by users who have ordered products with a price greater than $300.
#     query = '''
#     WITH users_high_value AS (
#     SELECT DISTINCT orders.user_id
#     FROM order_details
#     JOIN orders ON order_details.order_id = orders.id
#     WHERE order_details.price > 300)
#
#     SELECT DISTINCT products.id, products.name, products.price
#     FROM products
#     JOIN order_details ON products.id = order_details.product_id
#     JOIN orders ON order_details.order_id = orders.id
#     WHERE orders.user_id IN (
#     SELECT user_id FROM users_high_value);'''


#     query = '''
#     SELECT DISTINCT products.id, products.name, products.price
# FROM products
# JOIN order_details ON products.id = order_details.product_id
# JOIN orders ON order_details.order_id = orders.id
# WHERE orders.user_id IN (
#     SELECT DISTINCT orders.user_id
#     FROM order_details
#     JOIN orders ON order_details.order_id = orders.id
#     WHERE order_details.price > 300
# );
#     '''

    # connect_and_query(query)

# TODO: 13. Retrieve the top 5 users by total spending (sum of price * quantity).

#     query = '''
#     SELECT users.username AS user, SUM(price*quantity) AS total
# FROM order_details
# JOIN orders ON order_details.order_id = orders.id
# JOIN users ON orders.user_id = users.id
# GROUP BY users.username
# ORDER BY total DESC
# LIMIT 5
#     '''
#     query = '''
#     SELECT users.username AS user,
#        SUM(COALESCE(order_details.price, 0) * COALESCE(order_details.quantity, 0)) AS total
# FROM order_details
# JOIN orders ON order_details.order_id = orders.id
# JOIN users ON orders.user_id = users.id
# GROUP BY users.username
# ORDER BY total DESC
# LIMIT 5;
#     '''
#
    # connect_and_query(query)


# TODO: 14. Find all orders where the total spending exceeds the average order total.

#     query = '''
#     SELECT order_id, SUM(quantity * price) AS total
# FROM order_details
# GROUP BY order_id
# HAVING SUM(quantity * price) > (
#     SELECT AVG(quantity * price)
#     FROM order_details
# )
# ORDER BY total;
#     '''
#     connect_and_query(query)

# TODO: 15. Identify the product(s) with the highest total revenue (sum of price * quantity for each product).

#     query = '''
# SELECT product_id, products.name, SUM(order_details.price * order_details.quantity) AS total
# FROM order_details
# JOIN products ON product_id = products.id
# GROUP BY product_id, products.name
# ORDER BY total DESC
# LIMIT 1
#     '''

#     query = '''
#     WITH revenue_table AS (
#     SELECT product_id, products.name, SUM(order_details.price * order_details.quantity) AS total
#     FROM order_details
#     JOIN products ON product_id = products.id
#     GROUP BY product_id, products.name
# )
# SELECT *
# FROM revenue_table
# WHERE total = (SELECT MAX(total) FROM revenue_table);
#     '''

#     query = '''
#     SELECT product_id, products.name, SUM(order_details.price * order_details.quantity) AS total
# FROM order_details
# JOIN products ON product_id = products.id
# GROUP BY product_id, products.name
# HAVING SUM(order_details.price * order_details.quantity) = (
#     SELECT MAX(total)
#     FROM (
#         SELECT product_id, SUM(price * quantity) AS total
#         FROM order_details
#         GROUP BY product_id
#     ) AS subquery
# );
#     '''
#
#     connect_and_query(query)

# TODO: 16. Update the order_date for a specific order (e.g., order_id = 5) to a new date.

# specific date:
#     query = '''UPDATE orders
# SET order_date = '2024-07-29 15:45:30.123456'
# WHERE id = 5;
# '''
#     current time

#     query = '''UPDATE orders
# SET order_date = CURRENT_TIMESTAMP
# WHERE id = 5;
#
# SELECT * FROM orders
# WHERE id = 5;
# '''
#     connect_and_query(query)

# TODO: 17. Increase the price of all products by 10% for orders placed by a specific user_id (e.g., user_id = 50).

#     query = '''
# UPDATE order_details
# SET price = price * 1.1
# FROM orders
# WHERE order_details.order_id = orders.id
# AND orders.user_id = 11;
# SELECT *
# FROM orders
# JOIN order_details
# ON order_details.order_id = orders.id
# WHERE user_id = 11
#
#     '''
#     connect_and_query(query)


# TODO: 18. Delete all orders placed by a specific user (e.g., user_id = 32).

#     query = '''
# DELETE
# FROM orders
# WHERE user_id = 32
#     '''
#     connect_and_query(query)

# TODO: 19. Remove all products from order_details where the quantity is less than 2.
#     query = '''
# DELETE
# FROM order_details
# WHERE quantity < 2
#     '''
#     connect_and_query(query)

# more tasks:
# TODO: 1. Find the User with Most Orders
# Retrieve the user who has placed the highest number of orders and the total number of orders they placed.

# The one below sucks, as you know how many are tied for first in order to use LIMIT to only get the users with most orders
#     query = '''
#
# SELECT users.username, COUNT(users.username) AS number_of_orders
# FROM orders
# JOIN users
# ON users.id = orders.user_id
# GROUP BY users.username
# ORDER BY number_of_orders DESC
#     '''
#     connect_and_query(query)

#     query = '''
#     WITH order_count_table AS (
# 	SELECT users.username, COUNT(users.username) AS number_of_orders --COUNT(*) should be more efficient
# 	FROM orders
# 	JOIN users
# 	ON users.id = orders.user_id
# 	GROUP BY users.username
# )
#
# SELECT *
# FROM order_count_table
# WHERE number_of_orders = (SELECT MAX(number_of_orders) FROM order_count_table)
#     '''
#     connect_and_query(query)


# TODO: 2. List All Products with No Stock Left
# Display the products where the `stock` is 0.

#     query = '''
#     SELECT * FROM public.products
# WHERE stock = 0
#     '''
#     connect_and_query(query)

# TODO: 3. Orders with Only One Product
# Retrieve all orders that contain only one product in the `order_details` table.
#     query = '''
# SELECT order_id, COUNT(order_id) AS number_of_products
# FROM order_details
# GROUP BY order_id
# HAVING COUNT(order_id) = 1
#     '''
#     connect_and_query(query)
#
# # TODO: 4. Top-Selling Product
# Identify the product that has been ordered the most times (by total quantity).
#     but this one is lame as this doesnt account for ties
#     query = '''
#     SELECT SUM(quantity) AS number_of_products, product_id
# FROM order_details
# JOIN products
# ON product_id = products.id
# GROUP BY product_id
# ORDER BY number_of_products DESC
# LIMIT 1
#     '''

    # this one here is much better:

#     query = '''
#     WITH product_quantities_table AS
# (SELECT SUM(quantity) AS number_of_products, product_id
# FROM order_details
# JOIN products
# ON product_id = products.id
# GROUP BY product_id
# )
#
# SELECT *
# FROM product_quantities_table
# WHERE number_of_products = (SELECT MAX(number_of_products) FROM product_quantities_table)
#     '''
#
#     connect_and_query(query)

# TODO: 5. Users Who Haven’t Placed Any Orders
# Retrieve all users who have not placed any orders yet.

#     query = '''
#     SELECT users.username
# FROM users
# LEFT JOIN orders
# ON users.id = orders.user_id
# WHERE orders.user_id IS NULL
#     '''
#     query = '''
#     SELECT users.username
# FROM users
# WHERE users.id NOT IN (
# 	SELECT user_id
# 	FROM orders
# );
#     '''
#
#     connect_and_query(query)

# TODO: 6. Average Order Value Per User
# Calculate the average total value of all orders for each user.

#     query = '''
# WITH total_per_order AS (
# 	SELECT order_details.order_id, SUM(quantity*price) AS order_total
# FROM order_details
# GROUP BY order_id
# 	)
#
# SELECT AVG(total_per_order.order_total) as average_order_value, orders.user_id
# FROM total_per_order
# JOIN orders
# ON total_per_order.order_id = orders.id
# GROUP BY orders.user_id
# ORDER BY user_id;
# '''
#     connect_and_query(query)

# TODO: 7. Orders Above Average Price
# Retrieve orders where the total value (sum of `price * quantity` in `order_details`) is above the average order value.

#     query = '''
# SELECT order_id, SUM(price * quantity) AS total
# FROM order_details
# GROUP BY order_id
# HAVING SUM(price * quantity) > (
#     SELECT AVG(total_per_order)
#     FROM (
#         SELECT SUM(price * quantity) AS total_per_order
#         FROM order_details
#         GROUP BY order_id
#     ) AS subquery
# )
# ORDER BY total DESC;
#     '''
#     connect_and_query(query)

# TODO: 8. Products Ordered by a Specific User
# For a given `user_id` (e.g., `user_id = 6`), retrieve all the products they have ordered, along with the total quantity.
#     query = '''
#     SELECT product_id, SUM(quantity), orders.user_id
# FROM order_details
# JOIN orders
# ON order_details.order_id = orders.id
# WHERE orders.user_id = 6
# GROUP BY product_id, orders.user_id
#     '''
#     connect_and_query(query)

# TODO: 9. Restock Alert
# List all products with a stock level below a certain threshold (e.g., `stock < 5`).

# TODO: 10. Find Duplicate User Emails
# Check if there are any duplicate email addresses in the `users` table.

# TODO: 11. Most Recent Order for Each User
# Retrieve the most recent order (by `order_date`) for each user.

# TODO: 12. Total Spending Per User
# For each user, calculate their total spending (sum of `price * quantity`).

# TODO: 13. Highest Revenue Products
# Identify the top 3 products that have generated the most revenue (sum of `price * quantity`).

# TODO: 14. Delete Old Orders
# Remove all orders that are older than a certain date (e.g., orders placed more than a year ago).

# TODO: 15. Find Orders with Missing Details
# Identify all `orders` that have no corresponding records in `order_details`.

# TODO: 16. Products Never Ordered
# List all products that have never been ordered (i.e., products with no corresponding entry in `order_details`).

# TODO: 17. Users with Orders Over $1000
# Retrieve all users who have placed orders with a total value exceeding $1000.

# TODO: 18. Count Orders by Month
# Count the number of orders placed in each month of a given year.

# TODO: 19. Find Order-Product Pairs
# For each order, list the names of the products it includes and the total price for each product.

# TODO: 20. Revenue Trends by Month
# Calculate the total revenue (sum of `price * quantity`) generated in each month.
