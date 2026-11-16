"""Clase Tablero."""
import random
import numpy as np
from variables import (TAMANO_TABLERO, BARCOS, DIRECCIONES, AGUA, AGUA_DISPARADA,
                       BARCO, TOCADO, RES_TOCADO, RES_AGUA, RES_REPETIDO)


class Tablero:
    """Tablero de un jugador con sus barcos y los disparos recibidos."""

    def __init__(self, id_jugador, tamano=TAMANO_TABLERO, barcos=BARCOS):
        self.id_jugador = id_jugador
        self.tamano = tamano
        self.barcos = barcos
        # tablero: barcos + disparos recibidos (lo ve su dueño)
        self.tablero = np.full((tamano, tamano), AGUA)
        # disparos: solo disparos recibidos (lo ve el rival)
        self.disparos = np.full((tamano, tamano), AGUA)

    def _casillas_libres(self, casillas):
        """Devuelve True si todas las casillas están dentro del tablero y sin barco."""
        for fila, col in casillas:
            if not (0 <= fila < self.tamano and 0 <= col < self.tamano):
                return False
            if self.tablero[fila, col] != AGUA:
                return False
        return True

    def colocar_barcos(self):
        """Coloca todos los barcos al azar, enteros dentro del tablero y sin solaparse."""
        for eslora in self.barcos.values():
            colocado = False
            while not colocado:
                fila = random.randint(0, self.tamano - 1)
                col = random.randint(0, self.tamano - 1)
                d_fila, d_col = DIRECCIONES[random.choice(list(DIRECCIONES))]
                casillas = [(fila + d_fila * i, col + d_col * i) for i in range(eslora)]
                if self._casillas_libres(casillas):
                    for f, c in casillas:
                        self.tablero[f, c] = BARCO
                    colocado = True

    def recibir_disparo(self, fila, columna):
        """Marca el disparo en los dos arrays y devuelve tocado, agua o repetido."""
        if self.disparos[fila, columna] != AGUA:
            return RES_REPETIDO
        if self.tablero[fila, columna] == BARCO:
            self.tablero[fila, columna] = TOCADO
            self.disparos[fila, columna] = TOCADO
            return RES_TOCADO
        self.tablero[fila, columna] = AGUA_DISPARADA
        self.disparos[fila, columna] = AGUA_DISPARADA
        return RES_AGUA

    def quedan_barcos(self):
        """True si todavía hay alguna casilla de barco sin tocar."""
        return bool((self.tablero == BARCO).any())

    def mostrar(self, ocultar_barcos=False):
        """Imprime el tablero. Con ocultar_barcos=True solo enseña los disparos."""
        matriz = self.disparos if ocultar_barcos else self.tablero
        print("   " + " ".join(str(i) for i in range(self.tamano)))
        for i, fila in enumerate(matriz):
            print(f"{i:>2} " + " ".join(fila))
