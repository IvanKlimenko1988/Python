book={}

book['Миша'] = 98465566
book['Саша']=[64654464,46546464]

print(book)

if 98465566 in book.values():
    print("Yes")
else: print("No")

for x,y in book.items():
    print(x, y)

for x in book.values():
    print(x)

for x in book.keys():
    print(x)