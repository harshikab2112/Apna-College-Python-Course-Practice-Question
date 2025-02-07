# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.


class Student:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    def marks_average(self):
        average = (self.subject1 + self.subject2 + self.subject3) / 3
        print(f"Average score of {self.name} is {average:.2f}")


name1 = input("Enter Student Name:")
sub1 = int(input("Enter marks of first subject: "))
sub2 = int(input("Enter marks of second subject: "))
sub3 = int(input("Enter marks of third subject: "))

student1 = Student(name1, sub1, sub2, sub3)

student1.marks_average()
