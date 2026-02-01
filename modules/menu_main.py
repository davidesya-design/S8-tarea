"""
Módulo para gestionar la navegación del menú principal.

Este módulo proporciona la interfaz del menú principal
para seleccionar unidades de estudio.
"""

import os
from modules.menu_submenu import mostrar_sub_menu
from modules.delete import eliminar_carpeta


def mostrar_menu():
    """
    Muestra el menú principal del dashboard.
    
    Permite al usuario seleccionar una unidad de estudio.
    """
    ruta_base = os.path.dirname(os.path.dirname(__file__))

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\n" + "=" * 60)
        print("MENÚ PRINCIPAL - DASHBOARD")
        print("=" * 60)
        
        for key in unidades:
            print(f"  {key} - {unidades[key]}")
        print("  0 - Salir")
        print("\n  D - Eliminar una unidad")
        
        eleccion_unidad = input("\nElige una unidad, '0' para salir o 'D' para eliminar: ")
        
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad.upper() == 'D':
            mostrar_opciones_eliminar(ruta_base, unidades)
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("⚠ Opción no válida. Por favor, intenta de nuevo.")


def mostrar_opciones_eliminar(ruta_base, unidades):
    """
    Muestra opciones para eliminar una unidad.
    
    Args:
        ruta_base (str): Ruta base del proyecto.
        unidades (dict): Diccionario de unidades disponibles.
    """
    print("\n" + "-" * 60)
    print("ELIMINAR UNIDAD")
    print("-" * 60)
    
    for key in unidades:
        print(f"  {key} - {unidades[key]}")
    print("  0 - Cancelar")
    
    eleccion = input("\nElige la unidad a eliminar o '0' para cancelar: ")
    
    if eleccion == '0':
        print("✓ Operación cancelada.")
    elif eleccion in unidades:
        ruta_unidad = os.path.join(ruta_base, unidades[eleccion])
        eliminar_carpeta(ruta_unidad)
    else:
        print("⚠ Opción no válida.")
