# type(x) nous permet de pouvoir récupérer le type de variable

# String
a = "une chaine de caraRangectère !"
print(type(a), a)

# Int
b = 12
print(type(b), b)

# Float
c = 50.2
print(type(c), c)

# Complex
d = 1j
print(type(d), d)

# List
e = ["Bruno", "Andre", "Chris"]
print(type(e), e)

# Tuple
f = ("Bruno", "Andre", "Chris")
print(type(f), f)

# Range
g = range(4)
print(type(g), g)

# Dict
h = {"name" : "John", "age" : 36}
print(type(h), h)

# Set
i = {"apple", "banana", "cherry"}
print(type(i), i)

# Frozenset
j = frozenset({"apple", "banana", "cherry"})
print(type(j), j)

# Boolean
k = True
print(type(k), k)

# Bytes
l = b"Hello"
print(type(l), l)

# Byte Array
m = bytearray(5)
print(type(m), m)

# Memory View
n = memoryview(bytes(5))
print(type(n), n)
