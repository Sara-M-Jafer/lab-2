from testmodule import Student, StudentManager, update_student_name, update_student_gpa, update_student_department

manager = StudentManager()

s1 = Student(1, "Sara", 20, "Cyber Sec", 3.5)
s2 = Student(2, "Ali", 22, "Computer Science", 2.8)
s3 = Student(3, "noor", 20, "Cyber Security", 3.3)
s4 = Student(4, "ahmed", 23, "Computer Science", 1.5)
s5 = Student(5, "mena", 24, "Cyber Security", 0.5)
s6 = Student(6, "fatima", 25, "Computer Science", 4.0)

#add student
manager.add_student(s1)
manager.add_student(s2)
manager.add_student(s3)
manager.add_student(s4)
manager.add_student(s5)
manager.add_student(s6)

#show student
print("\n--- All Students ---")
manager.display_students()

print("\n High GPA Student")
high = list(filter(lambda s:s.gpa >= 2 ,manager.students))
list(map(lambda s: print(s.display_info()),high))

#update student

for student in manager.students:
    if student.student_id == 1:
        update_student_name(student, "Sarah")
        update_student_gpa(student, 3.8)
        update_student_department(student, "Cyber Security")

#after update
print("\n--- Update Student ---")
manager.display_students()

# operator overloading tests
print("\n--- Comparison ---")
print(s1 > s2)

print("\n--- Sorting ---")
manager.students.sort()
manager.display_students()


print("\n--- In-place ---")
s1 += 0.2
print(s1)

print("\n--- Bool ---")
if s1:
    print("Student Passed")

print("\n--- Contains ---")
print(1 in manager)

print("\n--- Indexing ---")
print(manager[0])

#number of student
print("\nNumber of students:", len(manager))

# delete student
print("\n--- Remove Student ---")
manager.remove_student(2)
manager.remove_student(6)

# after delete
print("\n--- All Students ---")
manager.display_students()

#search
print("\n--- Search Student ---")
found = manager.find_student(3)

if found:
    print(found)
else:
    print("Student not found")