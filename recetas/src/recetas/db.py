from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "recetas.db"

def conectar():
    return sqlite3.connect(DB_PATH)