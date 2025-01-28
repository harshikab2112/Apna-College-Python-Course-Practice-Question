# WAF to print the length of a list. ( list is the parameter)

# User-defined list
a = input("Enter your list here(separated by space): ")
myList = a.split()  # But this will treat every value as string

# Already defined list
b = [5, 3, "Riya", "Miya", True, 2.34]


def length_list(list):
    print(list)
    return len(list)


print("Length of the list is:", length_list(myList))
print("Length of the list is:", length_list(b))
