from tuplas import videojuegos

def eliminar_generos(num_veces):
    for i in range(num_veces):
        if len(generos) > 1:
            elemento_eliminado = generos.pop()
            print("Se eliminó:", elemento_eliminado)

generos = {genero for _, _, genero in videojuegos}

eliminar_generos(2)
generos.add("Roguelike")
generos.add("Estrategia")
generos.add("Deporte")


genero_favorito = input("Dime tu género de videojuegos favorito: ").strip().title()
print()

if genero_favorito in generos:
    print(f"El género '{genero_favorito}' está en la colección")
else:
    print(f"El género '{genero_favorito}' no está en la colección")

    print()

generos_amigo = {"Simulación", "Novela", "Aventura", "Shooter"}

union = generos | generos_amigo
interseccion = generos & generos_amigo
diferencia = generos - generos_amigo

print("Todos los géneros (unión):", union if union else "N/A")
print("Coincidencias (intersección):", interseccion if interseccion else "N/A")
print("Diferencia:", diferencia if diferencia else "N/A")