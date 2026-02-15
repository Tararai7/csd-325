import json

def print_students(students):
    """Prints each student's details in the required format."""
    for student in students:
        print(f"{student['last_name']}, {student['first_name']} : ID = {student['id']}, Email = {student['email']}")

# Load student.json into a Python list
with open('student.json', 'r') as file:
    student_list = json.load(file)

# Notify user this is the original list
print("This is the original Student list.\n")

# Print original student list
print_students(student_list)

# Add YOUR details here (REPLACE THESE VALUES)
new_student = {
    "last_name": "YOUR_LAST_NAME",   #  REPLACE WITH YOUR LAST NAME
    "first_name": "YOUR_FIRST_NAME", #  REPLACE WITH YOUR FIRST NAME
    "id": "YOUR_FICTIONAL_ID",       #  REPLACE WITH A 5-DIGIT ID (e.g., "12345")
    "email": "YOUR_EMAIL@EXAMPLE.COM" #  REPLACE WITH YOUR EMAIL
}
student_list.append(new_student)

# Notify user this is the updated list
print("\nThis is the updated Student list.\n")

# Print updated student list
print_students(student_list)

# Update student.json with new data
with open('student.json', 'w') as file:
    json.dump(student_list, file, indent=4)

# Notify user the file was updated
print("\nThe student.json file has been updated.")