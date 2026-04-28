from abc import ABC, abstractmethod
from dataclasses import dataclass

#============= logger mixin ================
class LoggerMixin:
    def log(self,message):
        print(f"[log]:{message}")

# ================= Person =================
class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

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

# ================= Student =====================
class Student(Person,LoggerMixin):
    def __init__(self, id, name, age, department, gpa):
        super().__init__(name, age)
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
        return f"Student_ID: {self.student_id} | Name:{self.name} | Age:{self.age} | Department:{self.department} | GPA:{self.gpa}"

    def display_info(self):
        return str(self)

# ====== Operator Overloading ======
    def __eq__(self, other):
        return isinstance(other, Student) and self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.gpa = min(self.gpa + value, 4)
        elif isinstance(value, Student):
            self.gpa = min(self.gpa + value.gpa, 4)
        return self

    def __bool__(self):
        return self.gpa >= 2

# =============== Callable =================
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


# =============== Friend =========================
def update_student_name(student, new_name):
    ptr = student
    print("\n[ Check - Name]")
    print("ptr is student:", ptr is student)
    ptr._name = new_name

# ================= Dataclass ======================
@dataclass(order=True)
class StudentRecord:
    student_id: int
    name: str
    gpa: float

    def __str__(self):
        return f"ID:{self.student_id} | name:{self.name} | GPA:{self.gpa}"

# ================= Manager ======================
class StudentManager(LoggerMixin):
    def __init__(self):
        self.students = []

    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        return self.students[index]

    def __contains__(self, student_id):
        return any(s.student_id == student_id for s in self.students)

    # add student
    def add_student(self, student):
        self.students.append(student)
        self.log(f"added student{student.student_id}")
        # print("student added successfully")

    # remove student
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.log(f"removed student{student_id}")
                # print("student removed successfully")
                return
        print("student not found")

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.log(f"Found student {student_id}")
                return s
        self.log("Student not found")
        return None

    def display_students(self):
        for s in self.students:
            print(s.display_info())

    def filter_students(self, checker):
        return list(filter(checker, self.students))

    def pipeline_gpa(self):
        to_percent = Pipe(lambda s: s.gpa * 25)
        return [s | to_percent for s in self.students]

    def sorted_records(self):
        records = [
            StudentRecord(s.student_id, s.name, s.gpa)
            for s in self.students
        ]
        return sorted(records, reverse=True)


