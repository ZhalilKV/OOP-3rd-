Enter your account number: 123456
Enter your name: John Doe

Options:
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Print Transaction History
5. Exit
Choose an option (1-5): 1
Enter amount to deposit: 1000
Deposited: $1000.00

Options:
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Print Transaction History
5. Exit
Choose an option (1-5): 3
Current Balance: $1000.00

Options:
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Print Transaction History
5. Exit
Choose an option (1-5): 2
Enter amount to withdraw: 200
Withdrew: $200.00

Options:
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Print Transaction History
5. Exit
Choose an option (1-5): 3
Current Balance: $800.00

Options:
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Print Transaction History
5. Exit
Choose an option (1-5): 4
Transaction history for account 123456 (John Doe):
DEPOSIT: $1000.00 on 2023-10-01 12:00:00
WITHDRAWAL: $200.00 on 2023-10-01 12:05:00

Options:
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Print Transaction History
5. Exit
Choose an option (1-5): 2
Enter amount to withdraw: 900
Insufficient funds for withdrawal.

Options:
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Print Transaction History
5. Exit
Choose an option (1-5): 5
Exiting the program.



Encapsulation in Python is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (variables) and methods (functions) that operate on that data into a single unit, typically a class. Encapsulation helps to restrict direct access to some of an object's components, which can prevent accidental modification and ensure data integrity.

Key Aspects of Encapsulation in Python
Public Members: These can be accessed from anywhere.
Protected Members: Indicated by a single underscore (_variable), they are intended to be used within the class and its subclasses.
Private Members: Indicated by a double underscore (__variable), they are not directly accessible outside the class.
