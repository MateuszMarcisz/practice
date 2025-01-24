import sqlite3
from idlelib import query


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

    # TODO 50: update the stock of a product in the `warehouse` table

    # query = '''
    # UPDATE warehouse
    # SET quantity = quantity + 2
    # WHERE product_id = 1 and location_id = 82
    # '''
    # execute_query(query)

    # TODO 51: Perform a query to find customers who have placed orders but have not purchased a specific product.

#     query = '''
#     SELECT c.first_name, c.last_name, GROUP_CONCAT(DISTINCT op.product_id)
# FROM customers c
# JOIN orders o ON c.id = o.customer_id
# JOIN order_products op ON o.id = op.order_id
# WHERE c.id NOT IN (
#     SELECT DISTINCT o.customer_id
#     FROM orders o
#     JOIN order_products op ON o.id = op.order_id
#     WHERE op.product_id = 1
#     )
# GROUP BY c.id
#     '''
#     execute_query(query)


    # TODO 52: Use a FULL OUTER JOIN (simulated using UNION) to find all products and their warehouse locations, including mismatches.

    # query = '''
    # SELECT p.name, l.name
    # FROM products p
    # LEFT JOIN warehouse w ON p.id = w.product_id
    # LEFT JOIN main.locations l on w.location_id = l.id
    # UNION
    # SELECT p.name, l.name
    # FROM locations l
    # LEFT JOIN warehouse w ON l.id = w.location_id
    # LEFT JOIN products p ON w.product_id = p.id
    # '''
    # execute_query(query)



    # TODO 53: Write a query to calculate the total revenue generated from all orders using `order_products`.

    # query = '''
    # SELECT SUM(op.quantity * op.price) AS revenue
    # FROM order_products op
    # '''
    # execute_query(query)

    # TODO 54: Find the most frequently ordered product and the total number of times it has been ordered.

#     query = '''
#     WITH product_counting AS (
#     SELECT p.name, COUNT(op.product_id) AS order_count
# FROM products p
# JOIN order_products op ON p.id = op.product_id
# GROUP BY op.product_id
# )
#
# SELECT name, order_count
# FROM product_counting
# WHERE order_count = (
#     SELECT MAX(order_count)
#     FROM product_counting
#     )
#     '''
#     execute_query(query)

    # TODO 55: Perform a JOIN query to get customer details along with their order status.

    # query = '''
    # SELECT c.first_name, c.last_name, o.id, o.status
    # FROM customers c
    # JOIN orders o ON c.id = o.customer_id
    # '''
    # execute_query(query)

    # TODO 56: Write a script to find customers who haven’t placed any orders (use a LEFT JOIN).

    # query = '''
    # SELECT c.first_name, c.last_name
    # FROM customers c
    # LEFT JOIN orders o ON c.id = o.customer_id
    # WHERE o.id IS NULL
    # '''
    # execute_query(query)

    # TODO 57: Write a query to find products that appear in more than 10 different orders.

    # query = '''
    # SELECT p.name, COUNT(DISTINCT op.order_id) AS number_of_orders
    # FROM products p
    # JOIN order_products op ON p.id = op.product_id
    # GROUP BY p.name
    # HAVING COUNT(DISTINCT op.order_id) > 10
    # '''
    # execute_query(query)

# TODO 58: Write a query using a CTE to calculate the total stock quantity for each product and filter only the products with a total stock greater than 100.

#     query = '''
#     WITH product_stock AS (
#     SELECT p.name, SUM(w.quantity) AS stock
#     FROM products p
#     JOIN warehouse w ON p.id = w.product_id
#     GROUP BY p.name
#     )
# SELECT ps.name, ps.stock
# FROM product_stock ps
# WHERE stock > 100
#     '''
#     execute_query(query)

# TODO 59: Use a CTE to find the average price of all products and list products that are above the average price.

#     query = '''
#     WITH products_average AS (
#     SELECT AVG(price) AS avg_price
#     FROM products
# )
# SELECT p.name, p.price
# FROM products p
# JOIN products_average pa ON p.price > pa.avg_price
#     '''
#     execute_query(query)

