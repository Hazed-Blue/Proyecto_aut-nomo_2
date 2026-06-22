# Proyecto_aut-nomo_2
Tarea de Lógica de programación
## ahorcado-game-python
# Juego del Ahorcado en Python - Diseño Funcional y Arquitectónico

Este repositorio contiene la implementación interactiva del clásico **Juego del Ahorcado**, desarrollado como parte de las actividades de aprendizaje autónomo para la asignatura de **Lógica de Programación** en la Universidad Internacional del Ecuador (UIDE).

El proyecto demuestra la transferencia práctica de conceptos de ingeniería de software, transitando desde el modelado abstracto (diagramas de casos de uso y arquitectura) hasta la codificación estructurada y modularizada en **Python 3**.

---

## 📋 Estructura del Proyecto

Para cumplir con el principio de **separación de responsabilidades** (Separation of Concerns), el software se encuentra desacoplado en componentes independientes:

* `main.py`: **Capa de Presentación y Control.** Centraliza el bucle principal de ejecución (`while`), gestiona las entradas/salidas por consola e implementa las estructuras condicionales para evaluar las reglas del juego.
* `palabras.py`: **Capa de Datos (Modelo).** Abstrae y administra el almacenamiento del diccionario de términos y expone la lógica pseudoaleatoria para seleccionar la palabra oculta.
* `/docs`: Carpeta que almacena la documentación de diseño previo (diagramas UML de casos de uso y diagramas de bloques arquitectónicos).

---

## 🛠️ Requisitos del Entorno

Para ejecutar esta aplicación, asegúrate de contar con los siguientes elementos configurados en tu entorno local:

1.  **Lenguaje de Programación:** [Python 3.10](https://www.python.org/) o superior.
2.  **Entorno de Desarrollo (IDE):** VS Code, PyCharm o la terminal del sistema.
3.  **Control de Versiones:** Git configurado y enlazado a tu cuenta de GitHub.

---

## 🚀 Instrucciones de Ejecución

Sigue estos pasos para clonar el repositorio y ejecutar el juego en tu máquina local:

### 1. Clonar el Repositorio
Abre tu terminal o símbolo del sistema y ejecuta el siguiente comando:
```bash
git clone [https://github.com/TU_USUARIO_DE_GITHUB/ahorcado-game-python.git](https://github.com/TU_USUARIO_DE_GITHUB/ahorcado-game-python.git)
