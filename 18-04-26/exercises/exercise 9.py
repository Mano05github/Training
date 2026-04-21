sales = [
{"product":"Laptop","qty":5},
{"product":"Mouse","qty":20},
{"product":"Laptop","qty":3},
{"product":"Keyboard","qty":10}
]

totals = {}

for item in sales:
    totals[item['product']] = totals.get(item['product'],0)+1

print(totals)

best_seller = max(totals, key=totals.get)

print(f"The highest selling product is: {best_seller} ({totals[best_seller]} units)")
