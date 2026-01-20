import csv

def leer_catalogo_csv():
    nombre_fichero = input("Introduce el nombre del fichero CSV: ")

    if not nombre_fichero.endswith(".csv"):
        nombre_fichero += ".csv"

    catalogo = {}

    try:
        with open(nombre_fichero, mode="r", encoding="utf-8") as fichero:
            reader = csv.reader(fichero, delimiter=';')
            next(reader)

            for fila in reader:
                titulo = fila[0]
                anio = int(fila[1])
                generos = fila[2].split(", ")

                catalogo[titulo] = {
                    "titulo": titulo,
                    "anio": anio,
                    "genero": generos
                }

        print(f"Catálogo cargado correctamente desde '{nombre_fichero}'")
        return catalogo

    except FileNotFoundError:
        print("Error: el fichero no existe.")
    except Exception as e:
        print("Error al leer el catálogo:", e)

    return {}
