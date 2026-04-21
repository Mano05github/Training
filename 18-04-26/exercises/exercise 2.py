numbers = [10,20,10,30,20,10,40]
dict1 = {}
for i in numbers:
    dict1[i] = dict1.get(i,0)+1

print(dict1)