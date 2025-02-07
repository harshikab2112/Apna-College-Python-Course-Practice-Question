# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.

line_num = 1
data = True
word = "learning"

with open("practice.txt", "r") as f:
    while data:
        data = f.readline()
        if word in data:
            print(line_num)
            break
        line_num += 1
    else:
        print(-1)
