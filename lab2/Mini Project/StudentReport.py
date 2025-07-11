# MINI PROJECT: Student Report Card Management System
def add_student(records, name, roll_no, marks):
    if roll_no in records:
        return False 
    records[roll_no] = {"name": name, "marks": marks}
    return True

def view_all_students(records):
    for roll_no, info in records.items():
        print(f"Roll No: {roll_no}, Name: {info['name']}, Marks: {info['marks']}")

def calculate_average(marks):
    return sum(marks) / len(marks)

def find_toppers(records):
    if not records:
        return []
    averages = {roll: calculate_average(info["marks"]) for roll, info in records.items()}
    max_avg = max(averages.values())
    toppers = [records[roll]["name"] for roll, avg in averages.items() if avg == max_avg]
    return toppers, max_avg

def search_student(records, roll_no):
    return records.get(roll_no, None)

def students_failed(records, passing_mark=40):
    failed_students = []
    for roll_no, info in records.items():
        if any(mark < passing_mark for mark in info["marks"]):
            failed_students.append((roll_no, info["name"]))
    return failed_students

def update_marks(records, roll_no, new_marks):
    if roll_no in records:
        records[roll_no]["marks"] = new_marks
        return True
    return False

students = {}

add_student(students, "Alice", 1, [85, 78, 92])
add_student(students, "Bob", 2, [65, 55, 70])
add_student(students, "Charlie", 3, [30, 85, 40])
add_student(students, "Diana", 4, [90, 93, 89])

print("\n--- All Student Records ---")
view_all_students(students)

toppers, avg = find_toppers(students)
print(f"\nTopper(s) with average marks {avg:.2f}: {', '.join(toppers)}")

roll_to_search = 2
result = search_student(students, roll_to_search)
if result:
    print(f"\nDetails of student with roll no {roll_to_search}: Name: {result['name']}, Marks: {result['marks']}")
else:
    print(f"\nStudent with roll no {roll_to_search} not found.")

failed = students_failed(students)
print("\nStudents who failed in one or more subjects:")
for roll, name in failed:
    print(f"Roll No: {roll}, Name: {name}")

updated = update_marks(students, 3, [45, 85, 50])
if updated:
    print("\nUpdated marks for roll no 3:")
    print(students[3])
else:
    print("\nFailed to update marks: Roll number not found.")