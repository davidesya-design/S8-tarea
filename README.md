# PROGRAMACIÓN ORIENTADA A OBJETOS

Este repositorio contiene el código fuente desarrollado durante la asignatura **Programación Orientada a Objetos**, impartida en la **Universidad Estatal Amazónica**. Está diseñado como un recurso de apoyo para estudiantes y profesionales interesados en conceptos y prácticas de programación orientada a objetos.

## Información de la asignatura

- **Institución**: Universidad Estatal Amazónica (UEA)  
- **Carrera**: Ingeniería en Tecnologías de la Información  
- **Asignatura**: Programación Orientada a Objetos
- **Estudiante**: Andrew David Valenzuela Yela

## Descripción General

Dashboard interactivo para explorar, ejecutar y gestionar ejemplos de programación orientada a objetos en Python. La aplicación proporciona una interfaz de menú basada en texto que facilita la navegación por diferentes unidades y temas de estudio.

## Características Principales

### 📚 Características del Dashboard

- **Navegación jerárquica**: Acceso organizado a unidades de estudio y sus subcarpetas
- **Visualización de código**: Muestra el contenido de archivos Python con formato legible
- **Ejecución de scripts**: Ejecuta scripts Python en ventanas nuevas según el sistema operativo
- **Gestión de archivos**: 
  - ✓ Eliminar scripts individuales
  - ✓ Eliminar subcarpetas completas
  - ✓ Eliminar unidades de estudio
  - ✓ Confirmación segura antes de cada eliminación
- **Interfaz amigable**: Menús intuitivos con opciones claras
- **Manejo de excepciones**: Control robusto de errores y excepciones

## Contenido del repositorio

Este repositorio incluye:

1. **Ejercicios prácticos** de programación orientada a objetos
2. **Ejemplos de implementación** en Python:
   - Técnicas de programación
   - Programación tradicional vs POO
   - Clases y objetos
   - Herencia
   - Encapsulamiento
   - Polimorfismo
3. **Dashboard interactivo** para explorar ejemplos
4. **Módulos reutilizables** para gestión de archivos y ejecución de scripts
5. **Documentación** clara y apuntes adicionales para reforzar el aprendizaje

## Estructura del Proyecto

```
2525-PROGRAMACION-ORIENTADA-A-OBJETOS/
├── Dashboard.py                    # Punto de entrada principal
├── README.md                       # Este archivo
├── modules/
│   ├── __init__.py                # Paquete Python
│   ├── display.py                 # Mostrar contenido de archivos
│   ├── executor.py                # Ejecutar scripts Python
│   ├── delete.py                  # Eliminar archivos y carpetas
│   ├── menu_main.py               # Menú principal
│   ├── menu_submenu.py            # Submenú de subcarpetas
│   └── menu_scripts.py            # Menú de selección de scripts
├── UNIDAD 1/                      # Contenido de la primera unidad
└── UNIDAD 2/                      # Contenido de la segunda unidad
```

## Objetivos

- Aplicar los principios fundamentales de la programación orientada a objetos
- Desarrollar soluciones eficientes y estructuradas utilizando Python
- Familiarizarse con conceptos como clases, objetos, herencia, polimorfismo y encapsulamiento
- Crear herramientas prácticas para explorar y ejecutar ejemplos educativos

## Tecnologías Utilizadas

- **Python 3.x**
- Módulos estándar: `os`, `subprocess`, `shutil`
- Arquitectura modular con separación de responsabilidades

## Cómo Usar el Dashboard

### Instalación

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/snogales-uea/2525-PROGRAMACION-ORIENTADA-A-OBJETOS.git
   cd 2525-PROGRAMACION-ORIENTADA-A-OBJETOS
   ```

2. Asegúrate de tener Python 3.x instalado:
   ```bash
   python --version
   ```

### Ejecución

1. Ejecuta el Dashboard:
   ```bash
   python Dashboard.py
   ```

2. Sigue el menú interactivo para:
   - **Seleccionar una unidad** de estudio
   - **Elegir una subcarpeta** temática
   - **Ver el código** de un script
   - **Ejecutar** el script en una ventana nueva
   - **Eliminar** archivos, carpetas o unidades (con confirmación)

### Opciones del Menú

- **Números (1-9)**: Seleccionar opciones
- **D**: Eliminar carpetas/archivos
- **0**: Regresar al menú anterior
- **9**: Ir al menú principal (desde el menú de scripts)
- **Ctrl+C**: Salir del programa en cualquier momento

## Procedimiento para contribuir a tu repositorio personal

1. Crear un nuevo repositorio en tu cuenta de GitHub:  
   Visita: https://github.com/new

2. Cambiar el repositorio remoto del proyecto clonado:
   ```bash
   git remote remove origin
   git remote add origin https://github.com/tu-usuario/proyecto-clonado.git
   ```

3. Subir el proyecto a tu repositorio personal:
   ```bash
   git push -u origin main
   ```

## Notas Importantes

- Los scripts se ejecutan en ventanas nuevas (cmd en Windows, xterm en Linux/Mac)
- La eliminación de carpetas y archivos es **irreversible**
- Se solicita confirmación explícita antes de cualquier operación de eliminación
- El código está documentado con docstrings completos

## Licencia

Este proyecto es de uso educativo y forma parte de la asignatura Programación Orientada a Objetos de la Universidad Estatal Amazónica.

## Autor

**Andrew David Valenzuela Yela**  
Estudiante de Ingeniería en Tecnologías de la Información  
Universidad Estatal Amazónica

---

*Última actualización: Febrero 2026*

