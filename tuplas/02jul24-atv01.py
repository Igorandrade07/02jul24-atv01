tuplacatupla = tuple(("a", "b", "c"))

print(tuplacatupla)

print("-------------------------------------------")

tuplacatupla = tuple(("a", "b", "c"))

print(tuplacatupla[1])

print("-------------------------------------------")
tuplacatupla = ("a", "b", "c", "d", "e", "f", "g", "h")
print(tuplacatupla[1:5])

print("-------------------------------------------")

tuplacatuplata = ("abba", "black", "carpenters", "daisuke", "elvis", "frank", "gorillaz", "house")
print(tuplacatuplata)

y = list(tuplacatuplata)
print(y)

y.append("Orange")
print(y)

tuplacatuplata = tuple(y)
print(tuplacatuplata)

print("-------------------------------------------")
tuplacatupla = (1, 2, 3, 4, 5, 6, 1, 8, 9, 1)
x = tuplacatupla.count(1)
print(x)


print("-------------------------------------------")
tuplacatupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
x = tuplacatupla.index(8)
print(x)