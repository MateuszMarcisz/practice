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

#     query = '''
#     SELECT *
# FROM products
# WHERE price = (SELECT MAX(price) FROM products)
#     '''
#     execute_query(query)

    # TODO: 22. Bonus - Find All Orders for a Specific Customer
    # Write a query to find all orders made by a specific customer, ordered by order date.

#     query = '''
#     SELECT *
# FROM orders
# WHERE customer_id = 7
# ORDER BY order_date
#     '''
#     execute_query(query)

    # TODO: 23. Bonus - Create a View for Order Details
    # Create a view to show the `order_id`, `product_name`, and `quantity` for each product in an order.

#     query = '''
#     CREATE VIEW order_info AS
# SELECT order_id, quantity, p.name
# FROM order_products
# JOIN products AS p ON order_products.product_id = p.id
#     '''
#     execute_query(query)

    # TODO: 24. Bonus - Find Products That Have Not Been Ordered Yet
    # Write a query to find all products that have not been ordered yet.

#     query = '''
#     SELECT name
# FROM products
# LEFT JOIN order_products AS op ON products.id = op.product_id
# WHERE op.quantity IS NULL
#     '''
#     execute_query(query)

    # this might be more efficient in big db:
#     query = '''
#     SELECT name
# FROM products p
# WHERE NOT EXISTS (
#     SELECT 1
#     FROM order_products op
#     WHERE op.product_id = p.id
# );
#     '''

    # TODO: 25. Bonus - Find Customers Who Ordered More Than Once
    # Write a query to list customers who have ordered products more than once.

    # query = '''
    # SELECT first_name, last_name, COUNT(o.id) AS number_of_orders
    # FROM customers
    # JOIN orders o ON customers.id = o.customer_id
    # GROUP BY first_name, last_name
    # HAVING number_of_orders > 1
    # '''
    # execute_query(query)

    # TODO: 26. INNER JOIN with Multiple Tables
    # Write a query to get the names of customers who have ordered products with a price greater than 500.

#     query = '''
#     SELECT DISTINCT first_name, last_name
# FROM customers
# JOIN orders ON customers.id = orders.customer_id
# JOIN order_products AS op ON orders.id = op.order_id
# WHERE op.price > 500
#     '''
#     execute_query(query)

    # TODO: 27. LEFT JOIN with Condition
    # Write a query to get all products and their corresponding warehouse quantities, including products that are not in the warehouse.

