
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def show_details(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print("-" * 25)


student1 = Student("Ram Shrestha", 85)
student2 = Student("Shyam Raut", 92)
student3 = Student("Hari Bhattarai", 78)

print("Student Details:")
print("=" * 25)

student1.show_details()
student2.show_details()
student3.show_details()

print("Alternative display using a list:")
print("=" * 35)

students = [student1, student2, student3]
for i, student in enumerate(students, 1):
    print(f"Student {i}:")
    student.show_details()