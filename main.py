from clases import Tablero
import funciones
import variables

funciones.imprimir_instrucciones()

# Creamos los dos tableros y colocamos los barcos (solo una vez)
jugador = Tablero("jugador")
maquina = Tablero("maquina")
jugador.colocar_barcos()
maquina.colocar_barcos()

while True:
    # Turno del jugador
    while True:
        print("\nTu tablero:")
        jugador.mostrar()
        print("\nTablero de la maquina:")
        maquina.mostrar(ocultar_barcos=True)

        fila, columna = funciones.pedir_coordenadas()
        resultado = maquina.recibir_disparo(fila, columna)

        if resultado == "repetido":
            print(variables.MENSAJE_REPETIDO)
            continue
        elif resultado == "tocado":
            print("Tocado! Vuelves a disparar.")
            if not maquina.quedan_barcos():
                break
        else:
            print("Agua.")
            break

    if not maquina.quedan_barcos():
        print("\nHas ganado, enhorabuena!")
        break

    # Turno de la maquina 
    print("\nTurno de la maquina...")
    while True:
        fila, columna = funciones.disparo_maquina(jugador)
        resultado = jugador.recibir_disparo(fila, columna)
        print(f"La maquina dispara a {fila},{columna}: {resultado}")
        if resultado == "agua":
            break
        if not jugador.quedan_barcos():
            break

    if not jugador.quedan_barcos():
        print("\nLa maquina ha hundido toda tu flota. Has perdido.")
        break
