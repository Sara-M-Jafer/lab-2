from  abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 18 <= value <= 25:
            self._age = value
        else:
            raise ValueError("age must be between 18 and 25")

    @abstractmethod
    def display_info(self):
        pass


class Student(Person):
    def __init__(self,id, name, age, department, gpa):
        super().__init__(name, age)
        self.student_id = id
        self.__department = department
        self.gpa = gpa

    @property
    def id(self):
        return self.id

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self,new_dpt):
        self.__department = new_dpt

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self,value):
        if 0 <= value <= 4 :
            self.__gpa = value
        else:
            raise ValueError("gpa must be between 0 and 4")


    def __str__(self):
        return f"Student_ID: {self.student_id} | Name:{self._name} | Age:{self.age} | Department: {self.department} | GPA:{self.gpa}"

    def display_info(self):
        return f"Student_ID: {self.student_id} | Name:{self._name} | Age:{self.age} | Department: {self.department} | GPA:{self.gpa}"

class StudentManager:

    def __init__(self):
        self.students = []

#show number of student
    def __len__(self):
        return len(self.students)

#add new student
    def add_student(self, student):
        self.students.append(student)
        print("student added successfully")

#to delete student
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("student removed successfully")
                return
        print("student not found")

#to update student information
    def update_student(self, student_id, **new):
        for student in self.students:
            if student.student_id == student_id:

                if "name" in new:
                    student._name = new["name"]

                if "age" in new:
                    student.age = new["age"]

                if "department" in new:
                    student.department = new["department"]

                if "gpa" in new:
                    student.gpa = new["gpa"]

                print("student updated successfully")
                return

        print("student not found")

# to display all student
    def display_students(self):
        if not self.students:
            print("no students available")
            return

        for student in self.students:
            print(student)

#سارة الكود مابي اخطاء, بس اخر كلاس ما يشتغل الا نسوي استدعاءات

# s =Student(1,"sara",22,"cybersecurity",3)
# print(s)