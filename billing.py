from discounts import get_discount
from config import TAX_RATE


def calculate_subtotal(cart):
    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_bill(cart, paid_amount):
    subtotal = calculate_subtotal(cart)
    discount = get_discount(subtotal)
    amount_after_discount = subtotal - discount
    tax = amount_after_discount * TAX_RATE
    grand_total = amount_after_discount + tax
    change = paid_amount - grand_total

    return {
        "items": cart,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "grand_total": grand_total,
        "paid_amount": paid_amount,
        "change": change
    }
