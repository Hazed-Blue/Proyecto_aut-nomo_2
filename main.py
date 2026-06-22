
from palabras import obtener_palabra_aleatoria
import logica_juego as lj  # Importamos la capa de negocio

def mostrar_pantalla(tablero, vidas, letras_intentadas):
    """Componente puro de Presentación."""
    print("\n" + "="*40)
    print(f" Palabra a adivinar:  {' '.join(tablero)}")
    print(f" Vidas restantes:     {vidas}")
    print(f" Letras intentadas:   {', '.join(letras_intentadas)}")
    print("="*40)

def ejecutar_partida():
    # Inicialización de datos usando la capa de negocio
    palabra_secreta = obtener_palabra_aleatoria()
    tablero = lj.inicializar_tablero(palabra_secreta)
    vidas = 6
    letras_intentadas = []
    
    print("--- ¡BIENVENIDO AL JUEGO DEL AHORCADO MODULARIZADO! ---")
    
    estado = "JUGANDO"
    
    # Bucle principal controlado por la lógica de negocio
    while estado == "JUGANDO":
        mostrar_pantalla(tablero, vidas, letras_intentadas)
        letra_ingresada = input("Introduce una letra: ")
        
        # 1. Validar la entrada (Capa de Negocio)
        validacion = lj.validar_entrada(letra_ingresada, letras_intentadas)
        if not validacion["valido"]:
            print(f"⚠️  {validacion['motivo']}")
            continue
            
        # Registrar el intento
        letra_limpia = letra_ingresada.upper().strip()
        letras_intentadas.append(letra_limpia)
        
        # 2. Procesar el intento (Capa de Negocio)
        es_correcto = lj.procesar_intento(letra_limpia, palabra_secreta, tablero)
        
        if es_correcto:
            print(f"¡Buen trabajo! La letra '{letra_limpia}' es correcta.")
        else:
            print(f"¡Oh no! La letra '{letra_limpia}' no se encuentra.")
            vidas -= 1
            
        # 3. Actualizar y evaluar estado terminal (Capa de Negocio)
        estado = lj.comprobar_estado_terminal(tablero, vidas)
        
    # Salida del bucle: Fin de la partida
    if estado == "VICTORIA":
        print(f"\n🎉 ¡FELICIDADES! Has ganado. La palabra era: {palabra_secreta}")
    else:
        print(f"\n💀 GAME OVER. Te has quedado sin vidas. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    ejecutar_partida()
