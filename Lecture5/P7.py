# Search for a number x in this tuple using for loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

myTuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(myTuple)

a = int(input("Enter a no. :"))

for i in range(len(myTuple)):
    if a == myTuple[i]:
        print(f"Found at {i} position")
        break
    else:
        print("finding...")
print("End of Loooop")
