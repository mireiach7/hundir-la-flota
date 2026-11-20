# Hundir la flota

Juego de Hundir la flota contra la máquina, hecho en Python con NumPy.

## Instalación
```
pip install -r requirements.txt
```

## Ejecución
En el terminal:
```
python main.py
```
Con ventana (tkinter):
```
python interfaz.py
```

## Cómo se juega
Tablero de 10x10 (filas y columnas de 0 a 9). Empiezas tú. Escribe `fila,columna`
(por ejemplo `3,4`). Si aciertas, repites turno; si fallas, dispara la máquina.
Gana quien hunda antes las 20 casillas de barco del rival. Escribe `salir` para terminar.

## Símbolos
| Símbolo | Significado |
|---|---|
| `~` | Agua sin disparar |
| `o` | Agua donde se ha disparado |
| `B` | Barco sin tocar |
| `X` | Barco tocado |

## Archivos
- `main.py`: ejecuta la partida
- `clases.py`: clase Tablero
- `funciones.py`: funciones auxiliares
- `variables.py`: constantes
- `interfaz.py`: versión con ventana

En la ventana: azul = agua, gris = agua disparada, verde = tu barco, rojo = tocado. Haz clic en el tablero de la derecha para disparar.
