# WAP to check if a list contain a palindrome of elements.
a = [1, 2, 3, 2, 1]
b = [1, "abc", "abc", 1]
c = [1, 2, 3, 4, 3, 5, 1]

if a == a[::-1]:
    print(True)
else:
    print(False)

if b == b[::-1]:
    print(True)
else:
    print(False)

if c == c[::-1]:
    print(True)
else:
    print(False)
