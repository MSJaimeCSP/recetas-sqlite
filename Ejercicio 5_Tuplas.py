<<<<<<< HEAD
# Crea unha tupla coas coordenadas (x, y, z)



coordenadas = (3, 7, 2)

# Realiza estas operacións:

# Accede a cada coordenada individualmente

for coord in coordenadas:
    print(coord)

# Intenta modificar unha coordenada (qué ocorre?)

#coordenadas[1] = 7

print(coordenadas)

# Convirte a tupla a lista

c_lista = list(coordenadas)

print('Convirte a tupla a lista ->', c_lista)

# Crea unha nova tupla concatenando (1, 2, 3)


coord_new=tuple(c_lista)+(1,2,3)


print("nueva tupla -> ", coord_new)


# Desempaqueta a tupla en variables x, y, z

x,y,z = coordenadas

=======
# Crea unha tupla coas coordenadas (x, y, z)



coordenadas = (3, 7, 2)

# Realiza estas operacións:

# Accede a cada coordenada individualmente

for coord in coordenadas:
    print(coord)

# Intenta modificar unha coordenada (qué ocorre?)

#coordenadas[1] = 7

print(coordenadas)

# Convirte a tupla a lista

c_lista = list(coordenadas)

print('Convirte a tupla a lista ->', c_lista)

# Crea unha nova tupla concatenando (1, 2, 3)


coord_new=tuple(c_lista)+(1,2,3)


print("nueva tupla -> ", coord_new)


# Desempaqueta a tupla en variables x, y, z

x,y,z = coordenadas

>>>>>>> 397adb68688532421a2e8f8a65020ab824a998c1
print("Desempaquetado -> ",x,y,z)