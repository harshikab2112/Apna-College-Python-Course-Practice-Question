# WAF to print the elements of a list in a single line. ( list is the parameter)

# User-defined list
a = input("Enter your list here(separated by space): ")
myList = a.split()  # But this will treat every value as string

# Already defined list
b = [5, 3, "Riya", "Miya", True, 2.34]


def print_list(list):
    print(list)
    for i in list:
        print(i, end=" ")


print_list(myList)
print()
print_list(b)
