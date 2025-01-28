# WAF to convert USD to INR.

n = float(input("Enter the USD amount: "))


def usd_to_inr(n):
    current_exchange_rate = 86.3675
    return n * current_exchange_rate


print(f"{n}USD = {usd_to_inr(n):.2f}INR.")
