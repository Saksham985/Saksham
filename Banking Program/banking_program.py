import os
import json


# Get the absolute path of the folder where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create a path for the data file inside that folder
DATA_FILE = os.path.join(BASE_DIR, "bank_data.json")


# ---- Utility Functions ----
def load_data():
    """Load account data from file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}


def save_data(data):
    """Save all account data to file"""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def options():
    print("""
    ***************************************
    User options ->
    1. Check Balance (press 1)
    2. Withdraw money (press 2)
    3. Deposit money (press 3)
    4. Transaction history (press 4)
    5. My savings (press 5)
    6. Exit to main window (press "e")
    ***************************************
    """)


def calculate_interest(principal, rate, time):
    """Calculate simple interest"""
    return (principal * rate * time) / 100


def savings_menu():
    print("""
    ----- My Savings Options -----
    1. Create Savings Goal
    2. View Savings Account
    3. Calculate Interest
    4. Deposit to Savings
    5. Back to Main Menu
    ------------------------------
    """)


# ---- Banking Logic ----
def user_dashboard(account_id, accounts):
    account = accounts[account_id]

    while True:
        options()
        selection = input("Enter the option: ").lower()

        if selection == "e":
            print("Thanks for visiting! Goodbye 😃")
            break

        elif selection == "1":
            print(f"Your current balance: ₹{account['balance']}")

        elif selection == "2":  # Withdraw
            try:
                withdraw = float(input("Enter amount to withdraw ₹: "))
                if withdraw > account["balance"]:
                    print("You have insufficient funds.")
                else:
                    account["balance"] -= withdraw
                    account["transactions"].append(f"Withdrawn: ₹{withdraw}")
                    print(f"Withdrawal successful! Current balance: ₹{account['balance']}")
                    save_data(accounts)
            except ValueError:
                print("Invalid amount. Try again!")

        elif selection == "3":  # Deposit
            try:
                deposit = float(input("Enter amount to deposit ₹: "))
                account["balance"] += deposit
                account["transactions"].append(f"Deposited: ₹{deposit}")
                print(f"Deposit successful! Current balance: ₹{account['balance']}")
                save_data(accounts)
            except ValueError:
                print("Invalid amount. Try again!")

        elif selection == "4":  # Transaction history
            print("\nYour Transaction History:")
            if not account["transactions"]:
                print("No transactions yet.")
            else:
                for t in account["transactions"]:
                    print(" •", t)

        elif selection == "5":  # Savings section
            handle_savings(account_id, accounts)

        else:
            print("Invalid option selected. Try again.")


def handle_savings(account_id, accounts):
    account = accounts[account_id]

    while True:
        savings_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            goal_name = input("Enter goal name (e.g., Car, House): ")
            target_amount = float(input("Enter target amount ₹: "))
            account["savings"][goal_name] = {"target": target_amount, "current": 0}
            print(f"Savings goal '{goal_name}' created!")
            save_data(accounts)

        elif choice == "2":
            if not account["savings"]:
                print("No savings goals yet!")
            else:
                print("\n----- Your Savings Goals -----")
                for goal, details in account["savings"].items():
                    progress = (details["current"] / details["target"]) * 100
                    print(f"{goal}: ₹{details['current']}/₹{details['target']} ({progress:.1f}%)")

        elif choice == "3":
            try:
                amount = float(input("Enter principal amount ₹: "))
                rate = float(input("Enter interest rate (%): "))
                time = float(input("Enter time period (years): "))
                interest = calculate_interest(amount, rate, time)
                print(f"Your interest earned will be ₹{interest:.2f}")
            except ValueError:
                print("Invalid input! Try again.")

        elif choice == "4":
            if not account["savings"]:
                print("No savings goals exist! Create one first.")
                continue

            print("\nAvailable Goals:")
            for goal in account["savings"]:
                print(f"- {goal}")

            goal_name = input("\nEnter goal name to deposit to: ")
            if goal_name in account["savings"]:
                deposit_amount = float(input("Enter amount to deposit ₹: "))
                account["savings"][goal_name]["current"] += deposit_amount
                print(f"Successfully deposited ₹{deposit_amount} to {goal_name}")
                save_data(accounts)
            else:
                print("Goal not found!")

        elif choice == "5":
            break

        else:
            print("Invalid choice! Try again.")


# ---- Main Menu ----
def main_menu():
    print("\n-----------------🏦 WELCOME TO PY BANK MENU 🏦-------------------\n")
    accounts = load_data()

    while True:
        print("""
        Select operation -->
        1. To Create an account (press "c")
        2. Existing user (press "eu")
        3. Exit (press "e")
        """)
        select = input("Enter your desired operation: ").lower()

        if select == "e":
            print("Bye! Have a cheerful day 🙋")
            save_data(accounts)
            break

        elif select == "c":
            account_id = input("Enter your account ID: ")

            if account_id in accounts:
                print("❌ Account ID already exists! Try a different one.")
                continue

            user_name = input("Enter account holder's name: ")
            password = input("Enter your password: ")

            # Ensure unique password
            if any(acc["password"] == password for acc in accounts.values()):
                print("❌ Password already taken! Choose a different one.")
                continue

            accounts[account_id] = {
                "name": user_name,
                "password": password,
                "balance": 0,
                "transactions": [],
                "savings": {},
            }

            save_data(accounts)
            print("\n🎉 Congrats! Account successfully created!")
            user_dashboard(account_id, accounts)

        elif select == "eu":
            account_id = input("Enter your account ID: ")
            password = input("Enter password: ")

            if account_id in accounts and accounts[account_id]["password"] == password:
                print(f"Welcome back, {accounts[account_id]['name']}!")
                user_dashboard(account_id, accounts)
            else:
                print("❌ Invalid account ID or password!")

        else:
            print("Invalid input! Try again.")


# Run Program
main_menu()
