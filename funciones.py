"""Funciones auxiliares del juego."""
import random
import numpy as np
from variables import (TAMANO_TABLERO, AGUA, MSG_BIENVENIDA, MSG_INSTRUCCIONES,
                       MSG_ENTRADA_INVALIDA, MSG_REPETIDO)


def mostrar_instrucciones():
    """Imprime la bienvenida y las reglas."""
    print(MSG_BIENVENIDA)
    print(MSG_INSTRUCCIONES)


def pedir_coordenadas(tablero_rival):
    """Pide fila y columna hasta que sean válidas y no repetidas.

    Devuelve (fila, columna) o None si el jugador escribe 'salir'.
    """
    while True:
        texto = input("Tu disparo (fila,columna): ").strip().lower()
        if texto == "salir":
            return None
        partes = texto.replace(",", " ").split()
        try:
            if len(partes) != 2:
                raise ValueError
            fila, columna = int(partes[0]), int(partes[1])
        except ValueError:
            print(MSG_ENTRADA_INVALIDA)
            continue
        if not (0 <= fila < TAMANO_TABLERO and 0 <= columna < TAMANO_TABLERO):
            print(MSG_ENTRADA_INVALIDA)
            continue
        if tablero_rival.disparos[fila, columna] != AGUA:
            print(MSG_REPETIDO)
            continue
        return fila, columna


def elegir_disparo_maquina(tablero_jugador):
    """Elige una casilla aleatoria a la que todavía no se ha disparado."""
    sin_disparar = np.argwhere(tablero_jugador.disparos == AGUA)
    fila, columna = random.choice(sin_disparar)
    return int(fila), int(columna)