# TODO 60: Use a CTE to rank products by total quantity in the warehouse and fetch the top 5 products by rank.

#     query = '''
#     WITH quantity_rank AS (
#     SELECT p.name,
#            p.stock_quantity AS quantity,
#            RANK() OVER (ORDER BY p.stock_quantity) AS quantity_rank
#     FROM products p
# )
# SELECT qr.name, qr.quantity, qr.quantity_rank
# FROM quantity_rank qr
# WHERE qr.quantity_rank <=5
#     '''
#     execute_query(query)

# TODO 61: Create a query that calculates the total revenue per customer using a CTE, then filter only customers who have generated more than $500 in revenue.

    # query = '''
    #     WITH total_per_customer AS (
    #     SELECT
    #         o.customer_id,
    #         SUM(op.quantity * op.price) AS revenue_per_customer
    #     FROM orders o
    #     JOIN order_products op ON o.id = op.order_id
    #     GROUP BY o.customer_id
    #     )
    #
    #     SELECT
    #         c.first_name,
    #         c.last_name,
    #         tpc.revenue_per_customer
    #     FROM customers c
    #     JOIN total_per_customer tpc ON c.id = tpc.customer_id
    #     WHERE tpc.revenue_per_customer > 500
    # '''
    # execute_query(query)

# TODO 62: Write a query using a window function to calculate the cumulative quantity of products in the warehouse table, ordered by product_id.

    # query = '''
    # SELECT p.name,
    #    w.product_id,
    #    w.quantity,
    #    SUM(w.quantity) OVER (ORDER BY w.product_id) AS cumulative_quantity
    # FROM warehouse w
    # JOIN products p ON w.product_id = p.id
    # '''
    # execute_query(query)

# TODO 63: Use a window function to calculate the running total of revenue for each product in the order_products table.

#     query = '''
#     WITH product_revenue AS (
#     SELECT
#         p.name,
#         op.product_id,
#         SUM(op.quantity * op.price) AS total_revenue
#     FROM products p
#     JOIN order_products op ON p.id = op.product_id
#     GROUP BY p.name, op.product_id
# )
# SELECT
#     pr.name,
#     pr.product_id,
#     pr.total_revenue,
#     SUM(pr.total_revenue) OVER (ORDER BY pr.product_id) AS cumulative_revenue
# FROM product_revenue pr
#     '''
#     execute_query(query)

# TODO 64: Use a window function to assign a rank to customers based on the number of orders they have placed.

    #     query = '''
    # SELECT c.first_name,
    #    c.last_name,
    #    COUNT(o.id) AS number_of_orders,
    #    RANK() OVER (ORDER BY COUNT(o.id) DESC) AS rank
    # FROM customers c
    # LEFT JOIN orders o ON c.id = o.customer_id
    # GROUP BY c.first_name, c.last_name
    # '''
    # execute_query(query)

# TODO 65: Use a query with both CTEs and window functions to find the top 3 customers based on revenue generated, along with their rank.

    # query = '''
    # WITH revenue_per_customer AS (
    # SELECT c.first_name,
    #        c.last_name,
    #        SUM(op.quantity * op.price) AS total
    # FROM customers c
    # JOIN orders o on c.id = o.customer_id
    # JOIN order_products op on o.id = op.order_id
    # GROUP BY c.first_name, c.last_name
    # )
    # SELECT first_name,
    #        last_name,
    #        total,
    #        RANK() OVER (ORDER BY total DESC) AS rank
    # FROM revenue_per_customer
    # LIMIT 3
    # '''
    # execute_query(query)

# TODO 66: Transform the order_products table by calculating the average quantity ordered per product and filter products with an average greater than 2 using a CTE.

