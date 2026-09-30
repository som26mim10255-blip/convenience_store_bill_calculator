from products import show_products, get_product
from cart import add_item, show_cart, get_cart
from billing import calculate_bill
from receipt import print_receipt
from utils import get_integer, get_positive_number


def main():
    cart = []

    print("=" * 45)
    print("      CONVENIENCE STORE BILL CALCULATOR")
    print("=" * 45)

    while True:
        print("\n1. Show products")
        print("2. Add product to cart")
        print("3. View cart")
        print("4. Generate bill")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_products()

        elif choice == "2":
            show_products()
            product_id = get_integer("Enter product number: ")
            product = get_product(product_id)

            if product is None:
                print("Product not found.")
                continue

            quantity = get_integer("Enter quantity: ")

            if quantity <= 0:
                print("Quantity should be greater than 0.")
                continue

            add_item(cart, product, quantity)
            print("Product added to cart.")

        elif choice == "3":
            show_cart(cart)

        elif choice == "4":
            if not cart:
                print("Cart is empty. Add some products first.")
                continue

            customer_name = input("Enter customer name: ").strip()
            if customer_name == "":
                customer_name = "Customer"

            paid_amount = get_positive_number(
                "Enter amount paid by customer: "
            )

            bill = calculate_bill(cart, paid_amount)
            print_receipt(customer_name, bill)

        elif choice == "5":
            print("Thank you for using the Bill Calculator.")
            break

        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
