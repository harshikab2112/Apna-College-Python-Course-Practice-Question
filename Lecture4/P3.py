# WAP to enter marks of 3 subjects from the user and
# store them in a dictionary.
# Start with an empty dictionary & add one by one.
# Use subject name as key & marks as value.
dict = {}
subject1 = int(input("Enter marks of Physics: "))
dict.update({"Physics": subject1})
subject2 = int(input("Enter marks of Chemistry: "))
dict.update({"Chemistry": subject2})
subject3 = int(input("Enter marks of Maths: "))
dict.update({"Maths": subject3})

print(dict)