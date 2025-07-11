# Q no. 12:
# Create a dictionary to store student names as keys and their scores in three subjects as values (in a list).
# Write functions to:
# a. Display the average marks of each student
# b. Find the topper
# c. Update the marks of a student

def display_averages(student_scores):
    averages = {}
    for student, scores in student_scores.items():
        averages[student] = sum(scores) / len(scores)
    return averages

def find_topper(student_scores):
    averages = display_averages(student_scores)
    topper = max(averages, key=averages.get)
    return topper, averages[topper]

def update_marks(student_scores, student_name, new_scores):
    if student_name in student_scores:
        student_scores[student_name] = new_scores
        return True
    else:
        return False

students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [70, 75, 80]
}

averages = display_averages(students)
print("Average marks of each student:", averages)

topper, top_score = find_topper(students)
print(f"Topper: {topper} with average score {top_score:.2f}")

updated = update_marks(students, "Charlie", [80, 85, 90])
if updated:
    print("Updated marks for Charlie:", students["Charlie"])
else:
    print("Student not found.")