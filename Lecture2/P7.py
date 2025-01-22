# WAP to find the greatest of 3 numbers entered by the user.
a, b, c, d= (
    int(input("Enter num1: ")),
    int(input("Enter num2: ")),
    int(input("Enter num3: ")),
    int(input("Enter num4: ")),
)

if a >= b and a >= c and a>=d:
    print(f"{a} is greatest of all 4 numbers")
elif b >= c and b>=d and b >= a:
    print(f"{b} is greatest of all 4 numbers")
elif c >= d and c >= a and c>=b:
    print(f"{c} is greatest of all 4 numbers")
else:
    print(f"{d} is greatest of all 4 numbers")