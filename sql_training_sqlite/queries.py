import sqlite3


def execute_query(query, params=None):
    """
    Execute a query on the database and return the fetched results.

    :param query: SQL query string to execute
    :param params: Optional tuple of parameters to pass to the query (default is None)
    :return: List of fetched results (empty list if no results)
    """
    # Connect to the database
    conn = sqlite3.connect('sql_training_warehouse.db')
    cursor = conn.cursor()

    # If there are parameters for the query, execute the query with parameters
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    # Fetch all results from the executed query
    results = cursor.fetchall()

    # Show results
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")

    # Close the connection
    conn.close()


if __name__ == '__main__':

    # TODO: 1. Retrieve All Records from a Table
    # Write a query to fetch all records from the `products` table.
    query = "SELECT * FROM products"
    execute_query(query)

    # TODO: 2. Retrieve Specific Columns
    # Write a query to get only the `name` and `price` columns from the `products` table.


    # TODO: 3. Filter Results with WHERE Clause
    # Write a query to find all products with a `price` greater than 50.

    # TODO: 4. Sorting Results
    # Write a query to get all products ordered by `price` in descending order.

    # TODO: 5. Use of AND/OR Operators
    # Write a query to find products with a `price` greater than 50 and a `stock_quantity` less than 100.

    # TODO: 6. COUNT Function
    # Write a query to count how many products are available in the `products` table.

    # TODO: 7. DISTINCT Keyword
    # Write a query to get a list of unique product prices from the `products` table.

    # TODO: 8. LIKE Operator
    # Write a query to search for products whose names start with the letter 'A'.

    # TODO: 9. LIMIT and OFFSET
    # Write a query to retrieve the first 5 products from the `products` table.

    # TODO: 10. JOIN Two Tables
    # Write a query to get the names of products along with their corresponding order details, by joining the `products` and `order_products` tables.

    # TODO: 11. INNER JOIN with Multiple Conditions
    # Write a query to get a list of products ordered by a customer, where the order total exceeds 100.

    # TODO: 12. LEFT JOIN
    # Write a query to get all customers and their corresponding orders (if any) by using a left join between `customers` and `orders`.

    # TODO: 13. GROUP BY Clause
    # Write a query to calculate the total quantity of each product ordered, grouping by `product_id`.

    # TODO: 14. HAVING Clause
    # Write a query to find products that have been ordered more than 50 times, using the `HAVING` clause.

    # TODO: 15. Subquery in SELECT
    # Write a query to list all products along with the name of the customer who placed the largest order.

    # TODO: 16. Subquery in WHERE
    # Write a query to find all orders that have products with a price greater than 100.

    # TODO: 17. UPDATE Records
    # Write a query to update the `price` of a product with a specific `id` to 35.99.

    # TODO: 18. DELETE Records
    # Write a query to delete a product with a specific `id` from the `products` table.

    # TODO: 19. INSERT Multiple Records
    # Write a query to insert multiple products into the `products` table in a single query.

    # TODO: 20. Complex Query with JOIN, GROUP BY, and HAVING
    # Write a query to find the total number of products ordered by each customer, but only show customers who have ordered more than 5 products in total.

    # TODO: 21. Bonus - Find the Most Expensive Product
    # Write a query to find the most expensive product in the `products` table.

    # TODO: 22. Bonus - Find All Orders for a Specific Customer
    # Write a query to find all orders made by a specific customer, ordered by order date.

    # TODO: 23. Bonus - Create a View for Order Details
    # Create a view to show the `order_id`, `product_name`, and `quantity` for each product in an order.

    # TODO: 24. Bonus - Find Products That Have Not Been Ordered Yet
    # Write a query to find all products that have not been ordered yet.

    # TODO: 25. Bonus - Find Customers Who Ordered More Than Once
    # Write a query to list customers who have ordered products more than once.

