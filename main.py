# Alpha Jesse
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account({self.account_number}, Balance: {self._balance})"

# Azi Zachariah
class SavingsAccount(Account):
    def_init_(self, account_number, balance=0):

super()._init_(acount_number, balance)
    self.interest_rate = 0.5
    self.withdrawal_limit = 700000

    def deposit(self, amount):
        if super().deposit(amount):
            self._balance += amount
    self.interest_rate
            return True
        return False

    def withdraw(self, amount):
         if amount <=
self.withdrawal_limit:
             return
super().withdraw(amount)
         return False

    def_str_(self):
         return f"SavingsAccount({self.account_number}, Balance:{self._balance})"
