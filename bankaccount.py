class BankAccount:
    def __init__(self, balance=0):
        if check_neg(balance):
            self.balance = balance

    def deposit(self, amount):
        if check_neg(amount):
            self.balance += amount

    def withdraw(self, amount):
        if check_neg(amount):
            self.balance -= amount

    def transfer(self, bank2, amount):
        if check_neg(amount):
            self.balance -= amount
            bank2.balance += amount


def check_neg(number):
    if number < 0:
        return False


a1 = BankAccount()
print(a1.balance)
a1.deposit(10)
print(a1.balance)
a2 = BankAccount(balance=20)
print(a2.balance)
a2.withdraw(15)
print(a2.balance)
a1.transfer(a2, 3)
print(a1.balance)
print(a2.balance)
