"""
File: shopping_cart.py
Author: Dallin Williams

Purpose: Use lists and loops to store items with assigned integers and display the list of items and the sum of their integers.
"""

items = []
prices = []
total_item = 0
total_price = 0

user_input_menu = 0
user_input_item = ""
user_input_number = 0

while user_input_menu != 5:

    print()
    print("Welcome to the Shopping Cart Program!\n")

    print("""
    Please Select One of the Following:\n
    1. Add Item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit\n
    """)

    user_input_menu = int(input("Please enter an action: "))

    if user_input_menu == 1:
        user_input_item = input("What item would you like to add?: ")
        user_input_price = float(input(f"What is the price of '{user_input_item}'?: $"))

        items.append(user_input_item)  # .append() adds item to the end of the list
        prices.append(user_input_price)
        print(f"'{user_input_item}' has been added to the cart!")
    
    elif user_input_menu == 2:

        if items == [] and prices == []:
            print("The cart is empty. ")
        
        else:
            print("\nYour Cart:\n ")

            for index in range(len(items)) and range(len(prices)):  # counts items, matches items with prices, and displays them in list format
                item = items[index]
                price = prices[index]

                print(f"{index + 1}. {item} - ${price:.2f}")
        
    elif user_input_menu == 3:
        user_input_number == int(input("Which item would you like to remove?: "))

        items.pop(user_input_number - 1)  # .pop() removes item from the list
        prices.pop(user_input_number - 1)

        print("Item Removed.")
    
    elif user_input_menu == 4:
        for number in prices:
            total_price += number  # sums the prices list
        
        print(f"Your total is: ${total_price:.2f}")

    elif user_input_menu == 5:
        for number in range(len(items)):  # counts how many objects in items list
            total_item = number
        
        if total_item == 0 and items == [] and prices == []:
            print("The cart is empty.")
        
        else:
            print(f"There are {total_item + 1} items in the cart. ")  # +1 because list indexes at 0

print("\nThank you for shopping with us!\n")
print("Goodbye!\n")