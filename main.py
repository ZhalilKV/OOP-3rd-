from personal import PersonalAccount

if __name__ == "__main__":
    # Get account details from the user
    account_number = int(input("Enter your account number: "))
    account_holder = input("Enter your name: ")

    # Create a personal account
    account = PersonalAccount(account_number, account_holder)

    while True:
        print("\nOptions:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Print Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
            if amount <= account.get_balance():
                print(f"Withdrew: ${amount:.2f}")

        elif choice == '3':
            print(f"Current Balance: ${account.get_balance():.2f}")

        elif choice == '4':
            account.print_transaction_history()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")