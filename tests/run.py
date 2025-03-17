from src.payment_system import create_account, check_balance, transfer_funds, view_transaction_history

def main():
    while True:
        print("\n--- Payment System ---")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Transfer Funds")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            create_account(name, balance)

        elif choice == '2':
            user_id = int(input("Enter user ID: "))
            check_balance(user_id)

        elif choice == '3':
            from_user = int(input("Enter sender user ID: "))
            to_user = int(input("Enter recipient user ID: "))
            amount = float(input("Enter transfer amount: "))
            transfer_funds(from_user, to_user, amount)

        elif choice == '4':
            view_transaction_history()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
