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
        self.tablero = np.full((tamano, tamano), AGUA)
        self.disparos = np.full((tamano, tamano), AGUA)

    def hay_sitio(self, casillas):
        """Devuelve True si todas las casillas están dentro y libres."""
        for fila, col in casillas:
            if fila < 0 or fila >= self.tamano or col < 0 or col >= self.tamano:
                return False
            if self.tablero[fila, col] != AGUA:
                return False
        return True

    def colocar_barcos(self):
        """Coloca todos los barcos al azar sin salirse ni pisarse."""
        for eslora in self.barcos.values():
            colocado = False
            while not colocado:
                fila = random.randint(0, self.tamano - 1)
                col = random.randint(0, self.tamano - 1)
                orientacion = random.choice(list(DIRECCIONES))
                cambio_fila, cambio_col = DIRECCIONES[orientacion]
                casillas = []
                for i in range(eslora):
                    casillas.append((fila + cambio_fila * i, col + cambio_col * i))
                if self.hay_sitio(casillas):
                    for f, c in casillas:
                        self.tablero[f, c] = BARCO
                    colocado = True

    def recibir_disparo(self, fila, columna):
        """Marca el disparo y devuelve tocado, agua o repetido."""
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
        """Devuelve True si queda alguna casilla de barco sin tocar."""
        return BARCO in self.tablero

    def mostrar(self, ocultar_barcos=False):
        """Imprime el tablero, sin barcos si ocultar_barcos es True."""
        if ocultar_barcos:
            matriz = self.disparos
        else:
            matriz = self.tablero
        print("   " + " ".join(str(i) for i in range(self.tamano)))
        for i in range(self.tamano):
            print(f"{i:>2} " + " ".join(matriz[i]))
