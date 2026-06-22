
"""
Capa de Negocio (Controlador / Reglas del Juego).
Este módulo contiene exclusivamente las funciones matemáticas y lógicas
que controlan los estados del juego, validan letras y actualizan el tablero.
No contiene 'print()' ni 'input()', garantizando el desacoplamiento total.
"""

def inicializar_tablero(palabra_secreta):
    """
    Crea el estado inicial del tablero oculto.
    Retorna una lista de guiones bajos equivalente a la longitud de la palabra.
    """
    return ["_"] * len(palabra_secreta)


def validar_entrada(letra, letras_intentadas):
    """
    Evalúa si la entrada del usuario cumple con las restricciones lógicas.
    Retorna un diccionario con el estado de la validación y un mensaje de error si aplica.
    """
    letra = letra.upper().strip()
    
    if len(letra) != 1 or not letra.isalpha():
        return {"valido": False, "motivo": "Por favor, ingresa únicamente una sola letra alfabética."}
        
    if letra in letras_intentadas:
        return {"valido": False, "motivo": f"Ya habías intentado la letra '{letra}'. Prueba con otra."}
        
    return {"valido": True, "motivo": "Letra válida."}


def procesar_intento(letra, palabra_secreta, tablero_actual):
    """
    Ejecuta la verificación condicional del carácter dentro de la palabra objetivo.
    Modifica el tablero de forma indexada si hay coincidencias.
    Retorna True si la letra fue correcta, False en caso contrario.
    """
    letra = letra.upper().strip()
    acierto = False
    
    # Estructura repetitiva para buscar coincidencias indexadas
    for posicion, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            tablero_actual[posicion] = letra
            acierto = True
            
    return acierto

def comprobar_estado_terminal(tablero, vidas):
    """
    Analiza las variables de control para verificar si el juego ha terminado.
    Retorna:
        - "VICTORIA" si no quedan guiones bajos.
        - "DERROTA" si las vidas llegaron a 0.
        - "JUGANDO" si la partida debe continuar.
    """
    if "_" not in tablero:
        return "VICTORIA"
    elif vidas <= 0:
        return "DERROTA"
    else:
        return "JUGANDO"
