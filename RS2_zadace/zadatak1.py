# 1. Kvadriranje broja
x = lambda a : a ** 2
print(x(3))

# 2. Zbroji pa kvadriraj
x = lambda a, b : (a + b) ** 2
print(x(1, 2))

# 3. Kvadriraj duljinu niza
x = lambda a : len(a) ** 2
print(x([1, 2, 3]))

# 4. Pomnoži vrijednost s 5 pa potenciraj na x
x = lambda a, b: (b * 5) ** a
print(x(2, 3))

# 5. Vrati True ako je broj paran, inače vrati None
x = lambda a : True if a % 2 == 0 else None
print(x(2))
print(x(3))