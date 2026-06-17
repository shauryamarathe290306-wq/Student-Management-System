import json

# ===================== LOAD DATA =====================
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

# ===================== SAVE FUNCTION =====================
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

# ===================== FEATURES =====================

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    save_data()
    print("✅ Student added successfully!")


def view_students():
    if not students:
        print("⚠️ No students found!")
        return

    print("\n📋 STUDENT LIST")
    print("-" * 40)

    for s in students:
        print(f"Name : {s['name']}")
        print(f"Roll : {s['roll']}")
        print(f"Marks: {s['marks']}")
        print("-" * 40)


def search_student():
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("\n🔍 STUDENT FOUND")
            print(f"Name : {s['name']}")
            print(f"Roll : {s['roll']}")
            print(f"Marks: {s['marks']}")
            return

    print("❌ Student not found!")


def update_student():
    roll = input("Enter roll number to update: ")

    for s in students:
        if s["roll"] == roll:
            print("Enter new details:")

            s["name"] = input("New name: ")
            s["roll"] = input("New roll number: ")
            s["marks"] = input("New marks: ")

            save_data()
            print("✅ Student updated successfully!")
            return

    print("❌ Student not found!")


def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data()
            print("🗑️ Student deleted successfully!")
            return

    print("❌ Student not found!")


def analytics():
    if not students:
        print("⚠️ No data available!")
        return

    total = len(students)
    total_marks = sum(int(s["marks"]) for s in students)
    topper = max(students, key=lambda x: int(x["marks"]))

    print("\n📊 ANALYTICS REPORT")
    print("-" * 40)
    print("Total Students :", total)
    print("Average Marks  :", total_marks / total)
    print("Topper         :", topper["name"], "-", topper["marks"])
    print("-" * 40)


# ===================== MENU =====================

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Analytics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        analytics()

    elif choice == "7":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice!")