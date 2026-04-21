with open('numbers.txt','r') as file:
    data = file.read()
    print(data)


tot = 0
with open('numbers.txt','r') as file:
    for line in file:
        # max_num = max(int(line.strip()))
        # min_num = min(int(line.strip()))
        tot+= int(line.strip())
        # l = []
        # l.append(int(line.strip()))
print(tot)
# print(l)

# print(max_num)
#
# print(min_num)


with open('numbers.txt','r') as file:
    l = []
    for line in file:
        l.append(int(line.strip()))
max_num = max(l)
min_num = min(l)

print(max_num)
print(min_num)

count = 0
for i in l:
    if i > 50:
        count += 1

print(count)
