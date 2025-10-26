# CLOUD BAKERY PROGRAM

##################################################################################################################


def welcome_message():
    print('**********************************************')
    print('*                                            *')
    print('*        WELCOME TO CLOUD BAKERY             *')
    print('*                                            *')
    print('*  1. TO OPEN MENU (PRESS m)                 *')
    print('*  2. FOR HELPLINE (PRESS h)                 *')
    print('*  3. FEEDBACK & REVIEW (PRESS r)            *')
    print('*                                            *')
    print('**********************************************')


###################################################################################################################


#  Global product dictionary
product = {
    "🍞 Bread Loaf": 40,
    "🥐 Croissant": 60,
    "🧁 Cupcake": 50,
    "🍪 Chocolate Chip Cookie": 30,
    "🍰 Strawberry Cake Slice": 90,
    "🥖 French Baguette": 55,
    "🍩 Donut": 45,
    "🥧 Apple Pie": 80,
    "🥯 Bagel": 35,
    "☕ Coffee": 70
}

##################################################################################################################


def menu():
    print("\n 👩‍🍳 CLOUD BAKERY MENU 👩‍🍳 \n")
    print("--------------------------------")

    for item in product:
        print(f"{item}: ₹{product[item]}")

    my_order = {}  # Initialize here
    global qn1

    print("--------------------------------")
    qn1 = input("Would you like to place an order? (y/n): ").lower()
    if qn1 != 'y':
        print("Thanks for visiting! Have a good day 😊")
    else:
        for item in product:
            x = input(f"Enter the quantity of {item} or (press 'exit' to stop): ")
            if x.lower() == 'exit':
                break

            if not x.isdigit():
                print("Please enter a valid number.")
                continue

            qty = int(x)
            my_order[item] = qty

        # Display only names with quantities
        print("___________________________")
        print("\n🧾 Your Order Summary :-\n")
        for item, qty in my_order.items():
            print(f"{item} x {qty}")
        print("___________________________")
        print("\n✅ Your order has been placed successfully!")

        total = 0
        for item, qty in my_order.items():
            price = product[item] * qty
            total += price
        print(f"💰 Total Bill Amount: ₹{total}\n")

    return my_order


##################################################################################################################


def my_orders(order):
    if not order:
        print("\nNo items ordered ❌.\n")
        return

    print("———————————————————————————")
    print("\n🧾 Final Billing Summary:\n")
    total = 0
    for item, qty in order.items():
        price = product[item] * qty
        print(f"{item} × {qty} = ₹{price}")
        total += price

    print("———————————————————————————")
    print(f"💰 Total Bill: ₹{total}")
    print("\n✅ Thank you for your order!\n")


##################################################################################################################


# main program execution

order = {}

while True:
    welcome_message()

    choice = input("Enter your choice (m/h/r): ").lower()

    if choice == 'm':
        order = menu()
        show = ''

        if qn1 != 'y':
            print()
        else:
            show = input("Would you like to view your orders and final bill ? (y/n): ").lower()
            
            if show == 'y':
                my_orders(order)
            else:
                print('Thanks for visiting! Have a good day 😊\n')
        

    elif choice == 'h':
        print("\n📞 Helpline Number: 1800-123-BAKE (2253)")
        print("⏰ Available 24/7 for your assistance!\n")

    elif choice == 'r':
        feedback = \
        input("On a scale of 1-5, how would you rate our service ? ") 
        input("Would you recommend us to others? (y/n): ") 
        input("Any suggestions for improvement ? \n") 
        print("🙏 Thank you for your valuable feedback!\n")
        print(f'{feedback} /5 is noted. We appreciate your input! 😊\n')
    else:
        print("Invalid choice! Please restart the program and try again.")

    cont = input("Would you like to continue? (y/n): ").lower()
    if cont != 'y':
        print("Thanks for visiting! Have a good day 😊")
        break


##################################################################################################################

