students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudents List:")
        for s in students:
            print("-", s)

    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in students:
            print("Student found!")
        else:
            print("Student not found!")

    elif choice == "4":
        break
