import random
from variables import (TAMANO_TABLERO, AGUA, MSG_BIENVENIDA, MSG_INSTRUCCIONES,
                       MSG_ENTRADA_INVALIDA, MSG_REPETIDO)


def mostrar_instrucciones():
    """Imprime la bienvenida y las reglas."""
    print(MSG_BIENVENIDA)
    print(MSG_INSTRUCCIONES)


def pedir_coordenadas(tablero_rival):
    """Pide fila y columna hasta que sean válidas. Devuelve None si escribe salir."""
    while True:
        texto = input("Tu disparo (fila,columna): ").strip().lower()
        if texto == "salir":
            return None
        partes = texto.replace(",", " ").split()
        if len(partes) != 2:
            print(MSG_ENTRADA_INVALIDA)
            continue
        try:
            fila = int(partes[0])
            columna = int(partes[1])
        except ValueError:
            print(MSG_ENTRADA_INVALIDA)
            continue
        if fila < 0 or fila >= TAMANO_TABLERO or columna < 0 or columna >= TAMANO_TABLERO:
            print(MSG_ENTRADA_INVALIDA)
            continue
        if tablero_rival.disparos[fila, columna] != AGUA:
            print(MSG_REPETIDO)
            continue
        return fila, columna


def elegir_disparo_maquina(tablero_jugador):
    """Elige una casilla al azar a la que aún no se ha disparado."""
    while True:
        fila = random.randint(0, TAMANO_TABLERO - 1)
        columna = random.randint(0, TAMANO_TABLERO - 1)
        if tablero_jugador.disparos[fila, columna] == AGUA:
            return fila, columna
