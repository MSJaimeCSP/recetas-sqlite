-- Tabla RECETAS
CREATE TABLE IF NOT EXISTS recetas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE,
    tiempoC INTEGER,
    imagen TEXT,
    tempada TEXT,
    fav INTEGER,
    etiqueta TEXT
);

-- Tabla INGREDIENTES
CREATE TABLE IF NOT EXISTS ingredientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreIng TEXT,
    umedida TEXT,
    cantidad REAL,
    receta_id INTEGER,
    FOREIGN KEY (receta_id) REFERENCES recetas(id)
);

-- Tabla PREPARACION
CREATE TABLE IF NOT EXISTS preparacion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orden INTEGER,
    descripcion TEXT,
    receta_id INTEGER,
    FOREIGN KEY (receta_id) REFERENCES recetas(id)
);

-- Tabla MENU_SEMANAL
CREATE TABLE IF NOT EXISTS menu_semanal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    tipoComida TEXT,
    numSemana INTEGER
);

-- Tabla MENU_RECETAS (relación N:M)
CREATE TABLE IF NOT EXISTS menu_recetas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    menu_id INTEGER,
    receta_id INTEGER,
    FOREIGN KEY (menu_id) REFERENCES menu_semanal(id),
    FOREIGN KEY (receta_id) REFERENCES recetas(id)
);