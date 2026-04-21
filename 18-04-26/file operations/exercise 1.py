with open('login.txt','r') as file:
    for line in file:
        print(line.strip())
    data = file.readlines()
    tot_records = len(data)
    print(tot_records)

count = {}
with open('login.txt','r') as file:
    for line in file:
        count[line.strip()] = count.get(line.strip(),0)+1

print(count)

max_log = max(count.values())

user = [k for k, v in count.items() if v == max_log]
print(user)

print('unique users:',list(count.keys()))
