from os import path, strerror
import json

def exportar_json(catalogo, directorio, nombre):
    ruta_completa = path.join(path.normpath(directorio), nombre + ".json")

    # Ahora mismo, el catálogo no es serializable porque el campo "genero" de videojuego es un set por pedido expreso de la práctica anterior (aunque es innecesario porque sólo hay un género por videojuego; probablemente sea un error). Por lo tanto, si queremos exportar a JSON el catálogo, debemos convertir el set a un objeto serializable (o cambiar el set por un str si lo autoriza Álvaro)

    catalogo_serializable = {}

    for k, v in catalogo.items():
        videojuego = {}
        for subk, subv in v.items():
            if isinstance(subv, set):
                videojuego[subk] = list(subv)
            else:
                videojuego[subk] = subv
        catalogo_serializable[k] = videojuego

    try:
        with open(ruta_completa, "w", encoding="utf-8") as archivo_json:
            json.dump(catalogo_serializable, archivo_json, ensure_ascii=False, indent=4)
        
        print(f"Catálogo exportado a JSON correctamente: '{ruta_completa}'")
        
    except IOError as e:
        print(f"Error al exportar a JSON el catálogo:", strerror(e.errno))

def leer_json(ruta):
    ruta = path.normpath(ruta)

    try:
        with open(ruta, "r", encoding="utf-8") as archivo_json:
            return json.load(archivo_json)
        
    except IOError as e:
        print(f"Error al leer '{ruta}':", strerror(e.errno))
        return None
    except json.JSONDecodeError as e:
        print(f"Error de formato JSON en '{ruta}': {e}")
        return None