from testmodule import Student, StudentManager

manager = StudentManager()

s1 = Student(1, "Sara", 20, "Cyber Security", 3.5)
s2 = Student(2, "Ali", 22, "Computer Science", 2.8)
s3 = Student(3, "noor", 19, "cyber security", 3.3)

#add student
manager.add_student(s1)
manager.add_student(s2)
manager.add_student(s3)

#show student
print("\n--- All Students ---")
manager.display_students()

# update student data
print("\n--- Update Student ---")
manager.update_student(1, name="Sarah", gpa=3.9)

#after update
manager.display_students()

#number of student
print("\nNumber of students:", len(manager))


# delete student
print("\n--- Remove Student ---")
manager.remove_student(2)

# after delete
manager.display_students()