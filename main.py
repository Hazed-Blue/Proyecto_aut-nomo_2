
from palabras import obtener_palabra_aleatoria

def inicializar_tablero(palabra):
    """Inicializa el estado visual con guiones bajos."""
    return ["_"] * len(palabra)

def mostrar_estado(tablero, vidas, letras_intentadas):
    """Componente de la Capa de Presentación: Muestra el estado actual en consola."""
    print("\n" + "="*30)
    print(f"Palabra a adivinar: {' '.join(tablero)}")
    print(f"Vidas restantes: {vidas}")
    print(f"Letras intentadas: {', '.join(letras_intentadas)}")
    print("="*30)

def jugar_ahorcado():
    # --- Inicialización de variables de estado ---
    palabra_secreta = obtener_palabra_aleatoria()
    tablero = inicializar_tablero(palabra_secreta)
    vidas = 6
    letras_intentadas = []
    
    print("¡Bienvenido al Juego del Ahorcado!")
    
    # --- Estructura Repetitiva Principal (Bucle Controlado por Estado) ---
    while vidas > 0 and "_" in tablero:
        mostrar_estado(tablero, vidas, letras_intentadas)
        
        # Captura de entrada del usuario
        letra = input("Ingresa una letra: ").upper().strip()
        
        # Validaciones de control de entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Error: Por favor, ingresa únicamente una sola letra.")
            continue
            
        if letra in letras_intentadas:
            print(f"Ya habías intentado la letra '{letra}'. Prueba con otra.")
            continue
            
        letras_intentadas.append(letra)
        
        # --- Estructura Condicional: Verificación Lógica del Carácter ---
        if letra in palabra_secreta:
            print(f"¡Excelente! La letra '{letra}' es correcta.")
            # Actualización indexada de la palabra
            for posicion, caracter in enumerate(palabra_secreta):
                if caracter == letra:
                    tablero[posicion] = letra
        else:
            print(f"Incorrecto. La letra '{letra}' no está en la palabra.")
            vidas -= 1  # Decremento lineal de recursos (vidas)

    # --- Evaluación de Estados Terminales ---
    if "_" not in tablero:
        print(f"\n¡Felicidades! Ganaste. La palabra era: {palabra_secreta}")
    else:
        print(f"\nGame Over. Te has quedado sin vidas. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()
