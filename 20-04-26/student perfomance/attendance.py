import csv

attendance = list(csv.DictReader(open("attendance.csv")))

# Print attendance
for a in attendance:
    print(a)

# Calculate percentage
attendance_dict = {}
for a in attendance:
    perc = (int(a["days_present"]) / int(a["total_days"])) * 100
    attendance_dict[a["name"]] = perc
    print(a["name"], perc)

# Below 80%
print([n for n, p in attendance_dict.items() if p < 80])

# Best attendance
print(max(attendance_dict, key=attendance_dict.get))