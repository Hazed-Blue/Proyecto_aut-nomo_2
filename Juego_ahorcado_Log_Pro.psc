// ===================================================================
// CAPA DE DATOS
// ===================================================================
Funcion palabra <- SeleccionarPalabraAleatoria
    Definir banco Como Caracter;
    Definir palabra Como Caracter;
    Dimension banco[6];
    
    banco[1] <- "ALGORITMO";
    banco[2] <- "PYTHON";
    banco[3] <- "INGENIERIA";
    banco[4] <- "SOFTWARE";
    banco[5] <- "DIAGRAMA";
    banco[6] <- "VARIABLE";
    
    palabra <- banco[Azar(6) + 1];
FinFuncion

// ===================================================================
// CAPA DE PRESENTACIÓN
// ===================================================================
Funcion MostrarTablero(tablero, tamano, intentos, usadas)
    Definir i Como Entero;
    Borrar Pantalla;
    Escribir "=========================================";
    Escribir "           JUEGO DEL AHORCADO            ";
    Escribir "=========================================";
    Escribir "";
    
    Escribir "Palabra: ";
    Para i <- 1 Hasta tamano Con Paso 1 Hacer
        Escribir Sin Saltar Subcadena(tablero, i, i), " ";
    FinPara
    Escribir "";
    Escribir "";
    
    Escribir "Intentos restantes: ", intentos;
    Escribir "Letras usadas: ", usadas;
    Escribir "-----------------------------------------";
FinFuncion

// ===================================================================
// CAPA DE LÓGICA DE NEGOCIO (MOTOR PRINCIPAL)
// ===================================================================
Algoritmo JuegoDelAhorcado
    // TODAS LAS DEFINICIONES DEBEN IR AQUÍ AL INICIO (FUERA DEL MIENTRAS)
    Definir jugarNuevamente Como Caracter;
    Definir palabraSecreta, tablero, letrasUsadas, letraIngresada Como Caracter;
    Definir longPalabra, intentos, i Como Entero;
    Definir acierto, letraRepetida, palabraCompletada Como Logico;
    
    jugarNuevamente <- "SI";
    
    Mientras jugarNuevamente = "SI" O jugarNuevamente = "S" Hacer
        
        // --- Reinicio y Asignación de variables en cada partida ---
        palabraSecreta <- SeleccionarPalabraAleatoria;
        longPalabra <- Longitud(palabraSecreta);
        intentos <- 6;
        letrasUsadas <- "";
        palabraCompletada <- Falso;
        
        tablero <- "";
        Para i <- 1 Hasta longPalabra Con Paso 1 Hacer
            tablero <- tablero + "_";
        FinPara
        
        Mientras intentos > 0 Y palabraCompletada = Falso Hacer
            
            MostrarTablero(tablero, longPalabra, intentos, letrasUsadas);
            
            Escribir "Introduce una letra: ";
            Leer letraIngresada;
            letraIngresada <- Mayusculas(letraIngresada);
            
            Si Longitud(letraIngresada) <> 1 Entonces
                Escribir "Error: Ingresa solo un caracter. Presione Enter.";
                Esperar Tecla;
            Sino
                letraRepetida <- Falso;
                Para i <- 1 Hasta Longitud(letrasUsadas) Con Paso 1 Hacer
                    Si Subcadena(letrasUsadas, i, i) = letraIngresada Entonces
                        letraRepetida <- Verdadero;
                    FinSi
                FinPara
                
                Si letraRepetida = Verdadero Entonces
                    Escribir "¡Esa letra ya la usaste! Intenta con otra. (Presione Enter)";
                    Esperar Tecla;
                Sino
                    letrasUsadas <- letrasUsadas + letraIngresada + " ";
                    
                    acierto <- Falso;
                    Para i <- 1 Hasta longPalabra Con Paso 1 Hacer
                        Si Subcadena(palabraSecreta, i, i) = letraIngresada Entonces
                            tablero <- Subcadena(tablero, 1, i-1) + letraIngresada + Subcadena(tablero, i+1, longPalabra);
                            acierto <- Verdadero;
                        FinSi
                    FinPara
                    
                    Si acierto = Falso Entonces
                        intentos <- intentos - 1;
                        Escribir "La letra no se encuentra en la palabra. (Presione Enter)";
                        Esperar Tecla;
                    FinSi
                FinSi
            FinSi
            
            palabraCompletada <- Verdadero;
            Para i <- 1 Hasta longPalabra Con Paso 1 Hacer
                Si Subcadena(tablero, i, i) = "_" Entonces
                    palabraCompletada <- Falso;
                FinSi
            FinPara
            
        FinMientras
        
        Borrar Pantalla;
        Si palabraCompletada = Verdadero Entonces
            Escribir "¡¡VICTORIA!! Has adivinado la palabra: ", palabraSecreta;
        Sino
            Escribir "¡¡DERROTA!! Te has quedado sin intentos.";
            Escribir "La palabra correcta era: ", palabraSecreta;
        FinSi
        Escribir "";
        
        Escribir "¿Deseas jugar de nuevo? (SI/NO): ";
        Leer jugarNuevamente;
        jugarNuevamente <- Mayusculas(jugarNuevamente);
        
    FinMientras
    
    Escribir "Fin del juego. ¡Gracias por participar!";
FinAlgoritmo