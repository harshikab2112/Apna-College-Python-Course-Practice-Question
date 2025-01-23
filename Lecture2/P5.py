# WAP to find the greatest of 3 numbers entered by the user.
a, b, c = (
    int(input("Enter num1: ")),
    int(input("Enter num2: ")),
    int(input("Enter num3: ")),
)

if a >= b and a >= c:
    print(f"{a} is greatest of all 3 numbers")
elif b >= c and b >= a:
    print(f"{b} is greatest of all 3 numbers")
else:
    print(f"{c} is greatest of all 3 numbers")
