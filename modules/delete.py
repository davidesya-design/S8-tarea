"""
Módulo para eliminar archivos y carpetas de forma segura.

Este módulo proporciona funcionalidad para eliminar archivos
y directorios con confirmación del usuario.
"""

import os
import shutil


def eliminar_archivo(ruta_archivo):
    """
    Elimina un archivo después de pedir confirmación.
    
    Args:
        ruta_archivo (str): Ruta del archivo a eliminar.
        
    Returns:
        bool: True si se eliminó exitosamente, False en caso contrario.
    """
    try:
        ruta_absoluta = os.path.abspath(ruta_archivo)
        print(f"\n{'!' * 60}")
        print(f"¿Desea eliminar: {os.path.basename(ruta_archivo)}?")
        print(f"{'!' * 60}")
        
        confirmacion = input("Escriba 'SÍ' para confirmar la eliminación: ")
        
        if confirmacion.upper() in ('SÍ', 'SI'):
            os.remove(ruta_absoluta)
            print(f"✓ Archivo eliminado exitosamente.")
            return True
        else:
            print("✓ Operación cancelada.")
            return False
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return False
    except Exception as e:
        print(f"Ocurrió un error al eliminar el archivo: {e}")
        return False


def eliminar_carpeta(ruta_carpeta):
    """
    Elimina una carpeta y su contenido después de pedir confirmación.
    
    Args:
        ruta_carpeta (str): Ruta de la carpeta a eliminar.
        
    Returns:
        bool: True si se eliminó exitosamente, False en caso contrario.
    """
    try:
        ruta_absoluta = os.path.abspath(ruta_carpeta)
        nombre_carpeta = os.path.basename(ruta_carpeta)
        
        # Contar archivos dentro de la carpeta
        cantidad_elementos = sum([len(files) + len(dirs) for _, dirs, files in os.walk(ruta_absoluta)])
        
        print(f"\n{'!' * 60}")
        print(f"⚠ ADVERTENCIA: Esta acción es irreversible")
        print(f"Carpeta: {nombre_carpeta}")
        print(f"Elementos a eliminar: {cantidad_elementos}")
        print(f"{'!' * 60}")
        
        confirmacion = input("Escriba 'SÍ' para confirmar la eliminación: ")
        
        if confirmacion.upper() in ('SÍ', 'SI'):
            shutil.rmtree(ruta_absoluta)
            print(f"✓ Carpeta y su contenido eliminados exitosamente.")
            return True
        else:
            print("✓ Operación cancelada.")
            return False
    except FileNotFoundError:
        print("La carpeta no se encontró.")
        return False
    except Exception as e:
        print(f"Ocurrió un error al eliminar la carpeta: {e}")
        return False
