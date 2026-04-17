# Recetas - SQLite

## Requisitos

* Python 3

## Configuración

Crear a base de datos:

.. code-block:: bash

sqlite3 data/recetas.db < data/schema.sql

## Execución

.. code-block:: bash

python -m recetas.receta

## Notas

* A base de datos está en data/recetas.db
* O código usa sqlite3
