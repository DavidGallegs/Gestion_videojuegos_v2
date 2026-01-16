from src.gestor.etapas.tuplas import videojuegos

catalogo = {}

for titulo, year, genero in videojuegos:
    clave = titulo.lower().replace(" ", "_")
    catalogo[clave] = {
        "titulo": titulo,
        "anio": year,
        "genero": {genero}
    }

def crear_juego(catalogo, titulo, anio, genero):
    clave = titulo.lower().replace(" ", "_")
    if clave in catalogo:
        print(f"El juego '{titulo}' ya existe.")
    else:
        catalogo[clave] = {"titulo": titulo, "anio": anio, "genero": {genero}}
        print(f"{titulo} añadido correctamente.")

def leer_juego(catalogo, clave):
    if clave in catalogo:
        print(f"{catalogo[clave]}")
    else:
        print("No se encontró ese juego.")

def actualizar_juego(catalogo, clave, nuevo_year=None, nuevo_genero=None):
    if clave in catalogo:
        if nuevo_year:
            catalogo[clave]["anio"] = nuevo_year
        if nuevo_genero:
            catalogo[clave]["genero"].add(nuevo_genero)
        print(f"'{catalogo[clave]['titulo']}' actualizado correctamente.")
    else:
        print("No existe ese juego.")

def eliminar_juego(catalogo, clave):
    if clave in catalogo:
        eliminado = catalogo.pop(clave)
        print(f"'{eliminado['titulo']}' eliminado correctamente.")
    else:
        print("No existe ese juego.")
