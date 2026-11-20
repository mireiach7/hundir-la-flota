TAMANO_TABLERO = 10

BARCOS = {
    "lancha 1": 1,
    "lancha 2": 1,
    "lancha 3": 1,
    "lancha 4": 1,
    "crucero 1": 2,
    "crucero 2": 2,
    "crucero 3": 2,
    "acorazado 1": 3,
    "acorazado 2": 3,
    "portaaviones": 4,
}

DIRECCIONES = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}

AGUA = "~"
AGUA_DISPARADA = "o"
BARCO = "B"
TOCADO = "X"

RES_TOCADO = "tocado"
RES_AGUA = "agua"
RES_REPETIDO = "repetido"

MSG_BIENVENIDA = "=== HUNDIR LA FLOTA ==="
MSG_INSTRUCCIONES = (
    "Disparas escribiendo fila,columna (de 0 a 9). Ejemplo: 3,4\n"
    "Si aciertas, vuelves a disparar. Si fallas, dispara la máquina.\n"
    "Gana quien hunda antes todos los barcos del rival.\n"
    "Escribe 'salir' para terminar.\n"
    "Símbolos: ~ agua | o agua disparada | B barco | X tocado\n"
)
MSG_ENTRADA_INVALIDA = "Entrada no válida. Escribe fila,columna entre 0 y 9. Ejemplo: 3,4"
MSG_REPETIDO = "Ya habías disparado ahí. Prueba otra casilla."
MSG_GANAS = "¡Has ganado!"
MSG_PIERDES = "Has perdido. La máquina ha hundido tu flota."
