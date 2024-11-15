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

    query = """
    CREATE TABLE products (
    id serial PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0
    )
    """
    connect_and_query(query)

    # create table orders

    query = """
    CREATE TABLE orders (
    id serial PRIMARY KEY,
    user_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    )
    """
    connect_and_query(query)

    #create table Order Details

    query = """
    CREATE TABLE order_details (
    id serial PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
    )
    """
    connect_and_query(query)