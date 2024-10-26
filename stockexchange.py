info = '''
Given Orders
Id	Order Type	Action	Price	Quantity
001	Buy	Add	20.00	100
002	Sell	Add	25.00	200
003	Buy	Add	23.00	50
004	Buy	Add	23.00	70
005	Buy	Remove	23.00	50
006	Sell	Add	28.00	100
Requirements

    Create a data structure to store the orders.
    Implement Add and Remove operations.
    After placing an individual order, display the buy/sell orders with the best price.
    '''

from collections import defaultdict


class OrderBook:
    def __init__(self):
        self.buy_orders = defaultdict(list)
        self.sell_orders = defaultdict(list)
        self.orders_by_id = {}

    def add_order(self, order_id, order_type, price, quantity):
        order = {"id": order_id, "quantity": quantity}
        if order_type == 'Buy':
            self.buy_orders[price].append(order)
        elif order_type == 'Sell':
            self.sell_orders[price].append(order)

        self.orders_by_id[order_id] = {"order_type": order_type, "price": price, "quantity": quantity}

        print(f"Added {order_type} order - ID: {order_id}, Price: {price}, Quantity: {quantity}")
        self.display_best_orders()

    def remove_order(self, order_id):
        if order_id not in self.orders_by_id:
            print(f"Order ID {order_id} not found.")
            return

        order_details = self.orders_by_id[order_id]
        order_type = order_details["order_type"]
        price = order_details["price"]

        orders = self.buy_orders if order_type == 'Buy' else self.sell_orders
        orders[price] = [order for order in orders[price] if order["id"] != order_id]

        if not orders[price]:
            del orders[price]

        del self.orders_by_id[order_id]

        print(f"Removed {order_type} order - ID: {order_id}, Price: {price}")
        self.display_best_orders()

    def display_best_orders(self):

        if self.buy_orders:
            best_buy_price = max(self.buy_orders.keys())
            best_buy_orders = self.buy_orders[best_buy_price]
            print(f"Best Buy Price: {best_buy_price}")
            for order in best_buy_orders:
                print(f"   ID: {order['id']}, Quantity: {order['quantity']}")
        else:
            print("No Buy Orders Available")

        if self.sell_orders:
            best_sell_price = min(self.sell_orders.keys())
            best_sell_orders = self.sell_orders[best_sell_price]
            print(f"Best Sell Price: {best_sell_price}")
            for order in best_sell_orders:
                print(f"   ID: {order['id']}, Quantity: {order['quantity']}")
        else:
            print("No Sell Orders Available")
        print("\n")



order_book = OrderBook()


order_book.add_order("001", "Buy", 20.00, 100)
order_book.add_order("002", "Sell", 25.00, 200)
order_book.add_order("003", "Buy", 23.00, 50)
order_book.add_order("004", "Buy", 23.00, 70)
order_book.add_order("005", "Buy", 23.00, 50)
order_book.add_order("006", "Sell", 28.00, 100)


order_book.remove_order("003")
order_book.remove_order("002")
