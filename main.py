from testmodule import Student, StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n========== student management ==========")
        print("1 - add student")
        print("2 - show all student")
        print("3 - update student information")
        print("4 - delete student")
        print("5 - search for student")
        print("6 - print student number")
        print("7 - exit")
        print("===========================================")

        choice = input("choice: ")

        if choice == "1":
            try:
                student_id = int(input("enter student ID: "))
                name = input("enter student Name: ")
                age = int(input("enter student Age: "))
                department = input("enter Department: ")
                gpa = float(input("enter GPA (0-4): "))

                student_obj = Student(student_id, name, age, department, gpa)
                manager.add_student(student_obj)

            except ValueError as e:
                print("error:", e)

        elif choice == "2":
            manager.show_all()

        elif choice == "3":
            try:
                student_id = int(input("enter student ID to update: "))
                print("Leave the field blank if you do not want to change it.")
                name = input("new name: ")
                age_input = input("new age: ")
                department = input("new department: ")
                gpa_input = input("new GPA: ")

                age = int(age_input) if age_input else None
                gpa = float(gpa_input) if gpa_input else None

                manager.update_student(student_id, name or None, age, department or None, gpa)

            except ValueError as e:
                print("error:", e)

        elif choice == "4":
            try:
                student_id = int(input("enter student ID to delete: "))
                manager.delete_student(student_id)
            except ValueError:
                print("enter correct number")

        elif choice == "5":
            try:
                student_id = int(input("enter student ID to search: "))
                s = manager.find_student(student_id)
                if s:
                    print(s.display_info())
                else:
                    print("The student could not be found.")
            except ValueError:
                print("enter correct number")

        elif choice == "6":
            print(f"all number of student: {len(manager)}")

        elif choice == "7":
            print("The program has been exited.")
            break

        else:
            print("Incorrect choice, please try again.")

if __name__ == "__main__":
    main()