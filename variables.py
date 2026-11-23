TAMANO_TABLERO = 10

BARCOS = {
    "Lancha 1": 1,
    "Lancha 2": 1,
    "Lancha 3": 1,
    "Lancha 4": 1,
    "Crucero 1": 2,
    "Crucero 2": 2,
    "Crucero 3": 2,
    "Acorazado 1": 3,
    "Acorazado 2": 3,
    "Portaaviones": 4,
}

ORIENTACIONES = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "O": (0, -1),
}

AGUA = "."          # agua sin disparar
AGUA_DISPARADA = "o"  # agua donde se ha disparado
BARCO = "B"         # barco sin tocar
TOCADO = "X"        # barco tocado

MENSAJE_BIENVENIDA = "HUNDIR LA FLOTA"
MENSAJE_ERROR = "Entrada no valida. Escribe fila y columna entre 0 y 9, por ejemplo: 3,5"
MENSAJE_REPETIDO = "Ya has disparado ahi, prueba otra casilla."
