# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

mySet = {9, "9.0"}
print(mySet)

#Another Solution
mySet2={
    ("int",9),
    ("float",9.0)
}
print(mySet2)