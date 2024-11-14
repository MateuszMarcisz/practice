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
    query = """
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    connect_and_query(query)
