class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")
        else:
            self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot deposit {amount}")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot withdraw {amount}")
        elif amount > self.balance:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")
        else:
            self.balance -= amount

    def transfer(self, bank2, amount):
        if amount < 0:
            raise ValueError(f"Cannot withdraw {amount}")
        elif amount > self.balance:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")
        else:
            self.balance -= amount
            bank2.balance += amount

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"


a1 = BankAccount()
print(a1.balance)
print(a1)
a1.deposit(10)
print(a1.balance)
a2 = BankAccount(balance=20)
print(a2.balance)
a2.withdraw(15)
print(a2.balance)
a1.transfer(a2, 3)
print(a1.balance)
print(a2.balance)
print(a2)
