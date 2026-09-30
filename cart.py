def add_item(cart, product, quantity):
    for item in cart:
        if item["name"] == product["name"]:
            item["quantity"] += quantity
            return

    cart.append({
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    })


def show_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\nYour Cart")
    print("-" * 50)
    print("Product              Qty       Price")
    print("-" * 50)

    total = 0

    for item in cart:
        amount = item["price"] * item["quantity"]
        total += amount
        print(
            f"{item['name']:<20} "
            f"{item['quantity']:<9} "
            f"Rs. {amount:.2f}"
        )

    print("-" * 50)
    print(f"Cart total: Rs. {total:.2f}")