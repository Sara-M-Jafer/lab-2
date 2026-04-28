from testmodule import *

# ================= Create Manager =================
manager = StudentManager()

# ================= Create Students =================
s1 = Student(1, "Sara", 20, "Cyber Sec", 3.5)
s2 = Student(2, "Ali", 22, "Computer Science", 2.8)
s3 = Student(3, "Noor", 20, "Cyber Security", 3.3)
s4 = Student(4, "Ahmed", 23, "Computer Science", 1.5)
s5 = Student(5, "Mena", 24, "Cyber Security", 0.5)
s6 = Student(6, "Fatima", 25, "Computer Science", 4.0)

# ================= Add Students =================
manager.add_student(s1)
manager.add_student(s2)
manager.add_student(s3)
manager.add_student(s4)
manager.add_student(s5)
manager.add_student(s6)

# ================= Display =================
print("\n--- All Students ---")
manager.display_students()

# ================= Callable (Filter GPA) =================
print("\n--- Valid GPA Students (>=2) ---")
checker = GPAChecker(2, 4)
valid_students = manager.filter_students(checker)
for s in valid_students:
    print(s)

# ================= Friend (Update Name) =================
update_student_name(s1, "Sarah")

# ================= Update using methods (بدل friend) =================
s1.gpa = 3.8
s1.department = "Cyber Security"

print("\n--- After Update ---")
manager.display_students()

# ================= Operator Overloading =================
print("\n--- Comparison (GPA) ---")
print("s1 == s2:", s1 == s2)
print("s1 > s2:", s1 > s2)

print("\n--- Sorting Students by GPA ---")
manager.students.sort()
manager.display_students()

print("\n--- In-place GPA Increase ---")
s1 += 0.2
print(s1)

print("\n--- Bool (Pass/Fail) ---")
if s1:
    print("Student Passed")
else:
    print("Student Failed")

# ================= Pipe =================
filter_passed = Pipe(lambda students: [s for s in students if s.gpa >= 2])
get_names = Pipe(lambda students: [s.name for s in students])

result = manager.students | filter_passed | get_names

print("\n--- Pipeline Result (Passed Students Names) ---")
print(result)

# ================= Dataclass =================
records = [StudentRecord(s.student_id, s.name, s.gpa) for s in manager.students]

print("\n--- Records ---")
for r in records:
    print(r)

print("\n--- Sorted Records (Dataclass) ---")
for r in sorted(records):
    print(r)

# ================= Manager Features =================
print("\n--- Contains ---")
print("Is ID 1 in manager?", 1 in manager)

print("\n--- Indexing ---")
print(manager[2])

print("\n--- Length ---")
print(len(manager))

# ================= Remove =================
print("\n--- Remove Students ---")
manager.remove_student(2)
manager.remove_student(6)

print("\n--- After Remove ---")
manager.display_students()

# ================= Search =================
print("\n--- Search Student ---")
found = manager.find_student(3)

if found:
    print("Found:", found)
else:
    print("Student not found")

# ================= Sorted Records from Manager =================
print("\n--- Sorted Records (Manager Method) ---")
for r in manager.sorted_records():
    print(r)
