from sql.db_config import connect_to_db


def connect_and_query(query):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # Execute and handle the query
        cursor.execute(query)

        # Fetch and print results if it's a SELECT query
        if query.strip().lower().startswith("select"):
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
    query = '''
    SELECT users.username AS user, 
       SUM(COALESCE(order_details.price, 0) * COALESCE(order_details.quantity, 0)) AS total
FROM order_details
JOIN orders ON order_details.order_id = orders.id
JOIN users ON orders.user_id = users.id 
GROUP BY users.username
ORDER BY total DESC
LIMIT 5;
    '''

    connect_and_query(query)


# TODO: 14. Find all orders where the total spending exceeds the average order total.

# TODO: 15. Identify the product(s) with the highest total revenue (sum of price * quantity for each product).

# TODO: 16. Update the order_date for a specific order (e.g., order_id = 5) to a new date.

# TODO: 17. Increase the price of all products by 10% for orders placed by a specific user_id (e.g., user_id = 50).

# TODO: 18. Delete all orders placed by a specific user (e.g., user_id = 32).

# TODO: 19. Remove all products from order_details where the quantity is less than 2.