#     query = '''
# WITH average_quantity AS (
#     SELECT p.name,
#            AVG(op.quantity) AS avg_quant_per_product
#     FROM products p
#     JOIN order_products op ON p.id = op.product_id
#     GROUP BY p.id, p.name
# )
# SELECT *
# FROM average_quantity aq
# WHERE aq.avg_quant_per_product > 2
#     '''
#     execute_query(query)

# TODO 67: Use a CTE to fetch all products along with the percentage contribution of their quantity to the total stock in the warehouse.

    # query = '''
    # WITH total_stock AS (
    # SELECT SUM(quantity) AS total
    # FROM warehouse
    # ),
    # product_stock AS (
    # SELECT product_id,
    #        SUM(quantity) AS product_quantity
    # FROM warehouse
    # GROUP BY product_id
    # )
    # SELECT ps.product_id,
    #    ps.product_quantity,
    #    ROUND((ps.product_quantity * 100.0) / ts.total, 2) AS percentage_contribution
    # FROM product_stock ps
    # CROSS JOIN total_stock ts
    # '''
    # execute_query(query)

# TODO 68: Use a window function to calculate the difference between the highest and lowest prices of a product ordered in the order_products table.
#
#     query '''
# WITH product_price_range AS (
#     SELECT
#         product_id,
#         MIN(price) OVER (PARTITION BY product_id) AS min_price,
#         MAX(price) OVER (PARTITION BY product_id) AS max_price
#     FROM order_products
# )
# SELECT
#     product_id,
#     max_price - min_price AS price_range
# FROM product_price_range
# GROUP BY product_id
#     '''
#     execute_query(query)

# TODO 69: Write a query using a CTE to group orders by status and calculate the total number of orders for each status.
#
#     query = '''
#     SELECT status,
#        GROUP_CONCAT(DISTINCT id) AS ids,
#        COUNT(id) AS number_of_orders
# FROM orders
# GROUP BY status
#     '''
#     execute_query(query)

# TODO 70: Use a query with a window function to calculate the lag of revenue per order, showing the difference in revenue between consecutive orders.

#     query = '''
#     SELECT
#     o.id AS order_id,
#     SUM(op.quantity * op.price) AS order_revenue,
#     LAG(SUM(op.quantity * op.price)) OVER (ORDER BY o.id) AS previous_revenue,
#     SUM(op.quantity * op.price) - LAG(SUM(op.quantity * op.price)) OVER (ORDER BY o.id) AS revenue_difference
# FROM orders o
# JOIN order_products op ON o.id = op.order_id
# GROUP BY o.id
# ORDER BY o.id
#     '''
#     execute_query(query)

# TODO 71: Write a query to generate a ranking of products based on the frequency of orders, using a window function.

    # query = '''
    # SELECT product_id,
    #    COUNT(order_id) AS number_of_orders,
    #    RANK() OVER (ORDER BY COUNT(order_id) DESC) AS rank
    # FROM order_products
    # GROUP BY product_id
    # '''
    # execute_query(query)

# TODO 72: Transform the warehouse table by calculating the ratio of the stock quantity at each location to the total stock of the respective product.

    # query = '''
    # WITH total_stock AS (
    # SELECT product_id,
    #        SUM(quantity) AS total
    # FROM warehouse
    # GROUP BY product_id
    # )
    # SELECT w.product_id,
    #        w.location_id,
    #        (w.quantity / ts.total * 100) AS stock_percentage
    # FROM warehouse w
    # JOIN total_stock ts ON w.product_id = ts.product_id
    # '''
    # execute_query(query)

# TODO 73: Use a CTE to normalize product prices by subtracting the average price from each product's price.

    # query = '''
    # WITH average_price AS (
    # SELECT AVG(price) AS average
    # FROM products
    # )
    # SELECT p.id,
    #        p.name,
    #        p.price - ap.average AS normalized_price
    # FROM products p
    # CROSS JOIN average_price ap
    # '''
    # execute_query(query)

