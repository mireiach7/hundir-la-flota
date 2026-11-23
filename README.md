# Hundir la flota

Versión de Hundir la flota en Python para jugar contra la máquina desde el terminal.

Este proyecto lo he realizado de forma **individual**, por lo que no puedo exponerlo en una presentación en grupo. Por eso, además de cómo se instala y se juega, explico aquí cómo lo he hecho. He usado IA como apoyo y lo he registrado en `AI_LOG.md`.

## Instalación

```
pip install -r requirements.txt
```

## Cómo ejecutarlo

```
python main.py
```

## Cómo se juega

- Cada jugador tiene un tablero de 10x10 con 10 barcos colocados al azar (20 casillas con barco).
- Empiezas tú. Escribe la coordenada como `fila,columna` (de 0 a 9), por ejemplo `3,5`.
- Si aciertas, vuelves a disparar. Si fallas, dispara la máquina (y sigue mientras acierte).
- Gana quien hunda todos los barcos del rival.
- Si repites un disparo o escribes algo mal, el programa te avisa y te vuelve a pedir la coordenada.

## Símbolos del tablero

| Símbolo | Significado |
|---|---|
| `.` | Agua sin disparar |
| `o` | Agua donde se ha disparado |
| `B` | Barco sin tocar |
| `X` | Barco tocado |

## Archivos

- `main.py`: ejecuta la partida
- `clases.py`: clase `Tablero`
- `funciones.py`: funciones auxiliares
- `variables.py`: constantes

## Cómo lo he hecho

### `variables.py`
Aquí guardo todo lo que no cambia durante la partida: el tamaño del tablero, el diccionario de barcos con su eslora, las orientaciones (N, S, E, O), los símbolos y los mensajes. Así ningún otro archivo tiene un `10` escrito a mano.

### `clases.py`
Contiene la clase `Tablero`. Cada jugador (yo y la máquina) tiene un objeto `Tablero` con dos arrays de NumPy de 10x10:

- `tablero`: los barcos y los disparos recibidos. Es lo que veo de mi propio tablero.
- `disparos`: solo los disparos recibidos, sin barcos. Es lo que veo del tablero de la máquina, para no descubrir dónde tiene sus barcos.

También guarda `vidas`, que empieza en 20 y baja con cada acierto, así no hace falta una clase `Barco`. Sus métodos son:

- `colocar_barcos()`: para cada barco elige una casilla y una orientación al azar, comprueba que cabe dentro del tablero y que no pisa a otro barco, y si no es válido prueba otra vez.
- `recibir_disparo(fila, columna)`: devuelve `"tocado"`, `"agua"` o `"repetido"` y marca el resultado en los dos arrays.
- `mostrar(ocultar_barcos=False)`: imprime el tablero. Con `ocultar_barcos=True` enseña solo los disparos.
- `quedan_barcos()`: devuelve `True` mientras queden vidas.

### `funciones.py`
- `imprimir_instrucciones()`: muestra la bienvenida y los símbolos.
- `pedir_coordenadas()`: pide `fila,columna` en un bucle y valida la entrada con `try/except`. Si no es válida, avisa y vuelve a pedirla.
- `disparo_maquina()`: elige casillas al azar hasta encontrar una a la que no se haya disparado, por eso la máquina nunca repite.

### `main.py`
Crea los dos tableros, coloca los barcos una sola vez y entra en un bucle `while True` con dos partes: mi turno y el de la máquina. Si acierto o acierta la máquina, se repite el turno. Con `break` se sale del bucle cuando a alguien no le quedan barcos y se anuncia el ganador.

### Conceptos usados
NumPy (los tableros son arrays), clases, funciones y módulos, bucles y condicionales (`while`, `for`, `if`, `break`, `continue`), diccionarios y `try/except`.

## Uso de IA

He usado Claude como apoyo en este proyecto. El detalle por módulo y por prompt está en `AI_LOG.md`.
