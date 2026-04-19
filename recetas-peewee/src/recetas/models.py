from peewee import *
from .db import db

class BaseModel(Model):
    class Meta:
        database = db

class Receta(BaseModel):
    nombre = CharField()
    tiempoC = IntegerField()
    imagen = CharField()
    tempada = CharField()
    fav = BooleanField()
    etiqueta = CharField()

class Ingrediente(BaseModel):
    nombreIng = CharField()
    umedida = CharField()
    cantidad = CharField()
    receta = ForeignKeyField(Receta, backref='ingredientes')

class Preparacion(BaseModel):
    orden = IntegerField()
    descripcion = TextField()
    receta = ForeignKeyField(Receta, backref='pasos')

class MenuSemanal(BaseModel):
    fecha = DateField()
    tipoComida = CharField()
    numSemana = IntegerField()

class MenuReceta(BaseModel):
    menu = ForeignKeyField(MenuSemanal)
    receta = ForeignKeyField(Receta)