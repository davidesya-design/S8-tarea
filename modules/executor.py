"""
Módulo para ejecutar scripts Python.

Este módulo proporciona funcionalidad para ejecutar archivos
Python en ventanas nuevas según el sistema operativo.
"""

import os
import subprocess


def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script Python en una ventana nueva.
    
    Args:
        ruta_script (str): Ruta del script a ejecutar.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")
