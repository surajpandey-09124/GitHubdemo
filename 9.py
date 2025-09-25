# Dictionary of students and marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

# Take student name as input
name = input("Enter student's name: ")

# Retrieve and display marks
if name in students:
    print(f"{name}'s marks are {students[name]}")
else:
    print(f"Student '{name}' not found.")
