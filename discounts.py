def get_discount(total):
    if total >= 1000:
        return total * 0.10
    elif total >= 500:
        return total * 0.05
    else:
        return 0


def get_discount_message(discount):
    if discount > 0:
        return f"You saved Rs. {discount:.2f} with the discount."
    return "No discount was applied."
