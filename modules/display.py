"""
Módulo para mostrar contenido de archivos Python.

Este módulo proporciona funcionalidad para leer y mostrar
el contenido de archivos de código fuente.
"""

import os


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo Python.
    
    Args:
        ruta_script (str): Ruta del archivo a mostrar.
        
    Returns:
        str: Contenido del archivo si se lee exitosamente, None en caso contrario.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n{'=' * 60}")
            print(f"Código de {ruta_script}")
            print('=' * 60 + "\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None
