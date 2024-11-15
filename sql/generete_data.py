import random
from faker import Faker
from db_config import connect_to_db

fake = Faker()

# Generate sample data
def generate_users(n=50):
    users = []
    for _ in range(n):
        users.append((fake.user_name(), fake.email()))
    return users

def generate_products(n=50):
    products = []
    for _ in range(n):
        products.append((fake.word(), round(random.uniform(5, 500), 2), random.randint(10, 100)))
    return products


def insert_data():
    connection = connect_to_db()
    cursor = connection.cursor()

    # Insert users
    users = generate_users()
    cursor.executemany("INSERT INTO users (username, email) VALUES (%s, %s)", users)

    # Insert products
    products = generate_products()
    cursor.executemany("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", products)

    connection.commit()
    cursor.close()
    connection.close()

# insert_data()

def generate_orders_and_details():
    connection = connect_to_db()
    cursor = connection.cursor()

    # Get user and product IDs
    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT id FROM products")
    product_ids = [row[0] for row in cursor.fetchall()]

    orders = []
    order_details = []

    for _ in range(50):  # 50 orders
        user_id = random.choice(user_ids)
        orders.append((user_id,))

    cursor.executemany("INSERT INTO orders (user_id) VALUES (%s)", orders)

    cursor.execute("SELECT id FROM orders")
    order_ids = [row[0] for row in cursor.fetchall()]

    for order_id in order_ids:
        for _ in range(random.randint(1, 5)):  # 1-5 products per order
            product_id = random.choice(product_ids)
            quantity = random.randint(1, 10)
            price = random.uniform(5, 500)  # Random price for learning
            order_details.append((order_id, product_id, quantity, round(price, 2)))

    cursor.executemany(
        "INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
        order_details,
    )

    connection.commit()
    cursor.close()
    connection.close()

generate_orders_and_details()