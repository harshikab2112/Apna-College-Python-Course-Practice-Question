# WAF to find the factorial of n. (n is the parameter)

n = int(input("Enter a number: "))


def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


print(f"Factorial of {n} is {factorial(n)}")
