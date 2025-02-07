# WAF that replace all occurrences of “java” with “python” in above file.

with open("practice.txt", "r") as f:
    data = f.read()

data = data.replace("java", "python").replace("Java", "Python")

with open("practice.txt", "w") as f:
    f.write(data)

with open("practice.txt", "r") as f:
    print(f.read())
