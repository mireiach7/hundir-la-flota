"""Constantes del juego Hundir la flota."""

TAMANO_TABLERO = 10

# Nombre de cada barco y su eslora
BARCOS = {
    "lancha 1": 1, "lancha 2": 1, "lancha 3": 1, "lancha 4": 1,
    "crucero 1": 2, "crucero 2": 2, "crucero 3": 2,
    "acorazado 1": 3, "acorazado 2": 3,
    "portaaviones": 4,
}

# Orientaciones: (cambio de fila, cambio de columna)
DIRECCIONES = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}

# Símbolos del tablero
AGUA = "~"              # agua sin disparar
AGUA_DISPARADA = "o"    # agua donde se ha disparado
BARCO = "B"             # barco sin tocar
TOCADO = "X"            # barco tocado

# Resultados de un disparo
RES_TOCADO = "tocado"
RES_AGUA = "agua"
RES_REPETIDO = "repetido"

# Mensajes
MSG_BIENVENIDA = "=== HUNDIR LA FLOTA ==="
MSG_INSTRUCCIONES = f"""
Reglas:
- Tablero de {TAMANO_TABLERO}x{TAMANO_TABLERO}. Filas y columnas van de 0 a {TAMANO_TABLERO - 1}.
- Disparas escribiendo fila y columna, por ejemplo: 3,4
- Si aciertas, vuelves a disparar. Si fallas, dispara la máquina.
- Gana quien hunda primero todos los barcos del rival.
- Escribe 'salir' para terminar la partida.

Símbolos:
  {AGUA} agua sin disparar    {AGUA_DISPARADA} agua disparada
  {BARCO} barco sin tocar     {TOCADO} barco tocado
"""
MSG_ENTRADA_INVALIDA = "Entrada no válida. Escribe fila y columna entre 0 y 9, por ejemplo 3,4"
MSG_REPETIDO = "Ya habías disparado a esa casilla. Prueba con otra."
