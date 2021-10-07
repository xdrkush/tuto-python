# Les fonctions

# Déclaration d'une fonction
def my_function():
  print("Hello from a function")

# appel de la fonction
my_function()

# Parametre de fonction
a = 5
b = 12
def addition(x, y):
  print(x + y)

addition(a, b)

name = 'Bruno'
lname = 'Shaun'
def hello (n, **l):
  print("Welcome to function python %s "%n + l["lname"] + " !")

hello(name, lname = 'Doe')