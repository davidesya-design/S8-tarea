"""
Módulo para gestionar el menú de selección de scripts.

Este módulo proporciona la interfaz para seleccionar,
visualizar y ejecutar scripts Python.
"""

import os
from modules.display import mostrar_codigo
from modules.executor import ejecutar_codigo
from modules.delete import eliminar_archivo


def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra el menú de scripts y permite ejecutarlos.
    
    Args:
        ruta_sub_carpeta (str): Ruta de la subcarpeta con scripts.
    """
    scripts = [
        f.name for f in os.scandir(ruta_sub_carpeta) 
        if f.is_file() and f.name.endswith('.py')
    ]

    while True:
        print("\n" + "-" * 60)
        print("SCRIPTS - Selecciona un script para ver y ejecutar")
        print("-" * 60)
        
        for i, script in enumerate(scripts, start=1):
            print(f"  {i} - {script}")
        print("  0 - Regresar al submenú anterior")
        print("  9 - Regresar al menú principal")
        print("  D - Eliminar un script")

        eleccion_script = input("\nElige un script, '0' para regresar, '9' al menú principal o 'D' para eliminar: ")
        
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        elif eleccion_script.upper() == 'D':
            mostrar_opciones_eliminar(ruta_sub_carpeta, scripts)
            # Recargar lista después de eliminar
            scripts = [
                f.name for f in os.scandir(ruta_sub_carpeta) 
                if f.is_file() and f.name.endswith('.py')
            ]
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("\n¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("✓ El script no se ejecutó.")
                        else:
                            print("⚠ Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts...")
                else:
                    print("⚠ Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("⚠ Opción no válida. Por favor, intenta de nuevo.")


def mostrar_opciones_eliminar(ruta_sub_carpeta, scripts):
    """
    Muestra opciones para eliminar un script.
    
    Args:
        ruta_sub_carpeta (str): Ruta de la subcarpeta.
        scripts (list): Lista de scripts disponibles.
    """
    print("\n" + "-" * 60)
    print("ELIMINAR SCRIPT")
    print("-" * 60)
    
    for i, script in enumerate(scripts, start=1):
        print(f"  {i} - {script}")
    print("  0 - Cancelar")
    
    eleccion = input("\nElige el script a eliminar o '0' para cancelar: ")
    
    if eleccion == '0':
        print("✓ Operación cancelada.")
    else:
        try:
            eleccion = int(eleccion) - 1
            if 0 <= eleccion < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion])
                eliminar_archivo(ruta_script)
            else:
                print("⚠ Opción no válida.")
        except ValueError:
            print("⚠ Opción no válida.")
