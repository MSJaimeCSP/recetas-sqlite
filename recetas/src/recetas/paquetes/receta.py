from abc import ABC, abstractmethod

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


    def __init__(self, nombre, tiempoC,imagen,tempada, fav,etiqueta):

        # Inicializamos la lista de agregación
        self.__ingredientes = []


        super().__init__(nombre, tiempoC)

        self.__tempada= tempada
        self.__fav= fav
        self.etiqueta= etiqueta
        self.imagen= imagen
        
        #Registro en la biblioteca de la clase
        Receta.__biblioteca.append(self)


    # COMPOSICIÓN: Una lista para guardar objetos 'Preparacion'
        self.__pasos_preparacion = []

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
    def __init__(self, fecha, tipoComida, NumSemana):
        self.__fecha = fecha
        self.tipoComida = tipoComida
        self.__NumSemana= NumSemana

# composición MenuSemanal - Recetas

# El menú nace con su propia lista de recetas
        self.__lista_recetas = []

    def agregar_receta_al_menu(self, Receta):
        # Uso de la excepción personalizada
        if Receta is None:
            raise MenuError("No se puede añadir una receta vacía al menú")
        
        # Añadimos la receta a la composición
        self.__lista_recetas.append(Receta)
        print(f"Receta '{Receta.get_nombre()}' añadida al menú de la semana {self.__NumSemana}")

    # DUNDER METHOD -> Para ver cuántas recetas hay en el menú
    def __len__(self):
        return len(self.__lista_recetas)    

try:
    # 1. Crear Ingredientes
    ing1 = Ingrediente("Masa de Pizza", "gramos", 500)
    ing2 = Ingrediente("Tomate", "ml", 100)
    ing3 = Ingrediente("Queso Mozzarella", "gramos", 200)

    # 2. Crear una Receta (Usando tu clase que hereda de RecetaBase)
    mi_pizza = Receta("Pizza Margarita", 20, "pizza.jpg", "Todo el año", True, "Italiana")

    # 3. Agregación: Añadir los ingredientes a la receta
    mi_pizza.agregar_ingredientes(ing1)
    mi_pizza.agregar_ingredientes(ing2)
    mi_pizza.agregar_ingredientes(ing3)

    # 4. Composición: Añadir pasos de preparación
    mi_pizza.añadir_paso(1, "Extender la masa sobre la bandeja.")
    mi_pizza.añadir_paso(2, "Añadir el tomate y el queso.")

    # 5. Composición: Crear el Menú Semanal y añadir la receta
    mi_menu = MenuSemanal("2026-03-23", "Almuerzo", 12)
    
    # Esto activará el print y usará el getter internamente
    mi_menu.agregar_receta_al_menu(mi_pizza)

    # 6. Probar el Dunder Method __len__
    print(f"Número de recetas en el menú: {len(mi_menu)}")

    # 7. Probar la Excepción (Intentar añadir algo vacío)
    # mi_menu.agregar_receta_al_menu(None)  # <--- Descomenta esto para ver el error

except MenuError as e:
    print(f"Error detectado: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

