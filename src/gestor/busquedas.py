def buscar_por_titulo(catalogo, titulo):
    clave = titulo.lower().replace(" ", "_")
    return catalogo.get(clave, None)

def buscar_parcial(catalogo, fragmento):
    fragmento = fragmento.lower()
    return [v for k, v in catalogo.items() if fragmento in k]

def buscar_por_genero(catalogo, genero):
    genero = genero.title()
    return [v for v in catalogo.values() if genero in v["genero"]]

def buscar_por_rango(catalogo, anio_min, anio_max):
    return [v for v in catalogo.values() if anio_min <= v["anio"] <= anio_max]
