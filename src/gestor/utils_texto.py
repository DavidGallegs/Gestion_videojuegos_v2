def generar_clave(titulo):
    return titulo.lower().replace(" ", "_")

def normalizar_genero(genero):
    return genero.strip().title()
