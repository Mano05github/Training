import json


with open('student.json','r') as file:
    data = json.load(file)

    print(data)
    students = data['students']
    print([i['name'] for i in students])
    python_students = [s["name"] for s in students if s["course"] == "Python"]
    print("Python Students:", python_students)
    top_student = max(students, key=lambda x: x["marks"])
    print(f"Highest Marks: {top_student['name']} ({top_student['marks']})")
    avg_marks = sum(s["marks"] for s in students) / len(students)
    print(f"Average Marks: {avg_marks}")
    course_counts = {}
    for s in students:
        course_counts[s["course"]] = course_counts.get(s["course"], 0) + 1
    print("Course Counts:", course_counts)