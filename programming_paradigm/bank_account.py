class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    
    def deposit(self, amount=0):
        if amount > 0:
            self.account_balance = self.account_balance + amount
            print(f"You deposited {amount} into your account")

    def withdraw(self, amount=0):
        if 0 < amount <= self.account_balance:
            self.account_balance = self.account_balance - amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current balance ${self.account_balance:.2f}")