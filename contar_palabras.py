"""
Recoge una frase por teclado y usa un bucle y un diccionario
para contar cuántas veces aparece cada palabra.
Imprime el diccionario resultante.
"""

frase = input("Introduce una frase: ")

palabras = {}

lista_palabras = frase.split(" ")

for palabra in lista_palabras:
    palabras.setdefault(palabra, 0)
    palabras[palabra] += 1

print(palabras)
