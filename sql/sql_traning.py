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
            for row in results:
                print(row)

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
    # TODO: 1. List all users who have placed at least one order.
    query = '''SELECT DISTINCT user_id from orders'''
    connect_and_query(query)
    query = '''
    SELECT DISTINCT username from users
    JOIN orders ON orders.user_id = users.id
    '''
    connect_and_query(query)

# TODO: 2. Retrieve all orders placed by a user with a specific user_id (e.g., user_id = 13).

# TODO: 3. Display the total quantity ordered for each product by product_id.

# TODO: 4. Find the total amount spent per user (sum of price * quantity for each order).

# TODO: 5. Identify the most purchased product by quantity (highest total quantity across all orders).

# TODO: 6. List the total number of orders placed on a specific date (e.g., '2023-01-01').

# TODO: 7. Join users and orders to display each user's name alongside their order_id.

# TODO: 8. Find the details of all products ordered by a specific user (e.g., user_id = 29).

# TODO: 9. Retrieve the total spending per order, including the order_id and user_id (sum of price * quantity).

# TODO: 10. Identify users who have placed more than 3 orders.

# TODO: 11. Find users who have never placed an order (i.e., no order_id associated with them).

# TODO: 12. List all products purchased by users who have ordered products with a price greater than $300.

# TODO: 13. Retrieve the top 5 users by total spending (sum of price * quantity).

# TODO: 14. Find all orders where the total spending exceeds the average order total.

# TODO: 15. Identify the product(s) with the highest total revenue (sum of price * quantity for each product).

# TODO: 16. Update the order_date for a specific order (e.g., order_id = 5) to a new date.

# TODO: 17. Increase the price of all products by 10% for orders placed by a specific user_id (e.g., user_id = 50).

# TODO: 18. Delete all orders placed by a specific user (e.g., user_id = 32).

# TODO: 19. Remove all products from order_details where the quantity is less than 2.
