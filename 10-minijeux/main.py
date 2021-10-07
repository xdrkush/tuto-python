# minijeux

# Import de lib
from random import *
from colorama import Back, Style

# Nos variables
max_try = 6  # nombre d'essaie maximum
mystery_number = randint(0, 100)  # génération de notre nombre aléatoir
i = 1  # essai en cours

# Print pour le démarage de notre appli
print('Devinez un nombre entre 0 et 100 en 6 essaie !')

# On démarre notre boucle afin d'incrémenter i afin de le comparé à mystery_number
while i < max_try + 1:
    print("essaie numéro: " + str(i))  # on log ne nombre d'éssai en cours
    x = input()  # on récupère la valeur taper par le joueur
    i += 1  # on incrémente le nombre d'essai
    if int(x) == mystery_number:  # notre condition pour checker si le nombre est correct
        print(Back.GREEN + "Vous avez gagné !" +
              Style.RESET_ALL)  # log en cas de victoire
        break
    if int(x) < mystery_number:  # condition si le joueur à mit un nombre trop petit
        print("Trop petit !")  # log
    if int(x) > mystery_number:  # condition si le joueur à mit un nombre trop grand
        print("Trop grand !")  # log
else: # condition si le joueur à dépasser le nombre d'éssai maximum
    print(Back.RED + 'Vous avez perdu ! Le nombre à deviner était le ' + str(mystery_number) + Style.RESET_ALL) # log si le joueur à perdu
