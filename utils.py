def get_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a whole number.")


def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Amount cannot be negative.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")
