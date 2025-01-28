# Write a function to check if no. is odd or even.

num = int(input("Enter a number: "))


def even_odd(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


print(f"{num} is {even_odd(num)}")
