# Read students
students = [line.strip() for line in open("students.txt")]
print(students)

# Total entries
print(len(students))

# Unique students
unique_students = set(students)
print(unique_students)

# Count occurrences
from collections import Counter
student_count = Counter(students)
print(dict(student_count))

# Write unique students
with open("unique_students.txt", "w") as f:
    for s in unique_students:
        f.write(s + "\n")