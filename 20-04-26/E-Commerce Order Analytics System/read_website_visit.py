with open('website_visits.txt','r') as file:
    for line in file:

        print(line.strip())

each_visit = {}


with open('website_visits.txt','r') as file:
    for line in file:
        each_visit[line.strip()] = each_visit.get(line.strip(),0)+1
print(each_visit)

print('total visits:',sum(each_visit.values()))
unique = set()
with open('website_visits.txt','r') as file:
    for line in file:
        unique.add(line.strip())


print(unique)

max_visits = max(each_visit.values())
most_freq_visitor = [k for k,v in each_visit.items() if v==max_visits]
print('most_freq_visitor:',most_freq_visitor)