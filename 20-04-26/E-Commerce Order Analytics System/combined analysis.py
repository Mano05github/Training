# Revenue per order
import csv
import json

orders = []
with open("orders.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["product_id"] = int(row["product_id"])
        row["quantity"] = int(row["quantity"])
        orders.append(row)


# Read JSON
with open("products.json") as f:
    data = json.load(f)

products = {
    p["product_id"]: {"name": p["name"], "price": p["price"]}
    for p in data["products"]
}


for o in orders:
    price = products[o["product_id"]]["price"]
    print(price * o["quantity"])

# Total revenue
total_revenue = sum(products[o["product_id"]]["price"] * o["quantity"] for o in orders)
print(total_revenue)

# Revenue per product
product_revenue = {}
for o in orders:
    name = products[o["product_id"]]["name"]
    price = products[o["product_id"]]["price"]
    product_revenue[name] = product_revenue.get(name, 0) + price * o["quantity"]
print(product_revenue)

# Highest selling product
print(max(product_revenue, key=product_revenue.get))

# Customer spending
spending = {}
for o in orders:
    c = o["customer"]
    price = products[o["product_id"]]["price"]
    spending[c] = spending.get(c, 0) + price * o["quantity"]
print(spending)

# Top customer
print(max(spending, key=spending.get))

# Customers > 50K
print([c for c, s in spending.items() if s > 50000])

# Final Challenges
print("Visited but not ordered:", set(visits) - set(customer_orders.keys()))
print("Ordered but visited <=1:", [c for c in customer_orders if visit_count[c] <= 1])