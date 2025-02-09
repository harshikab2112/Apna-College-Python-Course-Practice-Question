# Create Account class with 2 attributes - name, balance & account no.


class Account:
    def __init__(self, name, balance, account_no):
        self.name = name
        self.balance = balance
        self.account_no = account_no

    def print_details(self):
        print(f"{self.name} account details:")
        print(f"Account no. is {self.account_no:,}")
        print(f"Current Balance is {self.balance:,.2f}")


account1 = Account("Riya", 683469918164862, 919291794991)

account1.print_details()
