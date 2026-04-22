import csv

orders = []
with open("orders.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["product_id"] = int(row["product_id"])
        row["quantity"] = int(row["quantity"])
        orders.append(row)

# Print orders
for o in orders:
    print(o)

# Quantity per product
product_qty = {}
for o in orders:
    pid = o["product_id"]
    product_qty[pid] = product_qty.get(pid, 0) + o["quantity"]
print(product_qty)

# Orders per customer
customer_orders = {}
for o in orders:
    c = o["customer"]
    customer_orders[c] = customer_orders.get(c, 0) + 1
print(customer_orders)