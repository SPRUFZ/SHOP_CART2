#this code uses a product dictionary and a cart dictionary to manage
# a customers shopping experience, including adding, removing, viewing,
# and checking out items.

from datetime import date

# create the store inventory dictionary with five product names and prices.
products = {
    "Chips": 2.00,
    "Soda": 2.50,
    "Cookies": 3.25,
    "Granola Bar": 1.75,
    "Juice": 4.00
}

# create the empty shopping cart dictionary.
# keys are product names and values are quantities as positive integers.
shopping_cart = {}


# Func: display_products
# Purp: Show all inventory items with a numbered list using a for loop.
# Parameters: product_dict (dictionary of products and prices)
# Return: none
# This function uses products.items() to show each product and its price.
def display_products(product_dict):
    print("\n========== AVAILABLE PRODUCTS ==========")
    # Use a for loop to cycle through each product and price in the inventory.
    for index, (product_name, price) in enumerate(product_dict.items(), start=1):
        print(f"{index}. {product_name:<12} ${price:.2f}")


# Func: add_product
# Purp: Validate product selection and quantity, then add or update cart entries.
# Parameters: product_dict, cart_dict
# Return: none
# This function validates the product number with a while loop and the quantity with another.
def add_product(product_dict, cart_dict):
    # Show the available products so the customer can pick one.
    display_products(product_dict)
    product_names = list(product_dict.keys())

    # Validate the product number before accessing the product dictionary.
    while True:
        try:
            product_choice = int(input("Enter product number: "))
        except ValueError:
            print("Invalid input. Please enter a number from the list.")
            continue

        if 1 <= product_choice <= len(product_names):
            selected_product = product_names[product_choice - 1]
            break
        print("Invalid product number. Please choose a valid item.")

    # Validate quantity so it is greater than zero.
    while True:
        try:
            quantity = int(input(f"How many {selected_product} would you like to add? "))
        except ValueError:
            print("Quantity must be a whole number.")
            continue

        if quantity > 0:
            break
        print("Quantity must be greater than 0.")

    # If the item is already in the cart, add the new quantity to the existing amout.
    cart_dict[selected_product] = cart_dict.get(selected_product, 0) + quantity
    print(f"Added {quantity} {selected_product} to your cart!")
    print(f"{selected_product} quantity is now {cart_dict[selected_product]}.")


# Func: remove_product
# Purp: Remove one unit from a selected cart item or delete the item if its quantity becomes zero.
# Parameters: cart_dict, product_dict
# Return: none
# This function also validates the customer selection and checks if the cart is empty.
def remove_product(cart_dict, product_dict):
    if not cart_dict:
        print("Your cart is empty. There is nothing to remove.")
        return

    print("\n========== YOUR SHOPPING CART ==========")
    cart_items = list(cart_dict.items())

    # Display the current cart items and their quantities using a for loop.
    for index, (product_name, quantity) in enumerate(cart_items, start=1):
        print(f"{index}. {product_name} - Quantity: {quantity}")

    # Validate the product choice from the current cart list.
    while True:
        try:
            remove_choice = int(input("Enter item number to remove: "))
        except ValueError:
            print("Invalid input. Please enter a valid cart item number.")
            continue

        if 1 <= remove_choice <= len(cart_items):
            selected_product = cart_items[remove_choice - 1][0]
            break
        print("Invalid item number. Please select an item from the cart.")

    # Remove one unit and delete the item if its quantity reaches zero.
    if cart_dict[selected_product] > 1:
        cart_dict[selected_product] -= 1
        print(f"Removed 1 {selected_product} from your cart!")
        print(f"{selected_product} quantity is now {cart_dict[selected_product]}.")
    else:
        del cart_dict[selected_product]
        print(f"Removed 1 {selected_product} from your cart!")
        print(f"{selected_product} was removed from your cart.")


