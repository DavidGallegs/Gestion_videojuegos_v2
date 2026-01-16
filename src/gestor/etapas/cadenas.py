from tuplas import videojuegos

nombre_videojuego = input("Escribe el nombre de un videojuego: ")
encontrado = False

for titulo, año, genero in videojuegos:
        if nombre_videojuego.lower().strip() == titulo.lower().strip():
            print(f"Título: {titulo} | Género: {genero} | Año: {año}")
            encontrado = True
            break

if not encontrado:
    print("Ese videojuego no está en la lista")