from testmodule import Student, StudentManager, update_student_name, update_student_gpa, update_student_department,GPAChecker,Pipe,StudentRecord

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

# ================= Callable =================
print("\n--- Valid GPA Students ---")
checker = GPAChecker(2, 4)
valid_students = list(filter(checker, manager.students))
for s in valid_students:
    print(s)

# ================= Update =================
for student in manager.students:
    if student.student_id == 1:
        update_student_name(student, "Sarah")
        update_student_gpa(student, 3.8)
        update_student_department(student, "Cyber Security")

print("\n--- After Update ---")
manager.display_students()

# ================= Operator Overloading =================
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

# ================= Pipe =================
filter_passed = Pipe(lambda students: [s for s in students if s.gpa >= 2])
get_names = Pipe(lambda students: [s._name for s in students])

result = manager.students | filter_passed | get_names

print("\n--- Pipeline Result ---")
print(result)

# ================= Dataclass =================
records = [StudentRecord(s.student_id, s._name, s.gpa) for s in manager.students]

print("\n--- Records ---")
for r in records:
    print(r)

print("\n--- Sorted Records ---")
print(sorted(records))

# ================= Manager Features =================
print("\n--- Contains ---")
print(1 in manager)

print("\n--- Indexing ---")
print(manager[0])

print("\nNumber of students:", len(manager))

print("\n--- Remove Student ---")
manager.remove_student(2)
manager.remove_student(6)

print("\n--- All Students ---")
manager.display_students()

print("\n--- Search Student ---")
found = manager.find_student(3)

if found:
    print(found)
else:
    print("Student not found")

