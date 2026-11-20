from clases import Tablero
from funciones import mostrar_instrucciones, pedir_coordenadas, elegir_disparo_maquina
from variables import RES_TOCADO, MSG_GANAS, MSG_PIERDES


def main():
    mostrar_instrucciones()

    jugador = Tablero("jugador")
    maquina = Tablero("maquina")
    jugador.colocar_barcos()
    maquina.colocar_barcos()

    mensaje_final = ""

    while True:
        turno_jugador = True
        while turno_jugador:
            print("\nTU TABLERO:")
            jugador.mostrar()
            print("\nTABLERO DE LA MÁQUINA:")
            maquina.mostrar(ocultar_barcos=True)

            coordenadas = pedir_coordenadas(maquina)
            if coordenadas is None:
                mensaje_final = "Has salido de la partida."
                break
            fila, columna = coordenadas
            resultado = maquina.recibir_disparo(fila, columna)

            if resultado == RES_TOCADO:
                print("¡Tocado!")
                if not maquina.quedan_barcos():
                    mensaje_final = MSG_GANAS
                    break
            else:
                print("Agua.")
                turno_jugador = False

        if mensaje_final:
            break

        turno_maquina = True
        while turno_maquina:
            fila, columna = elegir_disparo_maquina(jugador)
            resultado = jugador.recibir_disparo(fila, columna)
            print(f"La máquina dispara a ({fila},{columna}): {resultado}")

            if resultado == RES_TOCADO:
                if not jugador.quedan_barcos():
                    mensaje_final = MSG_PIERDES
                    break
            else:
                turno_maquina = False

        if mensaje_final:
            break

    print(mensaje_final)


if __name__ == "__main__":
    main()
