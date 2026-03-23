<<<<<<< HEAD
frutas = ["mazá", "plátano", "laranxa", "uva", "mazá"]

# Realiza estas operacións:

# Engade "pera" ao final

frutas.append('pera')

# Inserta "kiwi" na posición 2

frutas.insert(2,'kiwi')
# Elimina a primera "mazá"

frutas.pop(0)

# Ordena a lista alfabéticamente

frutas.sort()

# Crea unha nova lista coas frutas que teñen máis de 5 letras

frutas_5 = [frutas for frutas in frutas if len(frutas) > 5]


print(frutas)
=======
frutas = ["mazá", "plátano", "laranxa", "uva", "mazá"]

# Realiza estas operacións:

# Engade "pera" ao final

frutas.append('pera')

# Inserta "kiwi" na posición 2

frutas.insert(2,'kiwi')
# Elimina a primera "mazá"

frutas.pop(0)

# Ordena a lista alfabéticamente

frutas.sort()

# Crea unha nova lista coas frutas que teñen máis de 5 letras

frutas_5 = [frutas for frutas in frutas if len(frutas) > 5]


print(frutas)
>>>>>>> 397adb68688532421a2e8f8a65020ab824a998c1
print('nova lista coas frutas que teñen máis de 5 letras-> ',frutas_5)