#     query = '''
#     SELECT name, COALESCE(warehouse.quantity, 0) as quantity
# FROM products
# LEFT JOIN warehouse ON products.id = warehouse.product_id
#     '''
#     execute_query(query)

    # TODO: 28. JOIN with Aggregate Function
    # Write a query to find the total quantity of products ordered by each customer.

    # query = '''
    # SELECT c.first_name, c.last_name, SUM(COALESCE(op.quantity, 0)) AS total_quantity_of_products
    # FROM customers AS c
    # LEFT JOIN orders AS o ON c.id = o.customer_id
    # LEFT JOIN order_products AS op ON o.id = op.order_id
    # GROUP BY c.id, first_name, last_name
    # '''
    # execute_query(query)

    # TODO: 29. JOIN with HAVING Clause
    # Write a query to find customers who have ordered more than 10 products in total.

    # query = '''
    # SELECT c.first_name, c.last_name, SUM(COALESCE(op.quantity, 0)) AS total_quantity_of_products
    # FROM customers AS c
    # LEFT JOIN orders AS o ON c.id = o.customer_id
    # LEFT JOIN order_products AS op ON o.id = op.order_id
    # GROUP BY c.id, first_name, last_name
    # HAVING SUM(COALESCE(op.quantity, 0)) > 10
    # '''
    # execute_query(query)


    # TODO: 30. RIGHT JOIN with Condition
    # Write a query to get all customers and the total amount they have spent on products, including those who have not made any orders.

    # query = '''
    # SELECT c.first_name, c.last_name, COALESCE(SUM(op.quantity * op.price), 0) AS total
    # FROM customers c
    # LEFT JOIN orders o ON c.id = o.customer_id
    # LEFT JOIN order_products op ON o.id = op.order_id
    # GROUP BY c.id, c.first_name, c.last_name
    # '''
    # execute_query(query)

    # TODO: 31. JOIN with Subquery
    # Write a query to find products that have been ordered by more than 5 different customers.

    # querry = '''
    # SELECT name, COUNT(DISTINCT o.customer_id) AS number_of_clients_that_ordered
    # FROM products p
    # JOIN order_products op ON p.id = op.product_id
    # JOIN orders o ON op.order_id = o.id
    # GROUP BY p.id
    # HAVING COUNT(DISTINCT o.customer_id) > 5
    # '''
    # execute_query(querry)

    # TODO: 32. Self JOIN
    # Find all customers who have ordered the same product.

    # query = '''
    # SELECT DISTINCT o.customer_id, p.name AS product_name
    # FROM orders o
    # JOIN order_products op ON o.id = op.order_id
    # JOIN products p ON op.product_id = p.id
    # WHERE op.product_id IN (
    #     SELECT op.product_id
    #     FROM order_products op
    #     JOIN orders o ON op.order_id = o.id
    #     GROUP BY op.product_id
    #     HAVING COUNT(DISTINCT o.customer_id) > 1
    # )
    # ORDER BY o.customer_id;
    # '''
    # execute_query(query)

    # TODO: 33. FULL OUTER JOIN (Simulated with UNION)
    # Write a query to find all products and their orders, including products with no orders and orders with no products.

    # query = '''
    # SELECT p.name, op.order_id
    # FROM products p
    # LEFT JOIN order_products op ON p.id = op.product_id
    # UNION
    # SELECT p.name, op.order_id
    # FROM order_products op
    # LEFT JOIN products p ON op.product_id = p.id
    # ORDER BY name
    # '''
    # execute_query(query)

    # TODO: 34. INNER JOIN with Multiple Conditions
    # Write a query to get customers who have ordered products from a specific category and have spent more than $100.

    # query = '''
    # SELECT c.first_name, c.last_name,
    #    SUM(op.price * op.quantity) AS total_per_order,
    #    COUNT(DISTINCT op.product_id) AS unique_items
    # FROM customers c
    # JOIN orders o ON c.id = o.customer_id
    # JOIN order_products op ON o.id = op.order_id
    # GROUP BY c.id, c.first_name, c.last_name, op.order_id
    # HAVING SUM(op.price * op.quantity) > 1000 AND COUNT(DISTINCT op.product_id) > 1
    # '''
    # execute_query(query)

    # TODO: 35. Cross Join
    # Write a query to get a list of all possible combinations of customers and products.

    # what is the point of this bs
    # query = '''
    # SELECT c.id AS customer_id, c.first_name, c.last_name, p.name AS product_name
    # FROM customers c
    # CROSS JOIN products p;
    # '''
    # execute_query(query)

    # TODO: 36. JOIN with DISTINCT
    # Write a query that will fetch all the location with mulitple of items assigned to them

    # query = '''
    # SELECT l.name, COUNT(DISTINCT w.product_id) AS number_of_stored_items
    # FROM locations l
    # JOIN warehouse w on l.id = w.location_id
    # GROUP BY l.name
    # HAVING COUNT(DISTINCT w.product_id) > 1
    # '''
    # execute_query(query)

    # TODO: 37. JOIN with LIKE Condition
    # Write a query to find customers whose names start with a specific letter and have ordered products from a specific category.

    # TODO: 38. JOIN with IS NULL
    # Write a query to find products that have never been ordered.

    # query = '''
    # SELECT p.name
    # FROM products p
    # LEFT JOIN order_products op ON p.id = op.product_id
    # WHERE op.product_id IS NULL
    # '''
    # execute_query(query)
    #
    # TODO: 39. JOIN with Date Condition
    # Write a query to find orders that were placed within the last 30 days.

    # query = '''
    # SELECT id, order_date
    # FROM orders
    # WHERE order_date >= DATE('now', '-30 days')
    # '''
    # execute_query(query)

    # TODO: 40. JOIN with EXISTS
    # Write a query to find products that have been ordered by customers with specific name.

    # query = '''
    # SELECT p.name, c.first_name, c.last_name
    # FROM products p
    # JOIN main.order_products op on p.id = op.product_id
    # JOIN orders ON op.order_id = orders.id
    # JOIN customers c ON orders.customer_id = c.id
    # WHERE c.first_name = 'Charles'
    # '''
    # execute_query(query)

    # TODO 41: Write a Python script to calculate the average price of all products in the `products` table.

    # query = '''
    # SELECT AVG(price) AS average_price
    # FROM products
    # '''
    # execute_query(query)

    # TODO 42: Find the top 5 most expensive products along with their descriptions using a Python query.

    # query = '''
    # SELECT *
    # FROM products
    # ORDER BY price DESC
    # LIMIT 5
    # '''
    # execute_query(query)

    # TODO 43: Perform an INNER JOIN between `products` and `warehouse` to get the total quantity of each product.

#     query = '''
#     SELECT p.name, w.quantity
# FROM products p
# JOIN warehouse w ON p.id = w.product_id
#     '''
#     execute_query(query)

    # TODO 44: Write a query to find the total stock quantity of each product, grouped by location.

#     query = '''
#     SELECT p.name, w.location_id, SUM(w.quantity) AS total_quantity
# FROM products p
# JOIN warehouse w ON p.id = w.product_id
# GROUP BY p.name, w.location_id
#     '''
#     execute_query(query)

    # TODO 45: Perform a LEFT JOIN to find products that are not stored in any warehouse location.

