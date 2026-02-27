from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self._name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if 6 <= value <= 24:
            self._age = value
        else:
            raise ValueError("age must be between 6 and 24")

    @abstractmethod
    def display_info(self):
        pass

class Student(Person):
    def __init__(self,id,name,age,department,gpa):
        super().__init__(name,age)
        self.__id = id
        self.__department = department
        self.gpa = gpa

    @property
    def id(self):
        return self.__id

    @property
    def department(self):
        return self.__department

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self,value):
        if 0 <= value <= 4:
            self.__gpa = value
        else:
            raise ValueError("gpa must be between 0 and 4")

    def __str__(self):
        return f"ID:{self.__id} | name:{self._name} | age:{self.age} | department:{self.__department} | gpa:{self.gpa}"


    def display_info(self):
        return f"ID:{self.__id} | name:{self._name} | age:{self.age} | department:{self.__department} | gpa:{self.gpa}"


class StudentManager:
    def __init__(self):
        self.students = []

    def __len__(self):
        return len(self.students)

    def add_student(self, student):
        if any(map(lambda s: s.id == student.id, self.students)):
            print(" This student already exists with the same ID!")
            return
        self.students.append(student)
        print(" The student has been successfully added!")

    def show_all(self):
        if not self.students:
            print("There are no registered students")
        else:
            for s in self.students:
                print(s.display_info())

    def find_student(self, student_id):
        return next(filter(lambda s: s.id == student_id, self.students), None)

    def update_student(self, student_id, name=None, age=None, department=None, gpa=None):
        s = self.find_student(student_id)
        if not s:
            print(" The student could not be found")
            return
        if name:
            s._name = name
        if age is not None:
            s.age = age
        if department:
            s._Student__department = department
        if gpa is not None:
            s.gpa = gpa
        print("Student data has been updated")

    def delete_student(self, student_id):
        s = self.find_student(student_id)
        if not s:
            print("The student could not be found")
            return
        self.students.remove(s)
        print("The student has been deleted")

