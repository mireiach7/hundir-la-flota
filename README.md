# Hundir la flota

Version de Hundir la flota en Python para jugar contra la maquina desde el terminal.

## Instalacion

```
pip install -r requirements.txt
```

## Como ejecutarlo

```
python main.py
```

## Como se juega

- Cada jugador tiene un tablero de 10x10 con 10 barcos colocados al azar (20 casillas con barco).
- Empiezas tu. Escribe la coordenada como `fila,columna` (de 0 a 9), por ejemplo `3,5`.
- Si aciertas, vuelves a disparar. Si fallas, dispara la maquina (y sigue mientras acierte).
- Gana quien hunda todos los barcos del rival.
- Si repites un disparo o escribes algo mal, el programa te avisa y te vuelve a pedir la coordenada.

## Simbolos del tablero

| Simbolo | Significado |
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
