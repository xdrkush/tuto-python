# Condition

x, y, z = 5, 8, 15

# Condition if, elif, else
if x < y:
    # %s permet de récuperer une varible python dans notre string
    print('%s est plus petit que %s'%(x, y))
elif x > y:
    print('%s est plus grand que %s'%(x, y))
else:
    print('%s est égal à %s'%(x, y))

# Condition if sur une ligne
if z > x: print("%s est plus grand que %s"%(z, x))

# Condition if, else sur une ligne
print("A") if x > y else print("B")

# Double condition
if y > x and z > y:
  print("Les deux contions return True")

# Une condition
if x > y or z > y:
  print("Une des 2 condition return True")

if z > 10:
  print("Z est plus grand que 10,")
  if x > 20:
    print("et X est plus grand que 20!")
  else:
    print("mais X est plus petit que 20")