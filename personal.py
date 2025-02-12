from amount import Amount


class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        self.balance += amount
        transaction = Amount(amount, 'DEPOSIT')
        self.transactions.append(transaction)

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
            return
        self.balance -= amount
        transaction = Amount(amount, 'WITHDRAWAL')
        self.transactions.append(transaction)

    def print_transaction_history(self):
        print(f"Transaction history for account {self.account_number} ({self.account_holder}):")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number: int):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    def __add__(self, amount: float):
        self.deposit(amount)

    def __sub__(self, amount: float):
        self.withdraw(amount)