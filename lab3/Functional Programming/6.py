def student_profile(**kwargs):
    print("Student Profile:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_profile(name="Abhishek", age=20, grade="A+")