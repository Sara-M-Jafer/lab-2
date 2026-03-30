from testmodule import Student, StudentManager, update_student_name, update_student_gpa, update_student_department, show_student_info

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

#
print("\n--- Update Student ---")
for student in manager.students:
    if student.student_id == 1:
        update_student_name(student, "Sarah")      # Friend function لتحديث الاسم
        update_student_gpa(student, 3.9)          # Friend fu4nction لتحديث GPA
        update_student_department(student, "Cyber Sec")  # Friend function لتحديث القسم

#after update
manager.display_students()

#number of student
print("\nNumber of students:", len(manager))


# delete student
print("\n--- Remove Student ---")
manager.remove_student(2)

# after delete
manager.display_students()
