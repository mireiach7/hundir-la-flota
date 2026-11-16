"""Hundir la flota en terminal. Se ejecuta con: python main.py"""
from clases import Tablero
from funciones import mostrar_instrucciones, pedir_coordenadas, elegir_disparo_maquina
from variables import RES_TOCADO


def main():
    mostrar_instrucciones()

    jugador = Tablero("jugador")
    maquina = Tablero("maquina")
    jugador.colocar_barcos()
    maquina.colocar_barcos()

    while True:
        # --- Turno del jugador ---
        turno_jugador = True
        while turno_jugador:
            print("\nTU TABLERO:")
            jugador.mostrar()
            print("\nTABLERO DE LA MÁQUINA:")
            maquina.mostrar(ocultar_barcos=True)

            coordenadas = pedir_coordenadas(maquina)
            if coordenadas is None:
                print("Has salido de la partida.")
                return
            resultado = maquina.recibir_disparo(*coordenadas)

            if resultado == RES_TOCADO:
                print("¡Tocado! Vuelves a disparar.")
                if not maquina.quedan_barcos():
                    print("\n¡Has ganado! Has hundido toda la flota enemiga.")
                    return
            else:
                print("Agua.")
                turno_jugador = False

        # --- Turno de la máquina ---
        turno_maquina = True
        while turno_maquina:
            fila, columna = elegir_disparo_maquina(jugador)
            resultado = jugador.recibir_disparo(fila, columna)
            print(f"La máquina dispara a ({fila},{columna}): {resultado}")

            if resultado == RES_TOCADO:
                if not jugador.quedan_barcos():
                    print("\nHas perdido. La máquina ha hundido tu flota.")
                    return
            else:
                turno_maquina = False


if __name__ == "__main__":
    main()
