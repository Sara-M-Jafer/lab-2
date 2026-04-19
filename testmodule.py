from abc import ABC, abstractmethod   #abstraction
from functools import total_ordering
from dataclasses import dataclass

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
@total_ordering
class Student(Person):
    def __init__(self, id, name, age, department, gpa):
        super().__init__(name, age)  #inhertance   #extend
        self.student_id = id
        self.department = department
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
        return f"Student_ID: {self.student_id} | Name:{self._name} | Age:{self.age} | Department:{self.department} | GPA:{self.__gpa}"

    def display_info(self):
        return str(self)

# ====== Operator Overloading ======

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__gpa == other.gpa

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__gpa < other.__gpa

    def __iadd__(self, value):
        # Context-aware
        if isinstance(value, (int, float)):
            self.gpa += value
        elif isinstance(value, Student):
            self.gpa += value.gpa
        else:
            return NotImplemented
        return self

    def __bool__(self):
        return self.gpa >= 2

    # Immutable style
    def add_bonus(self, value):
        return Student(self.student_id, self._name, self.age, self.department, self.gpa + value)

    # def __iadd__(self, value):
    #
    #     self.__gpa += value
    #     return self
    #
    # def __bool__(self):
    #     return self.__gpa >= 2

# =============== Callable Object =================
class GPAChecker:
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val

    def __call__(self, student):
        return self.min <= student.gpa <= self.max


# =============== Pipe Operator =================
class Pipe:
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        return self.func(other)

    def __or__(self, other):
        return Pipe(lambda x: other.func(self.func(x)))


# =============== Friend Functions & Pointer =========================
def update_student_name(student, new_name):
    ptr = student

    print("\n[ Check - Name]")
    print("ptr is student:", ptr is student)

    ptr._name = new_name


def update_student_gpa(student, new_gpa):
    ptr = student

    print("\n[ Check - GPA]")
    print("ptr is student:", ptr is student)

    ptr.gpa = new_gpa


def update_student_department(student, new_dpt):
    ptr = student

    print("\n[ Check - Department]")
    print("ptr is student:", ptr is student)

    ptr.department = new_dpt


# ================= Student Manager ======================
class StudentManager:
    def __init__(self):
        self.students = []


    # number of students
    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        return self.students[index]

    def __contains__(self, student_id):
        return any(s.student_id == student_id for s in self.students)

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

        for s in self.students:
            print(s)

    #find student
    def find_student(self, student_id):
        result = list(filter(lambda s: s.student_id == student_id, self.students))
        return result[0] if result else None

# ================= Dataclass ======================
@dataclass(order=True)
class StudentRecord:
    student_id: int
    name: str
    gpa: float