# Crea una lista con los títulos de tus 5 videojuegos favoritos
videojuegos = [
    "The Legend of Zelda Breath of the Wild",
    "Minecraft",
    "God of War",
    "Red Dead Redemption 2",
    "Super Mario Odyssey",
]

# Añade nuevos videojuegos al final de la lista
videojuegos.append("Elden Ring")
videojuegos.append("Undertale")

# Inserta un videojuego en una posición específica
videojuegos.insert(2, "Hollow Knight Silksong")

# Elimina un videojuego de la lista
videojuegos.remove("Super Mario Odyssey")

# Recorre la lista e imprime los títulos numerados
print("Lista de videojuegos:")
for i in range(len(videojuegos)):
    print(str(i + 1) + ". " + videojuegos[i])  # Sumamos 1 porque empieza en 0

# Muestra la lista ordenada alfabéticamente
print("\nLista ordenada alfabéticamente:")
lista_ordenada = sorted(videojuegos)

for i in range(len(lista_ordenada)):
    print(f"{i + 1}. {lista_ordenada[i]}")