# TODO 74: Write a query using a window function to calculate the percentage of total revenue contributed by each order.

    # query = '''
    # WITH total_revenue AS (
    # SELECT SUM(quantity * price) AS total
    # FROM order_products
    # )
    #
    # SELECT op.order_id,
    #        ROUND(SUM(op.quantity * op.price) / tr.total * 100, 2) AS percentage_of_revenue
    # FROM order_products op
    # CROSS JOIN total_revenue tr
    # GROUP BY op.order_id
    # '''
    # execute_query(query)

# TODO 75: Use a CTE to fetch products and their respective revenue per product, filtering products with revenue above the 75th percentile.

#     query = '''
#     WITH revenue_per_product AS (
#         SELECT p.name,
#                SUM(op.quantity * op.price) AS product_revenue
#         FROM products p
#         JOIN order_products op ON p.id = op.product_id
#         GROUP BY p.id
#     ),
#         percentile AS (
#         SELECT name,
#                product_revenue,
#                NTILE(4) OVER (ORDER BY product_revenue DESC) AS quartile
#         FROM revenue_per_product
#         )
#     SELECT name,
#            product_revenue
#     FROM percentile
#     WHERE quartile = 1
#
# --One can use PERCENTILE_CONT() if it is supported by the engine
#     '''
#     execute_query(query)

# TODO 76: Write a query using a window function to calculate the rank of products based on their average price in descending order.

    # query = '''
    # WITH avg_price AS(
    #     SELECT p.name,
    #            AVG(op.price) AS average_sell_price
    #     FROM products p
    #     JOIN order_products op ON p.id = op.product_id
    #     GROUP BY p.id, p.name
    #        )
    # SELECT name,
    #        average_sell_price,
    #        RANK() OVER (ORDER BY average_sell_price DESC) AS rank
    # FROM avg_price
    # '''
    # execute_query(query)

# TODO 77: Use a CTE to find the products whose price is above the median price of all products.

    # query = '''
    # -- If percentile_cont is supported one can use just this: PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) instead of abomination below
    # WITH ordered_prices AS (
    #     SELECT price,
    #            ROW_NUMBER() OVER (ORDER BY price) AS row_num,
    #            COUNT(*) OVER () AS total_rows
    #     FROM products
    # ), median_price AS (
    #     SELECT
    #         CASE
    #             WHEN total_rows % 2 = 1 THEN
    #                 MAX(price) FILTER (WHERE row_num = (total_rows + 1) / 2)
    #             ELSE
    #                 AVG(price) FILTER (WHERE row_num IN (total_rows / 2, (total_rows / 2) + 1))
    #         END AS median
    #     FROM ordered_prices
    # )
    # SELECT p.name,
    #        p.price,
    #        p.price - mp.median AS above_median
    # FROM products p
    # CROSS JOIN median_price mp
    # WHERE p.price > mp.median
    # ORDER BY p.price DESC
    # '''
    # execute_query(query)

    # apparenly sqlite version in my pycharm have median function so it can be used as this:
    # query = '''
    # WITH median_price AS (
    #     SELECT median(price) AS median_price_
    #     FROM products
    # )
    # SELECT p.name,
    #        p.price
    # FROM products p
    # CROSS JOIN median_price mp
    # WHERE p.price > mp.median_price_
    # '''


# TODO 78: Write a query using a window function to partition the data by location_id and calculate the total quantity of products per location.

    # query = '''
    # SELECT w.location_id,
    #        GROUP_CONCAT(DISTINCT product_id) AS produts_in_location,
    #        SUM(w.quantity) OVER (PARTITION BY w.location_id) AS total_per_location
    # FROM warehouse w
    # GROUP BY location_id
    # '''
    # execute_query(query)

