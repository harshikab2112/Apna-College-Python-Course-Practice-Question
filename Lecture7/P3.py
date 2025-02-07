# Search if the word “learning” exists in the file or not.

with open("practice.txt", "r") as f:
    data = f.read()

if "learning" in data:
    print(True)
else:
    print(False)