#     query = '''
#     SELECT p.name, w.location_id
# FROM products p
# LEFT JOIN warehouse w ON p.id = w.product_id
# WHERE w.location_id IS NULL
#     '''
#     execute_query(query)

    # TODO 46: Perform a RIGHT JOIN (simulated using LEFT JOIN) to find all locations that have no products.

    # query = '''
    # SELECT l.name
    # FROM locations l
    # LEFT JOIN warehouse w ON l.id = w.location_id
    # WHERE w.product_id IS NULL
    # '''
    # execute_query(query)

    # TODO 47: fetch product's (id 6) name, desc,, price, location's name, and quantity.

    # query = '''SELECT p.name, p.description, p.price, w.quantity, l.name
    # FROM products p
    # JOIN warehouse w ON p.id = w.product_id
    # JOIN locations l ON w.location_id = l.id
    # WHERE p.id = 6'''
    # execute_query(query)


    # TODO 48: Use a CROSS JOIN between `products` and `locations` to generate every possible product-location combination.

    # query = '''
    # SELECT p.name, l.name AS location_name
    # FROM products p
    # CROSS JOIN locations l
    # '''
    # execute_query(query)


    # TODO 49: Write a query to find orders that contain more than 3 unique products.

    # query = '''
    # SELECT o.id,
    #    COUNT(DISTINCT op.product_id) AS number_of_unique_products,
    #    GROUP_CONCAT(DISTINCT p.name) AS producs
    # FROM orders o
    # JOIN order_products op ON o.id = op.order_id
    # JOIN products p ON op.product_id = p.id
    # GROUP BY o.id
    # HAVING COUNT(DISTINCT op.product_id) > 3
    # '''
    # execute_query(query)

    # TODO 50: Write a Python function to update the stock of a product in the `warehouse` table based on order fulfillment.

    # query = '''
    # UPDATE warehouse
    # SET quantity = quantity + 2
    # WHERE product_id = 1 and location_id = 82
    # '''
    # execute_query(query)

    # TODO 51: Perform a query to find customers who have placed orders but have not purchased a specific product.
    # TODO 52: Use a FULL OUTER JOIN (simulated using UNION) to find all products and their warehouse locations, including mismatches.
    # TODO 53: Write a query to calculate the total revenue generated from all orders using `order_products`.
    # TODO 54: Find the most frequently ordered product and the total number of times it has been ordered.
    # TODO 55: Perform a JOIN query to get customer details along with their order status.
    # TODO 56: Write a script to find customers who haven’t placed any orders (use a LEFT JOIN).
    # TODO 57: Write a query to find products that appear in more than 10 different orders.
    # TODO 58: Create a function that returns the 3 most recent orders for a given customer.
    # TODO 59: Perform a JOIN query to find all products in the `products` table that are priced above the average price.
    # TODO 60: Write a query to identify customers who have placed orders containing products from multiple categories (if categories exist or can be derived from data).
    # TODO 61: Write a Python script to delete all products from the database with a stock quantity of zero.
    # TODO 62: Perform a query to get the names of customers who placed orders on the same day as a specific customer.
    # TODO 63: Write a Python script to find the total quantity of all products stored in warehouses and compare it to the `products` table stock quantity.
    # TODO 64: Perform a JOIN query to find orders containing products that are out of stock in the `warehouse` table.
    # TODO 65: Write a query to find the total number of products stored at each location.
    # TODO 66: Create a function that returns order details, including customer name and product names, for a given order ID.
    # TODO 67: Perform a query to get the customer who has spent the most money on orders.
    # TODO 68: Write a script to find and delete duplicate customer entries based on email addresses.
    # TODO 69: Perform a JOIN query to find orders that contain products with a specific word in their description.
    # TODO 70: Write a query to calculate the total quantity and value of products sold for each product ID.
    # TODO 71: Use a nested query to find the customer who placed the most orders in the past 30 days.
    # TODO 72: Write a script to automatically restock products in the warehouse with a stock quantity below a threshold.
    # TODO 73: Perform a query to find the customer who has ordered the largest variety of products.
    # TODO 74: Write a query to find orders containing products priced significantly higher than their average price.
    # TODO 75: Create a function to calculate and return the reorder rate for a specific product (times it has been ordered vs. total stock).
    # TODO 76: Perform a JOIN query to find orders with quantities exceeding the available stock at the time of order.
    # TODO 77: Write a query to calculate the revenue generated per customer and rank them by revenue.
    # TODO 78: Write a Python script to export the `orders` and `order_products` data as a CSV file, including JOINed details.
    # TODO 79: Perform a query to find customers who have placed orders with both `Delivered` and `Processing` statuses.
    # TODO 80: Write a Python script to detect and resolve foreign key constraint violations between `orders` and `customers`.

