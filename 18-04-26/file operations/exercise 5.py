import csv

rows = []
with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:

        row['salary'] = int(row['salary'])
        rows.append(row)

print("Employees:", [r["name"] for r in rows])


it_employees = [r["name"] for r in rows if r["department"] == "IT"]
print("IT Department:", it_employees)

avg_salary = sum(r["salary"] for r in rows) / len(rows)
print(f"Average Salary: {avg_salary}")

highest_paid = max(rows, key=lambda x: x["salary"])
print(f"Highest Salary: {highest_paid['name']} ({highest_paid['salary']})")

dept_counts = {}
for r in rows:
    dept_counts[r["department"]] = dept_counts.get(r["department"], 0) + 1
print("Department Counts:", dept_counts)