CREATE DATABASE IF NOT EXISTS recetas_db;
USE recetas_db;

CREATE TABLE IF NOT EXISTS recetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tiempoC INT,
    imagen VARCHAR(255),
    tempada VARCHAR(50),
    fav BOOLEAN,
    etiqueta VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS ingredientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombreIng VARCHAR(100),
    umedida VARCHAR(50),
    cantidad VARCHAR(50),
    receta_id INT,
    FOREIGN KEY (receta_id) REFERENCES recetas(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS preparacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    orden INT,
    descripcion TEXT,
    receta_id INT,
    FOREIGN KEY (receta_id) REFERENCES recetas(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS menu_semanal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    tipoComida VARCHAR(50),
    numSemana INT
);

CREATE TABLE IF NOT EXISTS menu_recetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    receta_id INT,
    FOREIGN KEY (menu_id) REFERENCES menu_semanal(id) ON DELETE CASCADE,
    FOREIGN KEY (receta_id) REFERENCES recetas(id) ON DELETE CASCADE
);