# Gestion-de-videojuegos (Mateus Leandro)

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