# Func: display_cart
# Purp: Print the cart with unit price, quantity, and line total for each item.
# Parameters: cart_dict, product_dict
# Return: none
# This function loops through cart items and uses product prices from the products dictionary.
def display_cart(cart_dict, product_dict):
    if not cart_dict:
        print("\nYour cart is empty.")
        return

    total_items = 0
    subtotal = 0.0

    print("\n========== YOUR SHOPPING CART ==========")
    print(f"{'Product':<12} {'Unit Price':>12} {'Quantity':>10} {'Line Total':>12}")

    # Use a for loop with shopping_cart.items() to access quantities and prices.
    for index, (product_name, quantity) in enumerate(cart_dict.items(), start=1):
        unit_price = product_dict[product_name]
        line_total = unit_price * quantity
        total_items += quantity
        subtotal += line_total
        print(f"{index}. {product_name:<10} ${unit_price:>7.2f} {quantity:>10} ${line_total:>9.2f}")

    print(f"\nTotal Items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")


# Func: calculate_total
# Purp: Sum the total price for every item in the cart.
# Parameters: cart_dict, product_dict
# Return: subtotal as a float
# This function calculates a running subtotal with a for loop.
def calculate_total(cart_dict, product_dict):
    subtotal = 0.0

    # Loop through each product in the cart and calculate price times quantity.
    for product_name, quantity in cart_dict.items():
        item_price = product_dict[product_name]
        subtotal += item_price * quantity

    return subtotal


# Func: calculate_discount
# Purp: Determine the percentage discount based on the total subtotal.
# Parameters: subtotal
# Return: discount_rate, amount_saved, final_total
# This function applies the discount rules required by the assignment.
def calculate_discount(subtotal):
    if subtotal < 10:
        discount_rate = 0.00
    elif subtotal < 20:
        discount_rate = 0.05
    elif subtotal < 40:
        discount_rate = 0.10
    else:
        discount_rate = 0.15

    amount_saved = subtotal * discount_rate
    final_total = subtotal - amount_saved
    return discount_rate, amount_saved, final_total


# Func: print_receipt
# Purp: Print a final receipt, including the date and discount information.
# Parameters: cart_dict, product_dict
# Return: none
# This function researches and uses the datetime module to display the current date.
def print_receipt(cart_dict, product_dict):
    if not cart_dict:
        print("Your cart is empty. Checkout cannot be completed.")
        return

    subtotal = calculate_total(cart_dict, product_dict)
    discount_rate, amount_saved, final_total = calculate_discount(subtotal)
    total_items = sum(cart_dict.values())
    current_date = date.today().strftime("%m/%d/%Y")

    print("\n========== RECEIPT ==========")
    print(f"Date: {current_date}")
    print()
    print(f"{'Product':<12} {'Unit Price':>12} {'Quantity':>10} {'Line Total':>12}")

    # Show each item in the cart with its unit price, quantity, and line total.
    for product_name, quantity in cart_dict.items():
        unit_price = product_dict[product_name]
        line_total = unit_price * quantity
        print(f"{product_name:<12} ${unit_price:>7.2f} {quantity:>10} ${line_total:>9.2f}")

    print()
    print(f"Total Items: {total_items:>6}")
    print(f"Subtotal:      ${subtotal:>8.2f}")
    print(f"Discount:      {discount_rate * 100:>5.0f}%")
    print(f"Amount Saved:  ${amount_saved:>8.2f}")
    print(f"Final Total:   ${final_total:>8.2f}")
    print()
    print("Thank you for shopping!")


# Main menu loop: this continues until a successful checkout ends the program.
while True:
    print("\n========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")

    # Validate the menu choice so only values 1 through 6 are accepted.
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number between 1 and 6.")
            continue

        if 1 <= choice <= 6:
            break
        print("Invalid choice. Please choose a number from 1 to 6.")

    # Use conditional logic to complete the customer's selection.
    if choice == 1:
        display_products(products)
    elif choice == 2:
        add_product(products, shopping_cart)
    elif choice == 3:
        remove_product(shopping_cart, products)
    elif choice == 4:
        display_cart(shopping_cart, products)
    elif choice == 5:
        current_total = calculate_total(shopping_cart, products)
        print(f"Current subtotal: ${current_total:.2f}")
    elif choice == 6:
        # Empty carts cannot be checked out.
        if not shopping_cart:
            print("Your cart is empty. Add products before checking out.")
            continue

        subtotal = calculate_total(shopping_cart, products)
        discount_rate, amount_saved, final_total = calculate_discount(subtotal)

        print("\n========== CHECKOUT ==========")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount: {discount_rate * 100:.0f}%")
        print(f"Amount Saved: ${amount_saved:.2f}")
        print(f"Final Total: ${final_total:.2f}")
        print_receipt(shopping_cart, products)
        break
