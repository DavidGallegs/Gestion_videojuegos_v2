from src.gestor.catalogo import catalogo, crear_juego, actualizar_juego, eliminar_juego
from src.gestor.busquedas import buscar_por_titulo, buscar_parcial, buscar_por_genero, buscar_por_rango
from src.gestor.estadisticas import total_juegos, conteo_por_genero

activo = True

def mostrar_catalogo():
    print("-------------------------------")
    print("\nCatálogo de videojuegos:")
    for juego in catalogo.values():
        generos = ", ".join(juego["genero"])
        print(f"- {juego['titulo']} ({juego['anio']}) | Género(s): {generos}")


def mostrar_estadisticas():
    print("\nEstadísticas del catálogo:")
    print(f"Total de videojuegos: {total_juegos(catalogo)}")
    print("Conteo por género:")
    for genero, cantidad in conteo_por_genero(catalogo).items():
        print(f"  - {genero}: {cantidad}")
    print()

def menu():
    global activo
    while activo:
        print("""\n--- OPCIONES ---
1. Mostrar lista de Videojuegos
2. Buscar videojuego por título exacto
3. Buscar videojuego por fragmento de título
4. Buscar videojuego por género
5. Buscar videojuego por rango de fechas
6. Añadir Videojuegos
7. Actualizar información de un Videojuego
8. Eliminar Videojuego
9. Mostrar estadísticas de la lista de Videojuegos
0. Salir 
---------------------------------------""")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                mostrar_catalogo()

            case "2":
                titulo = input("Título exacto: ")
                juego = buscar_por_titulo(catalogo, titulo)
                print(juego if juego else "No encontrado.")

            case "3":
                fragmento = input("Fragmento del título: ")
                resultados = buscar_parcial(catalogo, fragmento)
                for juego in resultados:
                    print(juego)

            case "4":
                genero = input("Género: ")
                resultados = buscar_por_genero(catalogo, genero)
                for juego in resultados:
                    print(juego)

            case "5":
                try:
                    min_año = int(input("Año mínimo: "))
                    max_año = int(input("Año máximo: "))
                    resultados = buscar_por_rango(catalogo, min_año, max_año)
                    for juego in resultados:
                        print(juego)
                except ValueError:
                    print("Introduce años válidos.")

            case "6":
                titulo = input("Título: ")
                try:
                    anio = int(input("Año: "))
                    genero = input("Género: ")
                    crear_juego(catalogo, titulo, anio, genero)
                except ValueError:
                    print("Año inválido.")

            case "7":
                clave = input("Clave del juego (título en minúsculas con guiones bajos): ")
                nuevo_year = input("Nuevo año (dejar vacío para no cambiar): ")
                nuevo_genero = input("Nuevo género (dejar vacío para no cambiar): ")
                actualizar_juego(
                    catalogo,
                    clave,
                    nuevo_year=int(nuevo_year) if nuevo_year else None,
                    nuevo_genero=nuevo_genero if nuevo_genero else None
                )

            case "8":
                clave = input("Clave del juego a eliminar [Usar guiones en nombres de más de una sílaba]: ")
                eliminar_juego(catalogo, clave)

            case "9":
                mostrar_estadisticas()

            case "0":
                print("Fin del programa")
                activo = False

            case _:
                print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
