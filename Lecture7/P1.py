# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

# Creating and writing to the file
with open("practice.txt", "w") as f:
    f.write(
        "Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java."
    )

# Reading and printing the file
with open("practice.txt", "r") as f:
    print(f.read())
