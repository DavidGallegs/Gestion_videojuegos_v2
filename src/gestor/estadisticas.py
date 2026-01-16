def total_juegos(catalogo):
    return len(catalogo)

def conteo_por_genero(catalogo):
    conteo = {}
    for v in catalogo.values():
        for g in v["genero"]:
            conteo[g] = conteo.get(g, 0) + 1
    return conteo
