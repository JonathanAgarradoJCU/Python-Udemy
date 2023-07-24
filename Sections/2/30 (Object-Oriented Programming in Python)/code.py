class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)
    

student = Student("Bob", (95.4, 90.1, 93.0, 78.7, 90))
student2 = Student("Rolf", (49.5, 88.7, 92.3, 99.6, 86.9))

print(student.name)
print(f"Your grade scores are: {student.grades}")
print(f"Your average score is: {Student.average(student):.2f}")

print()

print(student2.name)
print(f"Your grade scores are: {student2.grades}")
print(f"Your average score is: {Student.average(student2):.2f}")
