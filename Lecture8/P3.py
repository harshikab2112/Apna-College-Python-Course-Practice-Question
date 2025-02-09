# Create methods for debit, credit & printing the balance.


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Credited: ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid amount. Please enter a positive value.")

    def debit(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Debited: ${amount}. New Balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive value.")

    def print_balance(self):
        print(f"Current Balance: ${self.balance}")


# Example usage
account = BankAccount(1000)  # Starting with $1000
account.credit(500)
account.debit(300)
account.print_balance()
