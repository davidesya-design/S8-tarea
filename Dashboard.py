"""
Dashboard para explorar y ejecutar scripts de Python.

Este módulo proporciona un punto de entrada para la interfaz
de menú interactivo del dashboard.
"""

from modules.menu_main import mostrar_menu


if __name__ == "__main__":
    try:
        mostrar_menu()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")

