# WAP factorial using recursive function.

num = int(input("Enter a no.: "))


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(f"Factorial of {num} is {factorial(num)}")
