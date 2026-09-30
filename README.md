# convenience_store_bill_calculator
A simple Python-based billing system for a convenience store. It allows users to view products, add or remove items from a cart, calculate discounts and tax, view order summaries, and generate the final bill with basic input validation and testing.
Main features

Show the products available in the store.

Add one or more products to a shopping cart.

View the current cart and its total.

Automatically calculate discount and 5% tax.

Enter the amount paid and calculate change or remaining amount.

Print a simple receipt.

Run a few basic tests.

Functional modules

products.py - stores the product list and displays products.

cart.py - handles adding products and showing the cart.

discounts.py - applies the discount rules.

billing.py - performs subtotal, tax, total and change calculations.

receipt.py - prints the final receipt.

utils.py - handles simple input validation.

config.py - stores small project settings.

main.py - connects the modules and runs the menu.

test_bill.py - checks the main calculations.

Discount rules

Below Rs. 500: no discount

Rs. 500 to Rs. 999.99: 5% discount

Rs. 1000 or above: 10% discount

After the discount, 5% tax is added.

How to run

Make sure Python 3 is installed.

Open the project folder in a terminal and run:

python main.py

To run the tests:

python test_bill.py

No external Python packages are required.

Example flow

The program first shows a menu. A user can see the products, add products to the cart, check the cart, and generate a bill.

For example, if a customer buys 2 milk packets and 3 packets of chips, the program calculates the subtotal, checks the discount, adds tax, and then calculates the change from the amount paid.

Project level

This project is deliberately not over-complicated. It is meant to show that the basic Python concepts taught in the course can be used to solve a small real-life problem.
