# Gestion-de-videojuegos 

Práctica realizada por el grupo 3 conformado por Alejandro Rodrigo, David Gallegos, Francisco Javier López y Mateus Leandro.

## Integrado (David Gallegos)

### En github

- Aceptar las pulls request de las ramas `alex` y`json` a  la rama `main`
- Resolver conflictos entre archivos para poder hacer las fusiones de ramas.  
- Crear el .gitignore para evitar que __pycache__ se suba desde cualquier ubicación del programa

### Modificaciones en archivos

- Moficaciones oportunas y fusión de la información en el archivo README.md
- Reestructuración del código de main, añadiendo las opciones `10,11,12,13` en el `match` de `main.py`
- Crear la carpeta `func_ficheros` donde se alojan los ficheros creados en esta práctica
- Escribir las rutas necesarias en `main.py` para que funcione todo correctamente

### Comprobación del funcionamiento

Para comprobar que todos los códigos de Dev A,B y C funcionen correctamente estos son los pasos de mi testeo:
Antes de nada el testeo se realizo tras crear la carpeta `func_ficheros` y realizar las rutas oportunas en `main.py`

1. Exportar CSV
    1. Elegimos la opción 10
    2. Nombre del fichero `catalogo`
    3. En la carpeta raiz se ha creado un archivo llamado `catalogo.csv`
2. Leer CSV
    1. Elegimos la opción 11
    2. Seleccionamos el nombre del fichero poniendo `catalogo` sin extensión, en la terminal se escribira el contenido del archivo
3. Exportar JSON
    1. Seleccionamos la opción 12
    2. Especifique el directorio de guardado: ponemos `.`
    3. Nombre del archivo ponemos `catalogo`
    4. En main se ha creado un archivo json llamado `catalogo.json`
4. Leer JSON
    1. Seleccionamos la opción 13
    2. Escribimos `catalogo.json`
    3. Se mostrará en terminal la información del archivo json

## Dev A: CSV (Alejandro Rodrigo)
### Realización del programa

Almacenar en fichero de CSV

- Pedir al usuario un nombre de fichero para guardar dentro de el catálogo de videojuegos
en un fichero de tetxo en formato CSV.

### Implementación en main.py

En main.py, se debe de añadir en la parte superior del código, al principio del todo la siguiente línea "from src.gestor.exportar_csv import guardar_catalogo_csv". 
Para luego en este añadir en el menú la opción de exportarlo y la llamada de la función en el propio main.py

## Dev B: CSV (Francisco Javier)

### Realización del programa

Implementar la función de leer catálogo creando el archivo leer_catalogo_csv.py, que contiene
la función leer_catalogo_csv()

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
