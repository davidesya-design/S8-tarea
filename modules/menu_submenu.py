"""
Módulo para gestionar el submenú de selección de subcarpetas.

Este módulo proporciona la interfaz para seleccionar
una subcarpeta dentro de una unidad de estudio.
"""

import os
from modules.menu_scripts import mostrar_scripts
from modules.delete import eliminar_carpeta


def mostrar_sub_menu(ruta_unidad):
    """
    Muestra el submenú para seleccionar una subcarpeta.
    
    Args:
        ruta_unidad (str): Ruta de la unidad de estudio.
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n" + "-" * 60)
        print("SUBMENÚ - Selecciona una subcarpeta")
        print("-" * 60)
        
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"  {i} - {carpeta}")
        print("  0 - Regresar al menú principal")
        print("  D - Eliminar una subcarpeta")

        eleccion_carpeta = input("\nElige una subcarpeta, '0' para regresar o 'D' para eliminar: ")
        
        if eleccion_carpeta == '0':
            break
        elif eleccion_carpeta.upper() == 'D':
            mostrar_opciones_eliminar(ruta_unidad, sub_carpetas)
            # Recargar lista después de eliminar
            sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("⚠ Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("⚠ Opción no válida. Por favor, intenta de nuevo.")


def mostrar_opciones_eliminar(ruta_unidad, sub_carpetas):
    """
    Muestra opciones para eliminar una subcarpeta.
    
    Args:
        ruta_unidad (str): Ruta de la unidad.
        sub_carpetas (list): Lista de subcarpetas disponibles.
    """
    print("\n" + "-" * 60)
    print("ELIMINAR SUBCARPETA")
    print("-" * 60)
    
    for i, carpeta in enumerate(sub_carpetas, start=1):
        print(f"  {i} - {carpeta}")
    print("  0 - Cancelar")
    
    eleccion = input("\nElige la subcarpeta a eliminar o '0' para cancelar: ")
    
    if eleccion == '0':
        print("✓ Operación cancelada.")
    else:
        try:
            eleccion = int(eleccion) - 1
            if 0 <= eleccion < len(sub_carpetas):
                ruta_carpeta = os.path.join(ruta_unidad, sub_carpetas[eleccion])
                eliminar_carpeta(ruta_carpeta)
            else:
                print("⚠ Opción no válida.")
        except ValueError:
            print("⚠ Opción no válida.")
