from billing import calculate_bill
from discounts import get_discount


def run_tests():
    cart = [
        {"name": "Milk", "price": 55.0, "quantity": 2},
        {"name": "Chips", "price": 20.0, "quantity": 3}
    ]

    bill = calculate_bill(cart, 200)

    assert bill["subtotal"] == 170.0
    assert bill["discount"] == 0
    assert bill["grand_total"] == 178.5
    assert bill["change"] == 21.5

    assert get_discount(400) == 0
    assert get_discount(500) == 25
    assert get_discount(1000) == 100

    print("All basic tests passed.")


if __name__ == "__main__":
    run_tests()
