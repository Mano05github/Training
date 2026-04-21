orders = [
{"order_id":1,"customer":"Rahul","amount":2500},
{"order_id":2,"customer":"Sneha","amount":1800},
{"order_id":3,"customer":"Rahul","amount":3200},
{"order_id":4,"customer":"Amit","amount":1500}
]

# Dictionaries to store our results
spending = {}
order_counts = {}

for order in orders:
    name = order["customer"]
    amt = order["amount"]

    # Update spending and counts
    spending[name] = spending.get(name, 0) + amt
    order_counts[name] = order_counts.get(name, 0) + 1

#Find highest spending customer
top_customer = max(spending, key=spending.get)

print("1. Total Spending:", spending)
print(f"2. Highest Spender: {top_customer} ({spending[top_customer]})")
print("3. Order Counts:", order_counts)