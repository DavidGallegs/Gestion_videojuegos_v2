from tuplas import videojuegos
catalogo = {}


for titulo, year, genero in videojuegos:
    clave = titulo.lower().replace(" ", "_")
    catalogo[clave] = {
        "titulo": titulo,
        "anio": year,
        "genero": {genero}
    }


# --- CRUD ---

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
        print(f"🔄 '{catalogo[clave]['titulo']}' actualizado correctamente.")
    else:
        print("No existe ese juego.")


def eliminar_juego(catalogo, clave):
    if clave in catalogo:
        eliminado = catalogo.pop(clave)
        print(f"'{eliminado['titulo']}' eliminado correctamente.")
    else:
        print("No existe ese juego.")


# --- FUNCIONES DE BÚSQUEDA ---
#-Búsca por título exacto
def buscar_por_titulo(catalogo, titulo):
    clave = titulo.lower().replace(" ", "_")
    return catalogo.get(clave, None)


#-Busca usando una parte del título
def buscar_parcial(catalogo, fragmento):
    fragmento = fragmento.lower()
    return [v for k, v in catalogo.items() if fragmento in k]


#- Búsqueda por genero
def buscar_por_genero(catalogo, genero):
    genero = genero.title()
    return [v for v in catalogo.values() if genero in v["genero"]]


#- Búsqueda por año
def buscar_por_rango(catalogo, anio_min, anio_max):
    return [v for v in catalogo.values() if anio_min <= v["anio"] <= anio_max]

# --- ESTADÍSTICAS DEL CATÁLOGO ---
def total_juegos(catalogo):
    return len(catalogo)


def conteo_por_genero(catalogo):
    conteo = {}
    for v in catalogo.values():
        for g in v["genero"]:
            conteo[g] = conteo.get(g, 0) + 1
    return conteo
