import sqlite3
from faker import Faker
import random
from datetime import datetime


conn = sqlite3.connect('sql_training_warehouse.db')

cursor = conn.cursor()


# tables

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         description TEXT,
#         price REAL,
#         stock_quantity INTEGER
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS locations (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS warehouse (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         product_id INTEGER,
#         location_id INTEGER,
#         quantity INTEGER,
#         FOREIGN KEY (product_id) REFERENCES products(id),
#         FOREIGN KEY (location_id) REFERENCES locations(id)
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS orders (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         order_date DATE,
#         status TEXT,
#         customer_id INTEGER,
#         FOREIGN KEY (customer_id) REFERENCES customers(id)
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS order_products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         order_id INTEGER,
#         product_id INTEGER,
#         quantity INTEGER,
#         price REAL,
#         FOREIGN KEY (order_id) REFERENCES orders(id),
#         FOREIGN KEY (product_id) REFERENCES products(id)
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS customers (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         email TEXT NOT NULL
#     )
# ''')

fake = Faker()

# populate data

# products
products = []
for _ in range(200):  # Generate 200 products
    name = fake.word().capitalize()
    description = fake.sentence()
    price = round(random.uniform(50.0, 1000.0), 2)
    stock_quantity = random.randint(1, 100)
    products.append((name, description, price, stock_quantity))

cursor.executemany('''
    INSERT INTO products (name, description, price, stock_quantity)
    VALUES (?, ?, ?, ?)
''', products)


# locations
locations = []
for shelf in range(1, 11):  # 10 shelves
    for row in range(1, 11):  # 10 rows per shelf
        location_name = f'Shelf {shelf}, Row {row}'
        locations.append((location_name,))

cursor.executemany('''
    INSERT INTO locations (name)
    VALUES (?)
''', locations)

# warehouse
warehouse_data = []
for product_id in range(1, 201):  # Products are numbered 1 to 200
    location_id = random.randint(1, 100)  # Now there are 100 locations
    quantity = random.randint(1, 50)
    warehouse_data.append((product_id, location_id, quantity))

cursor.executemany('''
    INSERT INTO warehouse (product_id, location_id, quantity)
    VALUES (?, ?, ?)
''', warehouse_data)

# customers
customers = []
for _ in range(50):  # Generate 50 customers
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    customers.append((first_name, last_name, email))

cursor.executemany('''
    INSERT INTO customers (first_name, last_name, email)
    VALUES (?, ?, ?)
''', customers)


# orders
orders = []
for _ in range(100):  # Generate 100 orders
    order_date = fake.date_this_year()
    status = random.choice(['Processing', 'Shipped', 'Delivered'])
    customer_id = random.randint(1, 50)  # Link the order to a random customer
    orders.append((order_date, status, customer_id))

cursor.executemany('''
    INSERT INTO orders (order_date, status, customer_id)
    VALUES (?, ?, ?)
''', orders)

#order details
order_products = []
for order_id in range(1, 101):  # Orders are numbered 1 to 100
    num_items = random.randint(1, 5)  # Each order can have 1 to 5 items
    for _ in range(num_items):
        product_id = random.randint(1, 200)  # Choose a random product
        quantity = random.randint(1, 3)  # Each order will have 1 to 3 quantities of the product
        price = round(random.uniform(50.0, 1000.0), 2)  # Random price for each product
        order_products.append((order_id, product_id, quantity, price))

cursor.executemany('''
    INSERT INTO order_products (order_id, product_id, quantity, price)
    VALUES (?, ?, ?, ?)
''', order_products)

# commit and close

conn.commit()
conn.close()