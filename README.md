# Gestion-de-videojuegos 

Práctica realizada por el grupo 3 conformado por Alejandro Rodrigo, David Gallegos, Francisco Javier López y Mateus Leandro.

## Dev A: CSV (Alejandro Rodrigo)
### Realización del programa

Almacenar en fichero de CSV

- Pedir al usuario un nombre de fichero para guardar dentro de el catálogo de videojuegos
en un fichero de tetxo en formato CSV.

### Implementación en main.py

En main.py, se debe de añadir en la parte superior del código, al principio del todo la siguiente línea "from src.gestor.exportar_csv import guardar_catalogo_csv". 
Para luego en este añadir en el menú la opción de exportarlo y la llamada de la función en el propio main.py

## Dev C: JSON (Mateus Leandro)

### Funcionalidades agregadas
- Exportación del catálogo de videojuegos a archivo JSON
- Lectura y presentación de un catálogo almacenado en un archivo JSON

### Probar
- Ejecutar python3 main.py
- Seleccionar en el menú las nuevas funcionalidades: 12 y 13
- Probar su funcionamiento

### Archivos modificados
- gestor/json.py: Nuevo módulo con las funciones de escritura y lectura JSON para catálogos
- main.py: He importado el nuevo módulo y sus funciones, he modificado la función mostrar_catalogo() para que acepte como argumento un catálogo (en vez de imprimir solo el catálogo global) y he modificado el menú con las nuevas opciones 12 y 13
- Adicionalmente, he agregado un .gitignore para ignorar las carpetas __pycache__ y he eliminado el rastreo con git rm -r --cached