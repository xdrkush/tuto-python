# Les boucles

# Décommenter les boucle une par une

# notre variable i
i = 1

# WHILE

# # Boule classique while
# while i <= 6:
#   print(i)
#   i += 1

# # Boucle avec un break
# # Break permet de metre fin à une boucle
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# # Boucle avec un continue
# # Continue permet de continuer même si la condition est respecter
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# # Boucle avec gestion de l'erreur
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# FOR

# fruits = ["apple", "banana", "cherry"]
# # Parcourir un tableau (list)
# for x in fruits:
#   print(x)

# # Parcourir une chaine de caractère
# for x in "banana":
#   print(x)

# # Rechercher dans un tableau
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# # Parcourir un nombre connu
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")