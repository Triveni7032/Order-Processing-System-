# Order Processing System
# Demonstrating Iterators and Generators


orders = [
    {"order_id": 101, "customer": "Rahul", "amount": 1500},
    {"order_id": 102, "customer": "Priya", "amount": 2500},
    {"order_id": 103, "customer": "Arjun", "amount": 1200},
    {"order_id": 104, "customer": "Sneha", "amount": 3000},
    {"order_id": 105, "customer": "Kiran", "amount": 1800}
]


# -------------------------------------------------
# 1. CUSTOM ITERATOR
# -------------------------------------------------

class OrderIterator:

    def __init__(self, orders):
        self.orders = orders
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.orders):
            raise StopIteration

        order = self.orders[self.index]
        self.index += 1

        return order


print("===== CUSTOM ITERATOR =====")

order_iterator = OrderIterator(orders)

for order in order_iterator:
    print(
        "Order ID:", order["order_id"],
        "| Customer:", order["customer"],
        "| Amount:", order["amount"]
    )


# -------------------------------------------------
# 2. GENERATOR
# -------------------------------------------------

def order_generator(orders):

    for order in orders:
        yield order


print("\n===== GENERATOR =====")

for order in order_generator(orders):
    print(
        "Processing Order:",
        order["order_id"],
        "| Customer:",
        order["customer"]
    )


# -------------------------------------------------
# 3. GENERATOR FOR HIGH-VALUE ORDERS
# -------------------------------------------------

def high_value_orders(orders, minimum_amount):

    for order in orders:

        if order["amount"] >= minimum_amount:
            yield order


print("\n===== HIGH-VALUE ORDERS =====")

for order in high_value_orders(orders, 2000):

    print(
        "Order ID:", order["order_id"],
        "| Amount:", order["amount"]
    )


# -------------------------------------------------
# 4. GENERATOR FOR ORDER AMOUNTS
# -------------------------------------------------

def order_amounts(orders):

    for order in orders:
        yield order["amount"]


print("\n===== ORDER AMOUNTS =====")

for amount in order_amounts(orders):
    print("₹", amount)