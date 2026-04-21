import csv

sales_data = []
with open('sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert quantity and price to integers for calculations
        row['quantity'] = int(row['quantity'])
        row['price'] = int(row['price'])
        sales_data.append(row)

total_rev = sum(s["quantity"] * s["price"] for s in sales_data)
print(f"Total Sales Revenue: {total_rev}")

# 2. Find total quantity sold per product
# 4. Calculate total revenue per product
prod_qty = {}
prod_rev = {}
for s in sales_data:
    p = s["product"]
    rev = s["quantity"] * s["price"]
    prod_qty[p] = prod_qty.get(p, 0) + s["quantity"]
    prod_rev[p] = prod_rev.get(p, 0) + rev

print("Quantity per Product:", prod_qty)
print("Revenue per Product:", prod_rev)

# 3. Find the product with highest sales (revenue)
top_product = max(prod_rev, key=prod_rev.get)
print(f"Highest Sales Product: {top_product}")

# 5. Print products with sales above 50,000
high_sales = [p for p, r in prod_rev.items() if r > 50000]
print("Products with sales > 50,000:", high_sales)
