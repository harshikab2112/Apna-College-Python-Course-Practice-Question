# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.
my_List = [5, 3, "Riya", "Miya", True, 2.34]


def list_ele(list, index=0):
    if index == len(list):
        return
    print(list[index])
    list_ele(list, index + 1)


print(f"Elements are: {list_ele(my_List)}")
