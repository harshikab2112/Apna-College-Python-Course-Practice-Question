# Print the multiplication table of a number n.(while)

a = int(input("Enter a no.: "))
i = 1
while i <= 10:
    print(f"{a} X {i} = {a*i}")
    i += 1
