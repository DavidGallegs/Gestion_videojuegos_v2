import csv

def guardar_catalogo_csv(catalogo):
    nombre_fichero = input("Introduce el nombre del fichero CSV: ")

    if not nombre_fichero.endswith(".csv"):
        nombre_fichero += ".csv"

    try:
        with open(nombre_fichero, mode="w", newline="", encoding="utf-8") as fichero:
            writer = csv.writer(fichero, delimiter=';')

            # Cabecera
            writer.writerow(["Título", "Año", "Género"])

            # Datos del catálogo
            for juego in catalogo.values():
                generos = ", ".join(juego["genero"])
                writer.writerow([
                    juego["titulo"],
                    juego["anio"],
                    generos
                ])

        print(f"Catálogo guardado correctamente en '{nombre_fichero}'")

    except Exception as e:
        print("Error al guardar el catálogo:", e)
