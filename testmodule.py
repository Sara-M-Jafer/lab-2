from  abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        if 6 <= new_age <= 24 :
            self.__age = new_age
        else:
            print("age must be between 6 and 24")

    @abstractmethod
    def display_info(self):
        pass


class Student(Person):
    def __init__(self, student_id, name, age, department, gpa):
        super().__init__(name, age)
        self.student_id = student_id
        self.__department = department
        self.gpa = gpa

    @property
    def id(self):
        return self.student_id

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
            print("gpa must be between 0 and 4")

    def __str__(self):
        return f"Student_ID: {self.student_id} | Name:{self._name} | Age:{self.age} | Department: {self.department} | GPA:{self.gpa}"

    def display_info(self):
        return f"Student_ID: {self.student_id} | Name:{self._name} | Age:{self.age} | Department: {self.department} | GPA:{self.gpa}"

s =Student(1,"sara",30,"cybersecurity",3)
print(s)