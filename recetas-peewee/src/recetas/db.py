from peewee import *
import pymysql

pymysql.install_as_MySQLdb()

db = MySQLDatabase(
    'recetas_db',
    user='root',
    password='abc123.',
    host='127.0.0.1',
    port=3306
)


