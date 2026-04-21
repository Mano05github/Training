students = {
    'Rahul':85,
    'Sneha':92,
    'Arjun' : 78,
    'Priya' : 88
}



#  topper
max_marks = max(students.values())

student = [k for k,v in students.items() if v == max_marks]
print('Topper :',student)

# average mark

l = len(students.values())
avg = sum(students.values())/l
print(avg)

#  students above 85

s = [k for k,v in students.items() if v > 85]
print(s)