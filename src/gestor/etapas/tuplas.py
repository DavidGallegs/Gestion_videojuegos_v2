# Etapa 2: Tuplas

# 1. Lista de tuplas (título, año, género)
videojuegos = [
    ("The Legend of Zelda Breath of the Wild", 2017, "Aventura"),
    ("God of War", 2005, "Acción"),
    ("Red Dead Redemption 2", 2018, "Mundo abierto"),
    ("Hollow Knight Silksong", 2025, "Metroidvania"),
    ("Elden Ring", 2022, "Rol"),
    ("Undertale", 2015, "Aventura"),
    ("Minecraft", 2009, "Mundo abierto"),
]

if __name__ == "__main__":
    # 2. Recorrer la lista e imprimir los datos con formato claro
    print("Catálogo de videojuegos:")
    for titulo, año, genero in videojuegos:
        print(f"'{titulo} ({año}) {genero}'")
