from abc import ABC, abstractmethod   #abstraction

# ================= Person Class =================
class Person(ABC):
    def __init__(self, name, age):
        self._name = name #protect
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 18 <= value <= 28:
            self._age = value
        else:
            raise ValueError("age must be between 18 and 28")

    @abstractmethod
    def display_info(self):
        pass



# ================= Student Class =====================
class Student(Person):
    def __init__(self, id, name, age, department, gpa):
        super().__init__(name, age)  #inhertance   #extend
        self.student_id = id
        self.__department = department
        self.gpa = gpa

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, new_dpt):
        self.__department = new_dpt

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0 <= value <= 4:
            self.__gpa = value
        else:
            raise ValueError("gpa must be between 0 and 4")

    def __str__(self):
        return f"Student_ID: {self.student_id} | Name:{self._name} | Age:{self.age} | Department:{self.department} | GPA:{self.gpa}"

    def display_info(self):
        return str(self)

# =============== Friend Functions & Pointer =========================
def update_student_name(student, new_name):
    ptr = student  # pointer

    print("\n[Pointer Check - Name]")
    print("ptr is student:", ptr is student)

    ptr._name = new_name


def update_student_gpa(student, new_gpa):
    ptr = student  # pointer

    print("\n[Pointer Check - GPA]")
    print("ptr is student:", ptr is student)

    ptr.gpa = new_gpa


def update_student_department(student, new_dpt):
    ptr = student  # pointer

    print("\n[Pointer Check - Department]")
    print("ptr is student:", ptr is student)

    ptr.department = new_dpt



# ================= Student Manager ======================
class StudentManager:
    def __init__(self):
        self.students = []

    # number of students
    def __len__(self):
        return len(self.students)

    # add student
    def add_student(self, student):
        self.students.append(student)
        print("student added successfully")

    # remove student
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("student removed successfully")
                return
        print("student not found")

    # display students
    def display_students(self):
        if not self.students:
            print("no students available")
            return

        list(map(lambda s: print(s), self.students))#lambda

