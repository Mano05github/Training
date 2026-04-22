import json

# Read JSON
with open("products.json") as f:
    data = json.load(f)

# Print product details
for p in data["products"]:
    print(p["name"], p["price"])

# Store in dictionary
products = {
    p["product_id"]: {"name": p["name"], "price": p["price"]}
    for p in data["products"]
}

# Most expensive product
print(max(products.values(), key=lambda x: x["price"]))

# Least expensive product
print(min(products.values(), key=lambda x: x["price"]))