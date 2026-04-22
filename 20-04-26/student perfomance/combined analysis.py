# Marks stats


import json
from collections import Counter
# Read JSON
data = json.load(open("marks.json"))

# Print names and marks
for s in data["students"]:
    print(s["name"], s["marks"])

marks = [s["marks"] for s in data["students"]]
print(max(marks), min(marks), sum(marks))

import csv

attendance = list(csv.DictReader(open("attendance.csv")))
attendance_dict = {}
for a in attendance:
    perc = (int(a["days_present"]) / int(a["total_days"])) * 100
    attendance_dict[a["name"]] = perc
    print(a["name"], perc)
# Courses
print(tuple([s["course"] for s in data["students"]]))
print(set([s["course"] for s in data["students"]]))

# Dictionaries
marks_dict = {s["name"]: s["marks"] for s in data["students"]}

# Pass/Fail
for s in data["students"]:
    print(s["name"], "Pass" if s["marks"] >= 50 else "Fail")

# Grade function
def grade(m):
    if m >= 90: return "A"
    elif m >= 75: return "B"
    elif m >= 50: return "C"
    else: return "Fail"

# High performers
print([s["name"] for s in data["students"] if s["marks"] > 80 and attendance_dict[s["name"]] > 85])

# Final combined structure
final = {}
for s in data["students"]:
    name = s["name"]
    final[name] = {
        "marks": s["marks"],
        "attendance": attendance_dict[name],
        "course": s["course"],
        "grade": grade(s["marks"])
    }

# Eligible & improvement
print([n for n, d in final.items() if d["marks"] >= 75 and d["attendance"] >= 80])
print([n for n, d in final.items() if d["marks"] < 75 or d["attendance"] < 80])

# Write report
with open("report.txt", "w") as f:
    for n, d in final.items():
        f.write(f"{n} - Marks:{d['marks']} - Attendance:{d['attendance']} - Grade:{d['grade']}\n")

# Eligible students file
with open("eligible_students.txt", "w") as f:
    for n in final:
        if final[n]["marks"] >= 75 and final[n]["attendance"] >= 80:
            f.write(n + "\n")

# Final output
print("Topper:", max(final, key=lambda x: final[x]["marks"]))
print("Best Attendance:", max(final, key=lambda x: final[x]["attendance"]))
print("Average:", sum(marks) / len(marks))