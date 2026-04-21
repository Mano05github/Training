import json

with open('orders.json','r') as file:
    data = json.load(file)

orders = data['orders']


for o in orders:
    print(o)


total_revenue = sum(o["amount"] for o in orders)
print(f"Total Revenue: {total_revenue}")

spending = {}
order_count = {}
for o in orders:
    spending[o["customer"]] = spending.get(o["customer"], 0) + o["amount"]
    order_count[o["customer"]] = order_count.get(o["customer"], 0) + 1

print("Total Spending per Customer:", spending)
print("Total Orders per Customer:", order_count)


top_customer = max(spending, key=spending.get)
print(f"Highest Spender: {top_customer} ({spending[top_customer]})")