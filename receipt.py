from discounts import get_discount_message


def print_receipt(customer_name, bill):
    print("\n" + "=" * 45)
    print("              STORE RECEIPT")
    print("=" * 45)
    print(f"Customer: {customer_name}")
    print("-" * 45)

    for item in bill["items"]:
        amount = item["price"] * item["quantity"]
        print(
            f"{item['name']:<18} "
            f"{item['quantity']} x Rs.{item['price']:.2f} "
            f"= Rs.{amount:.2f}"
        )

    print("-" * 45)
    print(f"Subtotal:       Rs. {bill['subtotal']:.2f}")
    print(f"Discount:       Rs. {bill['discount']:.2f}")
    print(f"Tax (5%):       Rs. {bill['tax']:.2f}")
    print(f"Grand Total:    Rs. {bill['grand_total']:.2f}")
    print(f"Paid Amount:    Rs. {bill['paid_amount']:.2f}")

    if bill["change"] >= 0:
        print(f"Change:         Rs. {bill['change']:.2f}")
        print("Payment status: PAID")
    else:
        print(f"Amount Due:     Rs. {-bill['change']:.2f}")
        print("Payment status: NOT ENOUGH")

    print(get_discount_message(bill["discount"]))
    print("=" * 45)
