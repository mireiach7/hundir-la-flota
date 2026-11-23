import random
import variables


def imprimir_instrucciones():
    print(variables.MENSAJE_BIENVENIDA)
    print("Juegas contra la maquina. Cada uno tiene un tablero de 10x10.")
    print("Escribe las coordenadas como fila,columna (de 0 a 9). Ejemplo: 3,5")
    print("Si aciertas, vuelves a disparar. Si fallas, dispara la maquina.")
    print("Simbolos:")
    print(f"  {variables.AGUA} agua sin disparar")
    print(f"  {variables.AGUA_DISPARADA} agua donde se ha disparado")
    print(f"  {variables.BARCO} barco sin tocar")
    print(f"  {variables.TOCADO} barco tocado")
    print()


def pedir_coordenadas():
    while True:
        texto = input("Tu disparo (fila,columna): ")
        try:
            partes = texto.split(",")
            if len(partes) != 2:
                raise ValueError
            fila = int(partes[0])
            columna = int(partes[1])
            if fila < 0 or fila >= variables.TAMANO_TABLERO:
                raise ValueError
            if columna < 0 or columna >= variables.TAMANO_TABLERO:
                raise ValueError
            return fila, columna
        except ValueError:
            print(variables.MENSAJE_ERROR)
            continue


def disparo_maquina(tablero_jugador):
    while True:
        fila = random.randint(0, variables.TAMANO_TABLERO - 1)
        columna = random.randint(0, variables.TAMANO_TABLERO - 1)
        if tablero_jugador.disparos[fila, columna] == variables.AGUA:
            return fila, columna
