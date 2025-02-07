# From a file containing numbers separated by comma,
# print the count of even numbers.

with open("number.txt", "w") as f:
    f.write("12, 67, 34, 66, 90, 22, 123, 45, 64, 20, 30, 98")


with open("number.txt", "r") as f:
    data = f.read()
    count = 0
    num = data.split(",")
    for i in num:
        if int(i.strip()) % 2 == 0:
            count += 1
    print(count)