# TODO 79: Use a CTE to create a summary table of customers, including their total orders, total revenue, and the average revenue per order.

    # query = '''
    # WITH customer_orders AS (
    #     SELECT customer_id,
    #            COUNT(*) AS number_of_orders
    #     FROM orders
    #     GROUP BY customer_id
    # ), customer_total AS (
    #     SELECT o.customer_id,
    #            SUM(op.quantity * op.price) AS total_per_customer,
    #            AVG(op.quantity * op.price) AS average_per_customer
    #     FROM order_products op
    #     JOIN orders o ON op.order_id = o.id
    #     GROUP BY o.customer_id
    # )
    # SELECT c.id,
    #        CONCAT(c.first_name, ' ', c.last_name) AS name,
    #        co.number_of_orders,
    #        ct.total_per_customer,
    #        ct.average_per_customer
    # FROM customers c
    # JOIN customer_orders co ON c.id = co.customer_id
    # JOIN customer_total ct ON c.id = ct.customer_id
    # '''
    # execute_query()

# TODO 80: Write a query using a CTE and a window function to calculate the difference between a product's price and the average price of all products in the same warehouse location.

    # query = '''
    # WITH average AS (
    #     SELECT w.location_id,
    #            AVG(p.price) AS average_per_location
    #     FROM warehouse w
    #     JOIN products p ON w.product_id = p.id
    #     GROUP BY location_id
    # )
    # SELECT p.name,
    #        w.location_id,
    #        a.average_per_location,
    #        ROUND(p.price - a.average_per_location, 2) AS price_diff
    # FROM products p
    # JOIN warehouse w ON p.id = w.product_id
    # JOIN average a ON w.location_id = a.location_id
    # ORDER BY p.name, w.location_id
    # '''
    # execute_query(query)

# TODO 81: Combine a CTE with window functions to create a report showing each customer’s total revenue, average order value, and their rank based on revenue.

    # query = '''
    # WITH customer_revenue AS (
    #     SELECT CONCAT(c.first_name, ' ',c.last_name) AS customer,
    #            SUM(op.price * op.quantity) AS total_revenue,
    #            AVG(op.price * op.quantity) AS average_order_value
    #     FROM customers c
    #     JOIN orders o ON c.id = o.customer_id
    #     JOIN order_products op ON o.id = op.order_id
    #     GROUP BY c.id
    # )
    # SELECT *,
    #        RANK() OVER (ORDER BY total_revenue DESC) AS rank
    # FROM customer_revenue
    # '''
    # execute_query(query)

# TODO 82: Write a query to transform the order_products table by calculating the z-score (standard score) for each product's price.

    # query = '''
    # WITH statistics AS (
    #     SELECT AVG(price) AS mean,
    #            STDEV(price) AS std_dev
    #     FROM order_products
    # )
    # SELECT op.id,
    #        p.name AS product,
    #        op.price,
    #        (op.price - s.mean) / s.std_dev AS z_score
    # FROM order_products op
    # JOIN products p ON op.product_id = p.id
    # CROSS JOIN statistics s
    # '''
    # execute_query(query)

# TODO 83: Use a CTE to split orders into "High Value" and "Low Value" groups based on whether their total revenue is above or below the average order value.

    # query = '''
    # WITH order_revenue AS (
    #     SELECT order_id,
    #            SUM(price * quantity) AS total_revenue
    #     FROM order_products
    #     GROUP BY order_id
    # ),
    # average_revenue AS (
    #     SELECT AVG(total_revenue) AS average
    #     FROM order_revenue
    # )
    # SELECT op.order_id,
    #        ROUND(SUM(op.quantity * op.price), 2) AS order_revenue,
    #        CASE
    #            WHEN SUM(op.quantity * op.price) > ar.average THEN 'High Value'
    #            ELSE 'Low Value'
    #            END AS Value_Category,
    #     ROUND(ar.average, 2) AS average
    # FROM order_products op
    # CROSS JOIN average_revenue ar
    # GROUP BY op.order_id
    # '''
    # execute_query(query)

# TODO 84: Write a query using a window function to assign a dense rank to warehouse locations based on the total stock they hold.

    # query = '''
    # SELECT w.location_id,
    #        l.name,
    #        DENSE_RANK() OVER(ORDER BY SUM(w.quantity) DESC) AS Rank
    # FROM warehouse w
    # JOIN locations l ON w.location_id = l.id
    # GROUP BY w.location_id, l.name
    # '''
    # execute_query(query)

