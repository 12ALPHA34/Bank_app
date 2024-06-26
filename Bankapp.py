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
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = 0.005
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        if super().deposit(amount):
            self._balance += amount
            self.interest_rate
            return True
        return False

    def withdraw(self, amount):
         if amount <= self.withdrawal_limit:
             return super().withdraw(amount)
         return False
        

    def _str_(self):
         return f"SavingsAccount({self.account_number}, Balance:{self._bjalance})"

    #Lahanre
class CurrentAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def __str__(self):
        return f"CurrentAccount({self.account_number}, Balance: {self._balance})"

#YakongDaniel
class ChildrensAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = 0.007

    def deposit(self, amount):
        if super().deposit(amount):
            self._balance += amount * self.interest_rate
            return True
        return False

    def withdraw(self, amount):
        return False  # No withdrawals allowed

    def __str__(self):
        return f"ChildrensAccount({self.account_number}, Balance: {self._balance})"

# Simon Joshua 
class StudentAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.withdrawal_limit = 2000
        self.deposit_limit = 50000

    def deposit(self, amount):
        if amount <= self.deposit_limit:
            return super().deposit(amount)
        return False

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            return super().withdraw(amount)
        return False

    def __str__(self):
        return f"StudentAccount({self.account_number}, Balance: {self._balance})"
