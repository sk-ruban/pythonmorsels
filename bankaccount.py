class BankAccount:
    number = 1
    accounts = []

    def __init__(self, balance=0):
        if balance < 0:
            # Bonus 1 - Raise ValueError for negative checks
            raise ValueError(f"Can't open account with {balance} balance")
        else:
            self._balance = balance
        # Bonus 2 - Assign unique account number (Differentiate Class & Object - self)
        self.number = BankAccount.number
        BankAccount.number += 1
        BankAccount.accounts.append(self)

    # Bonus 3 - @property creates a read-only attribute (Remember to _balance the rest)
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Can't deposit {amount}")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")
        elif amount > self.balance:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")
        else:
            self._balance -= amount

    def transfer(self, bank2, amount):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")
        elif amount > self._balance:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")
        else:
            self._balance -= amount
            bank2._balance += amount

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"


account1 = BankAccount()
print(BankAccount.accounts)
account2 = BankAccount(100)
print(BankAccount.accounts)
print(account1.number)
print(account2.number)
account1.deposit(400)
print(account1)
account1.transfer(account2, 20)
