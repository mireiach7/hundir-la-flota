import random
import numpy as np
import variables


class Tablero:

    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimension = variables.TAMANO_TABLERO
        self.barcos = variables.BARCOS
        self.tablero = np.full((self.dimension, self.dimension), variables.AGUA)
        self.disparos = np.full((self.dimension, self.dimension), variables.AGUA)
        self.vidas = sum(self.barcos.values())

    def colocar_barcos(self):
        for nombre, eslora in self.barcos.items():
            colocado = False
            while not colocado:
                fila = random.randint(0, self.dimension - 1)
                columna = random.randint(0, self.dimension - 1)
                orientacion = random.choice(list(variables.ORIENTACIONES))
                cambio_fila, cambio_columna = variables.ORIENTACIONES[orientacion]

                casillas = []
                for i in range(eslora):
                    casillas.append((fila + cambio_fila * i, columna + cambio_columna * i))

                valido = True
                for f, c in casillas:
                    if f < 0 or f >= self.dimension or c < 0 or c >= self.dimension:
                        valido = False
                    elif self.tablero[f, c] != variables.AGUA:
                        valido = False

                if valido:
                    for f, c in casillas:
                        self.tablero[f, c] = variables.BARCO
                    colocado = True

    def recibir_disparo(self, fila, columna):
        if self.disparos[fila, columna] != variables.AGUA:
            return "repetido"

        if self.tablero[fila, columna] == variables.BARCO:
            self.tablero[fila, columna] = variables.TOCADO
            self.disparos[fila, columna] = variables.TOCADO
            self.vidas -= 1
            return "tocado"

        self.tablero[fila, columna] = variables.AGUA_DISPARADA
        self.disparos[fila, columna] = variables.AGUA_DISPARADA
        return "agua"

    def mostrar(self, ocultar_barcos=False):
        if ocultar_barcos:
            matriz = self.disparos
        else:
            matriz = self.tablero

        print("   " + " ".join(str(i) for i in range(self.dimension)))
        for i in range(self.dimension):
            print(str(i).rjust(2) + " " + " ".join(matriz[i]))

    def quedan_barcos(self):
        return self.vidas > 0
