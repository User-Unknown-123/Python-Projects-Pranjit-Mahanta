import csv


# q1 create csv file and write data
def create_file():
    f = open("attendance.csv", "w", newline="")
    writer = csv.writer(f)

    writer.writerow(["EmpID", "Name", "Status"])

    n = int(input("How many employees: "))
    for i in range(n):
        eid = input("Enter employee id: ")
        name = input("Enter name: ")
        status = input("Enter status (Present/Absent): ")
        writer.writerow([eid, name, status])

    f.close()
    print("CSV file created")


# q2 read and display csv file
def read_file():
    f = open("attendance.csv", "r")
    reader = csv.reader(f)

    print("Attendance Records:")
    for row in reader:
        print(row)

    f.close()


# q3 append new record
def append_file():
    f = open("attendance.csv", "a", newline="")
    writer = csv.writer(f)

    eid = input("Enter employee id: ")
    name = input("Enter name: ")
    status = input("Enter status (Present/Absent): ")
    writer.writerow([eid, name, status])

    f.close()
    print("Record added")


# q4 count absent employees
def count_absent():
    f = open("attendance.csv", "r")
    reader = csv.reader(f)

    count = 0
    next(reader)  # skip heading

    for row in reader:
        if row[2].lower() == "absent":
            count += 1

    f.close()
    print("Absent employees:", count)


# q5 search employee by id
def search_employee():
    eid = input("Enter employee id to search: ")
    f = open("attendance.csv", "r")
    reader = csv.reader(f)

    found = False
    for row in reader:
        if row and row[0] == eid:
            print("Employee found:", row)
            found = True

    if not found:
        print("Employee not found")

    f.close()


# menu program
while True:
    print("\nMenu")
    print("1. Create attendance file")
    print("2. Read attendance file")
    print("3. Add new attendance")
    print("4. Count absent employees")
    print("5. Search employee by ID")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        create_file()
    elif ch == 2:
        read_file()
    elif ch == 3:
        append_file()
    elif ch == 4:
        count_absent()
    elif ch == 5:
        search_employee()
    elif ch == 6:
        print("Exit")
        break
    else:
        print("Invalid choice")