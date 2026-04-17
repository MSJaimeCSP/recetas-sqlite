import os

from abc import ABC, abstractmethod

# realizar conexion a la BBDD

from recetas.db import conectar

conexion = conectar()
cursor = conexion.cursor()


# ------- Creamos Clases -----

class MenuError(Exception):
    """Clase para gestionar errores específicos del Menú Semanal."""
    pass

class RecetaBase(ABC):
    def __init__(self,nombre,tiempoC):
        self.__nombre= nombre
        self.__tiempoC = tiempoC

    def get_nombre(self):
        return self.__nombre

    # Definimos un método que los hijos SÍ O SÍ deben tener
    @abstractmethod
    def preparar(self):
        pass

class Receta(RecetaBase):

    __biblioteca = []  # usar en la classmethod , almacenar todas las recetas
    
    @classmethod     # creamos un decorador para ver todas las recetas
    def ver_biblioteca(cls):
        return cls.__biblioteca

    def __init__(self, nombre, tiempoC,imagen,tempada, fav,etiqueta):

        super().__init__(nombre, tiempoC)

        self.__ingredientes = []       # Agregación
        self.__pasos_preparacion = []  # Composición
        self.__tempada = tempada
        self.__fav = fav
        self.etiqueta = etiqueta       # Público
        self.imagen = imagen           # Público
        
        #Registro en la biblioteca de la clase
        Receta.__biblioteca.append(self)
        

    # Getter de pasos e ingredientes

    def get_pasos(self):
        return self.__pasos_preparacion

    def get_ingredientes(self):
        return self.__ingredientes

    
     # El método para realizar la agregación (Punto 1..* del UML) 
    def agregar_ingredientes(self, nuevo_ingrediente):

        # Aquí es donde realmente se añade a la lista
        self.__ingredientes.append(nuevo_ingrediente)

    # Método para alimentar la composición
    def añadir_paso(self, orden, descripcion):
        nuevo_paso = Preparacion(orden, descripcion)
        self.__pasos_preparacion.append(nuevo_paso) 

    # implementar el método abstracto 
    def preparar(self):
        return f"Preparando la receta: {self.get_nombre()}"
    
    @classmethod
    def buscar_receta(cls, nombre_busca):
        return [r for r in cls.__biblioteca if nombre_busca in r.get_nombre()]
    
    def __str__(self):
        return f"{self.get_nombre()} | Tiempo: {self._RecetaBase__tiempoC} min | Ingredientes: {len(self.__ingredientes)} | Pasos: {len(self.__pasos_preparacion)}"

class Ingrediente:
    def __init__(self, nombreIng, umedida, cantidad):
        self.__nombreIng = nombreIng
        self.__umedida = umedida
        self.__cantidad = cantidad

class Preparacion:
    def __init__(self, orden, descripcion):
        self.__orden = orden
        self.__descripcion= descripcion

class MenuSemanal:
    def __init__(self, id, fecha, tipoComida, numSemana):
        self.id = id
        self.fecha = fecha
        self.tipoComida = tipoComida
        self.numSemana = numSemana
        self.__lista_recetas = []

    def guardar(self, cursor):
        cursor.execute("""
        INSERT INTO menu_semanal (fecha, tipoComida, numSemana)
        VALUES (%s, %s, %s)
        """, (self.fecha, self.tipoComida, self.numSemana))

        self.id = cursor.lastrowid
    def agregar_receta(self, cursor, receta_id):
        cursor.execute("""
        INSERT INTO menu_recetas (menu_id, receta_id)
        VALUES (%s, %s)
        """, (self.id, receta_id))


    # Dentro de la clase MenuSemanal — para eliminar del menú
    def eliminar_receta_del_menu(self, receta):
        if receta not in self.__lista_recetas:
            raise MenuError("La receta no está en este menú.")
        self.__lista_recetas.remove(receta)
        print(f"Receta '{receta.get_nombre()}' eliminada del menú semana {self.numSemana}")

    # DUNDER METHOD -> Para ver cuántas recetas hay en el menú
    def __len__(self):
        return len(self.__lista_recetas)    

 