# TODO 85: Write a query to find the total stock quantity across all locations.

# TODO 86: Calculate the average price of products per warehouse location.

# TODO 87: Retrieve the top 5 most expensive products and their descriptions.

# TODO 88: Find the customers who placed the highest number of orders.

# TODO 89: List all locations with their total stock value (price × quantity).

# TODO 90: Use a CTE to list all products priced above the average product price.

# TODO 91: Create a CTE to calculate the total revenue per customer and display customers who contributed at least 5% of the total revenue.

# TODO 92: Use a CTE to calculate the monthly order count and average order value.

# TODO 93: With a CTE, generate a report showing warehouse locations with their total stock and highlight locations with above-average stock.

# TODO 94: Create a CTE to rank products based on total quantity sold.

# TODO 95: Write a query using a window function to rank customers by total revenue.

# TODO 96: Use a window function to assign a dense rank to products based on their price.

# TODO 97: Calculate a running total of revenue from all orders, sorted by date.

# TODO 98: Assign a rank to orders based on the number of items in each order.

# TODO 99: For each customer, calculate the average price of products they purchased and compare each product's price to this average.

# TODO 100: Identify the products that are stored in more than one location.

# TODO 101: Find the customers whose orders include at least 3 different products.

# TODO 102: Write a query to list products that have never been ordered.

# TODO 103: Identify orders that include products from multiple locations.

# TODO 104: Generate a list of customers who have purchased products worth over $500.

# TODO 105: Write a query to group products into price ranges (e.g., <$100, $100-$500, >$500).

# TODO 106: Transform the order_products table to show the percentage of each product's price relative to the total price in that order.

# TODO 107: Create a report showing customers' first and last orders using window functions.

# TODO 108: Use a query to split customers into quartiles based on their total revenue.

# TODO 109: For each order, calculate the z-score of the total revenue compared to all orders.

# TODO 110: Write a query to find locations where the stock quantity of any product exceeds the average stock across all locations.

# TODO 111: Identify orders that have the highest total revenue among all orders placed by the same customer.

# TODO 112: Find products that have a price higher than the average price of all products in their location.

# TODO 113: List customers who spent more than the average revenue of all customers.

# TODO 114: Retrieve the top 3 products with the highest quantity sold per location.

# TODO 115: Use a CTE to calculate the total revenue per product, then assign a rank to each product within its price range using window functions.

# TODO 116: Create a report that calculates the moving average of order quantities over time.

# TODO 117: Use a window function to calculate the percentage of total revenue each customer contributes to the company.

# TODO 118: Write a query to rank locations based on the number of unique products they store.

# TODO 119: Combine a CTE and a window function to identify the top-selling product per location.

# TODO 120: Transform the customers table to show the count of orders in "Processing," "Shipped," and "Delivered" statuses for each customer.

# TODO 121: Create a report showing the total revenue from orders grouped by month and customer.

# TODO 122: Pivot the warehouse table to show the total stock quantity of products for each location in separate columns.

# TODO 123: Unpivot the order_products table to list each product and its respective quantity and price as separate rows.

# TODO 124: Generate a pivot table showing the number of products in different price ranges per location.

# TODO 125: Write a query to calculate the median price of products per location.

# TODO 126: Use a window function to calculate the 75th percentile of product prices across all locations.

# TODO 127: Calculate the standard deviation of order values per customer.

# TODO 128: For each product, determine how its price compares to the average price of all products.

# TODO 129: Identify locations where the z-score of total stock is above 2.0.

# TODO 130: Find the product that generates the highest revenue in each location.

# TODO 131: Write a query to calculate the reorder point (quantity below which restocking is needed) for each product.

# TODO 132: Generate a report showing the order trends (e.g., increasing or decreasing) over the last 6 months.

# TODO 133: For each customer, calculate the time difference between their first and last orders.

# TODO 134: Write a query to calculate the Gini coefficient of revenue distribution among customers.
