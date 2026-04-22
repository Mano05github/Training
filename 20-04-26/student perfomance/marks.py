import json
from collections import Counter
# Read JSON
data = json.load(open("marks.json"))

# Print names and marks
for s in data["students"]:
    print(s["name"], s["marks"])

# Highest & lowest marks
print(max(data["students"], key=lambda x: x["marks"]))
print(min(data["students"], key=lambda x: x["marks"]))

# Average marks
marks = [s["marks"] for s in data["students"]]
print(sum(marks) / len(marks))

# Python course students
print([s["name"] for s in data["students"] if s["course"] == "Python"])

# Course count
print(dict(Counter([s["course"] for s in data["students"]])))