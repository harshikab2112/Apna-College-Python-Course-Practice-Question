# Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter a number: "))


def sum_natural_num(n):
    if n==1:
        return 1
    return n+ sum_natural_num(n-1)


print(f"sum of first {n} natural numbers is:", sum_natural_num(n))
