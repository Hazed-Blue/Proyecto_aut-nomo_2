# palabras.py
import random

def obtener_palabra_aleatoria():
    """
    Componente de la Capa de Datos.
    Administra y retorna un término seleccionado al azar.
    """
    banco_palabras = ["ALGORITMO", "PYTHON", "INGENIERIA", "SOFTWARE", "DIAGRAMA", "VARIABLE"]
    return random.choice(banco_palabras)
