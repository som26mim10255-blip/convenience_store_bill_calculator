PRODUCTS = {
    1: {"name": "Milk", "price": 55.0},
    2: {"name": "Bread", "price": 40.0},
    3: {"name": "Biscuits", "price": 30.0},
    4: {"name": "Chips", "price": 20.0},
    5: {"name": "Cold Drink", "price": 45.0},
    6: {"name": "Chocolate", "price": 60.0},
    7: {"name": "Noodles", "price": 35.0},
    8: {"name": "Soap", "price": 38.0},
    9: {"name": "Toothpaste", "price": 75.0},
    10: {"name": "Water Bottle", "price": 20.0},
}


def show_products():
    print("\nAvailable Products")
    print("-" * 35)
    print("ID   Product              Price")
    print("-" * 35)

    for product_id, product in PRODUCTS.items():
        print(
            f"{product_id:<4} {product['name']:<20} "
            f"Rs. {product['price']:.2f}"
        )


def get_product(product_id):
    return PRODUCTS.get(product_id)
