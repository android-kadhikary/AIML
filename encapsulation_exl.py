class Account:
    def __init__(self, owner, balance):
        self.owner = owner        # Public attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

# Usage
acc = Account("John Doe", 1000)
print(acc.owner)           # Output: John Doe
print(acc.get_balance())   # Output: 1000

acc.deposit(500)
print(acc.get_balance())   # Output: 1500

acc.withdraw(200)
print(acc.get_balance())   # Output: 1300

# Direct access to private attribute will raise an AttributeError
#print(acc.__balance)     # Uncommenting this line will raise an AttributeError