# Search for a number x in this tuple using while loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

myTuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(myTuple)

a = int(input("Enter a no. :"))
index = 0
while index < len(myTuple):
    if a == myTuple[index]:
        print(f"Found at {index} position")
        break
    else:
        print("finding...")
    index += 1
