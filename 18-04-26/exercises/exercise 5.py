# email domain extractor

emails = [
    'user1@gmail.com',
    'user2@yahoo.com',
    'user3@gmail.com',
    'user4@outlook.com'
]

for i in emails:
    print(i[6:])

domains = ['gmail.com','yahoo.com','outlook.com']

#count of users per domain
g_domain = 0
y_domain = 0
o_domain = 0

for i in emails:
    if i[6:] == domains[0]:
        g_domain += 1
    elif i[6:] == domains[1]:
        y_domain += 1
    elif i[6:] == domains[2]:
        o_domain += 1
    else:
        print(None)

print(g_domain)
print(y_domain)
print(o_domain)


