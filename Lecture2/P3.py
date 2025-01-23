marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif marks < 70:
    grade = "D"

print("Grade of the student is", grade)
