student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Access values in the dictionary
student_name = student["name"]

# Add a new key-value pair
student["grade"] = "A"

# Print the dictionary
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")
