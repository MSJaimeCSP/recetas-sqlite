# Exercicio 8: Conxuntos
# A partir destes conxuntos:



conx_a = {1, 2, 3, 4, 5}
conx_b = {4, 5, 6, 7, 8}

# Realiza estas operacións:

# Unión de ambos conxuntos

union_conx = conx_a.union(conx_b)

print('Unión de ambos conxuntos-> ',union_conx)

# Intersección

intersec = conx_a.intersection(conx_b)

print('Intersección ->', intersec)

# Diferencia (A - B)

difer = conx_a.difference(conx_b)

print('Diferencia (A - B) ->', difer)

# Diferencia simétrica

simetrica = conx_a.symmetric_difference(conx_b)

print('Diferencia simétrica -> ', simetrica)

# Verifica si 3 está en A

verif = 3 in conx_a

print('Verifica si 3 está en A -> ', verif)

