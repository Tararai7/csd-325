import json
import os

def print_students(students):
    """Prints each student's details in the required format."""
    for student in students:
        print(f"{student['last_name']}, {student['first_name']} : ID = {student['id']}, Email = {student['email']}")

# ====== FIX 1: FILE PATH HANDLING ======
# Check if student.json exists in current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, 'student.json')

if not os.path.exists(json_path):
    # Create default student.json if missing
    default_data = [
        {
            "last_name": "Ripley",
            "first_name": "Ellen",
            "id": "45604",
            "email": "eripley@gmail.com"
        }
    ]
    with open(json_path, 'w') as f:
        json.dump(default_data, f, indent=4)
    print(f"Created default student.json at {json_path}")

# Load student.json into a Python list
with open(json_path, 'r') as file:
    student_list = json.load(file)

# Notify user this is the original list
print("This is the original Student list.\n")

# Print original student list
print_students(student_list)

# ====== FIX 2: SYNTAX CORRECTION ======
# Corrected dictionary definition (properly closed braces)
new_student = {
    "last_name": "Rai",
    "first_name": "Tara",
    "id": "98765",
    "email": "tara.rai@example.com"
}
student_list.append(new_student)

# Notify user this is the updated list
print("\nThis is the updated Student list.\n")

# Print updated student list
print_students(student_list)

# Update student.json with new data
with open(json_path, 'w') as file:
    json.dump(student_list, file, indent=4)

# Notify user the file was updated
print("\nThe student.json file has been updated.")