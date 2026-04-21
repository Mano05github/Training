from Tools.scripts.texi2html import increment

products = {
"Laptop":75000,
"Mobile":30000,
"Tablet":25000
}


inc_for_laptop = (10/100)*products["Laptop"]
inc_for_mobile = (10/100)*products["Mobile"]
inc_for_tablet = (10/100)*products["Tablet"]

products["Laptop"] += inc_for_laptop
products["Mobile"] += inc_for_mobile
products["Tablet"] += inc_for_tablet

print(products)


products = {k: int(v*1.10) for k,v in products.items()}

for item,prices in products.items():
    print(f'{item}:{prices}')