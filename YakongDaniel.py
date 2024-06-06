Class ChildrensAccount(Account):
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
