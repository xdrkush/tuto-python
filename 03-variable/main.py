# Les Variables

name = "Bruno"
age = 21

# String
print(name, type(name))

# Int
print(age, type(age))
print(age, type(str(age)))

# Age sera devenu une String
print("Bonjour, je suis " + name + " !", " J'ai " + str(age))

# Assigner plusieur variable
va, ri, able = "Orange", "Banana", "Cherry"
print(va, ri, able)

# Multiple varible dans une liste
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

# Concaténation String
a = 'Hello'
b = "World"
c = a + " " + b
print(c)

# Calcul
d = 5
e = 7
f = d + e
print(f)