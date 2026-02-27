class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def display_info(self):
    print(f"Name: {self.name} | Age: {self.age}")


class Student(Person):
    def __init__(self, student_id, name, age, department, gpa):
        super().__init__(name, age)
        self.student_id = student_id
        self.department = department
        self.gpa = gpa

    def display_info(self):
        super().display_info()
        print(f"Student_ID: {self.student_id} | Department: {self.department} | GPA:{self.gpa}")

class Teacher(Person):
    def __init__(self, teacher_id, name, age, department, salary):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.department = department
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Teacher ID: {self.teacher_id} | Department: {self.department} | Salary: {self.salary}")