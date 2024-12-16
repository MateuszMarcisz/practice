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

    # query = "SELECT * FROM products"
    # execute_query(query)

    # TODO: 2. Retrieve Specific Columns
    # Write a query to get only the `name` and `price` columns from the `products` table.

#     query = '''
#     SELECT name, price
# FROM products
#     '''
#     execute_query(query)

    # TODO: 3. Filter Results with WHERE Clause
    # Write a query to find all products with a `price` greater than 50.

#     query = '''
#     SELECT name, price
# FROM products
# WHERE price > 50
#     '''
#     execute_query(query)

    # TODO: 4. Sorting Results
    # Write a query to get all products ordered by `price` in descending order.

#     query = '''
#     SELECT name, price
# FROM products
# ORDER BY price DESC
#     '''
#     execute_query(query)

    # TODO: 5. Use of AND/OR Operators
    # Write a query to find products with a `price` greater than 50 and a `stock_quantity` less than 100.

#     query = '''
#     SELECT name, price, stock_quantity
# FROM products
# WHERE price > 50 and stock_quantity < 100
#     '''
#     execute_query(query)

    # TODO: 6. COUNT Function
    # Write a query to count how many products are available in the `products` table.

#     query = '''
#     SELECT COUNT(*)
# FROM products
# WHERE stock_quantity > 0
#     '''
#     execute_query(query)

    # TODO: 7. DISTINCT Keyword
    # Write a query to get a list of unique product prices from the `products` table.

#     query = '''
#     SELECT DISTINCT price
# FROM products
#     '''
#     execute_query(query)

    # TODO: 8. LIKE Operator
    # Write a query to search for products whose names start with the letter 'A'.

#     query = '''
# SELECT name
# FROM products
# WHERE name LIKE 'A%'
#     '''
#     execute_query(query)

    # TODO: 9. LIMIT and OFFSET
    # Write a query to retrieve the first 5 products from the `products` table.

#     query = '''
#     SELECT name
# FROM products
# ORDER BY id
# LIMIT 5
#     '''
#     execute_query(query)


    # TODO: 10. JOIN Two Tables
    # Write a query to get the names of products along with their corresponding order details, by joining the `products` and `order_products` tables.

#     query = '''
#     SELECT name, order_products.*
# FROM products
# LEFT JOIN order_products
# ON products.id = order_products.product_id
#     '''
#     execute_query(query)

    # TODO: 11. INNER JOIN with Multiple Conditions
    # Write a query to get a list of products ordered by a customer, where the order total exceeds 100.

    # query = '''
    # SELECT SUM(order_products.quantity*main.order_products.price) as total,
    #    order_products.product_id,
    #    customers.first_name,
    #    customers.last_name
    # FROM order_products
    # JOIN orders ON order_products.order_id = orders.id
    # JOIN customers ON orders.customer_id = customers.id
    # GROUP BY orders.id, customers.first_name, customers.last_name
    # HAVING total > 100
    # ORDER BY total
    # '''
    # execute_query(query)

    # TODO: 12. LEFT JOIN
    # Write a query to get all customers and their corresponding orders (if any) by using a left join between `customers` and `orders`.

#     query = '''
#     SELECT customers.first_name, customers.last_name, GROUP_CONCAT(orders.id) AS order_ids
# FROM customers
# LEFT JOIN orders ON customers.id = orders.customer_id
# GROUP BY customers.first_name, customers.last_name
#     '''
#     execute_query(query)

    # TODO: 13. GROUP BY Clause
    # Write a query to calculate the total quantity of each product ordered, grouping by `product_id`.

#     query = '''
#     SELECT products.name, SUM(order_products.quantity) AS total_quantity_ordered
# FROM products
# LEFT JOIN order_products ON products.id = order_products.product_id
# GROUP BY products.name
#     '''
#     execute_query(query)

    # TODO: 14. HAVING Clause
    # Write a query to find products that have been ordered more than 50 times, using the `HAVING` clause.

#     query = '''
#     SELECT products.name, SUM(order_products.quantity) AS total_quantity_ordered
# FROM products
# JOIN order_products ON products.id = order_products.product_id
# GROUP BY products.name
# HAVING SUM(order_products.quantity) > 10
#     '''
#     execute_query(query)

    # TODO: 15. Subquery in SELECT
    # Write a query to list all products along with the name of the customer who placed the largest order.
#     query = '''
#     WITH largest_order AS (
#     SELECT orders.id AS order_id, customers.first_name, customers.last_name, SUM(order_products.price * order_products.quantity) AS total_order_value
#     FROM orders
#     JOIN customers ON orders.customer_id = customers.id
#     JOIN order_products ON orders.id = order_products.order_id
#     JOIN products ON order_products.product_id = products.id
#     GROUP BY orders.id, customers.id
#     ORDER BY total_order_value DESC
#     LIMIT 1
# )
# SELECT products.name, largest_order.first_name, largest_order.last_name, largest_order.order_id
# FROM order_products
# JOIN products ON order_products.product_id = products.id
# JOIN largest_order ON order_products.order_id = largest_order.order_id
# ORDER BY products.name;
#     '''
#     execute_query(query)
    # TODO: 16. Subquery in WHERE
    # Write a query to find all orders that have products with a price greater than 100.

#     query = '''
#     SELECT DISTINCT orders.id
# FROM orders
# JOIN order_products ON orders.id = order_products.order_id
# WHERE order_products.price > 100
#     '''
#     execute_query()

    # TODO: 17. UPDATE Records
    # Write a query to update the `price` of a product with a specific `id` to 35.99.

#     query = '''
#     UPDATE products
# SET price = 35.99
# WHERE id = 2
#     '''
#     execute_query(query)

    # TODO: 18. DELETE Records
    # Write a query to delete a product with a specific `id` from the `products` table.

#     query = '''
#     DELETE FROM products
# WHERE id = 666
#     '''
#     execute_query(query)

    # TODO: 19. INSERT Multiple Records
    # Write a query to insert multiple products into the `products` table in a single query.

    # query = '''
    # INSERT INTO products(name, description, price, stock_quantity)
    # VALUES ('pump', 'best pump ever', 666, 42),
    #        ('hehe', 'very funny', 6.9, 420)
    # '''
    # execute_query(query)

    # TODO: 20. Complex Query with JOIN, GROUP BY, and HAVING
    # Write a query to find the total number of products ordered by each customer, but only show customers who have ordered more than 5 products in total.

#     query = '''
# SELECT customers.first_name, customers.last_name, SUM(op.quantity) as number_of_products_ordered
# FROM customers
# JOIN orders ON customers.id = orders.customer_id
# JOIN order_products AS op ON orders.id = op.order_id
# GROUP BY customers.first_name, customers.last_name
# HAVING number_of_products_ordered > 5
#     '''
#     execute_query(query)

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

