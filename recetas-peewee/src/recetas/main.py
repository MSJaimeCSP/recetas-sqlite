from .db import db
from .models import *

def crear_tablas():
    db.connect()
    db.create_tables([
        Receta, Ingrediente, Preparacion, MenuSemanal, MenuReceta
    ])

def crear_receta():
    nombre = input("Nombre receta: ")
    tiempo = int(input("Tiempo: "))

    receta = Receta.create(
        nombre=nombre,
        tiempoC=tiempo,
        imagen="img.jpg",
        tempada="Todo el año",
        fav=True,
        etiqueta="General"
    )

    #  INGREDIENTES
    while True:
        nombre_ing = input("Ingrediente (N para salir): ")
        if nombre_ing.lower() == "n":
            break

        unidad = input("Unidad: ")
        cantidad = input("Cantidad: ")

        Ingrediente.create(
            nombreIng=nombre_ing,
            umedida=unidad,
            cantidad=cantidad,
            receta=receta
        )

    #  PASOS 
    orden = 0
    while True:
        paso = input("Paso (N para salir): ")
        if paso.lower() == "n":
            break

        orden += 1

        Preparacion.create(
            orden=orden,
            descripcion=paso,
            receta=receta
        )

    print("✅ Receta completa creada")

def ver_recetas():
    for r in Receta.select():
        print(f"{r.nombre} - {r.tiempoC} min")

def crear_menu():
    fecha = input("Fecha (YYYY-MM-DD): ")
    tipo = input("Tipo comida: ")
    semana = int(input("Semana: "))

    menu = MenuSemanal.create(
        fecha=fecha,
        tipoComida=tipo,
        numSemana=semana
    )

    print("\nRecetas disponibles:")
    for r in Receta.select():
        print(f"{r.id} - {r.nombre}")

    # 👉 RELACIÓN menú-recetas
    while True:
        rid = input("ID receta (N para salir): ")

        if rid.lower() == "n":
            break

        MenuReceta.create(
            menu=menu,
            receta=int(rid)
        )

    print("✅ Menú semanal creado")

def ver_menus():
    for m in MenuSemanal.select():
        print(f"\n📅 {m.fecha} - {m.tipoComida} (Semana {m.numSemana})")

        relaciones = MenuReceta.select().where(MenuReceta.menu == m)

        for rel in relaciones:
            print(f"- {rel.receta.nombre}")

def menu():
    while True:
        print("\n--- MENÚ PEEWEE ---")
        print("1. Crear receta")
        print("2. Ver recetas")
        print("3. Crear menú semanal")
        print("4. Ver menús")
        print("5. Salir")

        op = input("Opción: ")

        if op == "1":
            crear_receta()
        elif op == "2":
            ver_recetas()
        elif op == "3":
            crear_menu()
        elif op == "4":
            ver_menus()
        elif op == "5":
            break

if __name__ == "__main__":
    crear_tablas()
    menu()