try:

    # Crear una Receta (Usando tu clase que hereda de RecetaBase)
    def crear_receta(cursor, conexion):

        nombre = input("Nombre receta: ")
        tiempo = int(input("Tiempo: "))

        #  Llamamos funcion crear ingredientes 
        ingredientes = Creo_Ingredientes()

        mi_receta = Receta(nombre, tiempo, "img.jpg", "Todo el año", True, "General")

        for ing in ingredientes:
            mi_receta.agregar_ingredientes(ing)

        print("Receta creada correctamente")

        # Añadir pasos de preparación
        orden_paso= 0
        while True:
            
            pasos_receta = input("Introduce pasos (o pulsa N para terminar): ")
    
            if pasos_receta.lower() == "n":
                break
    
            orden_paso += 1
            mi_receta.añadir_paso(orden_paso, pasos_receta)

        

    # Insertar en la BD
        cursor.execute(
    "SELECT * FROM recetas WHERE nombre = %s", 
    (mi_receta.get_nombre(),)
    )
        existe = cursor.fetchone()

        if not existe:
            cursor.execute("""
            INSERT INTO recetas (nombre, tiempoC, imagen, tempada, fav, etiqueta)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                mi_receta.get_nombre(),
                tiempo,
                mi_receta.imagen,
                mi_receta._Receta__tempada,
                int(mi_receta._Receta__fav),
                mi_receta.etiqueta
            ))

        receta_id = cursor.lastrowid  # guardar clave para otras tablas

        # añadir ingredientes

        for ing in mi_receta.get_ingredientes():     # leemos del getter de ingredientes para guardar toda la lista
            cursor.execute("""
            INSERT INTO ingredientes (nombreIng, umedida, cantidad, receta_id)
            VALUES (%s, %s, %s, %s)
            """, (
                ing._Ingrediente__nombreIng,
                ing._Ingrediente__umedida,
                ing._Ingrediente__cantidad,
                receta_id
            ))

        # añadir pasos

        for paso in mi_receta.get_pasos():
            cursor.execute("""
            INSERT INTO preparacion (orden, descripcion, receta_id)
            VALUES (%s, %s, %s)
            """, (
                paso._Preparacion__orden,
                paso._Preparacion__descripcion,
                receta_id
            ))
        
        conexion.commit()
        
            # Crear el Menú Semanal y añadir la receta
    
except MenuError as e:
    print(f"Error detectado: {e}")
    conexion.close()
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    conexion.close()






def menu(cursor, conexion):
    while True:
        print("\n--- MENÚ PRINCIPAL MDB---")
        print("1. Crear receta")
        print("2. Ver Recetas")
        print("3. Crear Menu Semanal")
        print("4. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_receta(cursor, conexion)

        elif opcion == "2":
            print("Entrando en ver_recetas()")  # 👈 prueba2
            ver_recetas()

        elif opcion == "3":
            crear_menusemanal(cursor, conexion)

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida")

def crear_menusemanal(cursor, conexion):
    
    from datetime import datetime

    fecha = input("Fecha (YYYY-MM-DD): ")
    datetime.strptime(fecha, "%Y-%m-%d")
    
    tipo = input("Tipo comida: ")
    semana = int(input("Semana: "))

    menu = MenuSemanal(None, fecha, tipo, semana)
    menu.guardar(cursor)

    # 🔥 FALTABA ESTO
    cursor.execute("SELECT id, nombre FROM recetas")
    recetas = cursor.fetchall()

    print("Recetas disponibles:")
    for r in recetas:
        print(f"{r[0]} - {r[1]}")

    # Asociar recetas
    while True:
        receta_id = input("ID receta (o N para terminar): ")

        if receta_id.lower() == "n":
            break

        menu.agregar_receta(cursor, int(receta_id))

    conexion.commit()
    print("Menú creado correctamente")



def ver_recetas():
    print("Listado de recetas")

    cursor.execute("SELECT nombre, tiempoC FROM recetas")
    recetas = cursor.fetchall()

    for nombre, tiempo in recetas:
        print(f"{nombre} - {tiempo} min")

def Creo_Ingredientes():  
        
    lista_ing = []
    while True:
        nombre_ing = input("Nombre del ingrediente (o pulsa N para terminar): ")
        if nombre_ing.lower() == "n":
            break
            
        unidad_ing = input("Unidad:")
        ctdad_ing = input("Cantidad: ")
        print("-------------------")

        # Crear objeto ingrediente
        ing = Ingrediente(nombre_ing, unidad_ing, ctdad_ing)

        # añadir a la lista
        lista_ing.append(ing)
        
        #devolvemos la lista de ingredientes
    return lista_ing


def ejecutar_schema(cursor, conexion):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # sube de /recetas a /src
    ruta = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "data", "schema.sql")
    )
    with open(ruta, "r", encoding="utf-8") as f:
        sql = f.read()
    # dividir por sentencias
    for sentencia in sql.split(";"):
        sentencia = sentencia.strip()
        if sentencia:
            cursor.execute(sentencia)

    conexion.commit()
    print("✅ Base de datos y tablas creadas")



if __name__ == "__main__":
    try:

        ejecutar_schema(cursor, conexion)
        menu(cursor, conexion)

    except MenuError as e:
        print(f"Error detectado: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    finally:
        conexion.close()

