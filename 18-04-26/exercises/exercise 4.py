# invertory management

invertory = {
    'laptop':10,
    'mouse':25,
    'keyboard':15
}

invertory['monitor'] = 8
print(invertory)

invertory['laptop']-=2
print(invertory)

items = [k for k,v in invertory.items() if v < 10]
print(items)