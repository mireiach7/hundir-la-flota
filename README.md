# Hundir la flota

Juego de Hundir la flota contra la máquina, hecho en Python con NumPy.

## Instalación
```
pip install -r requirements.txt
```

## Ejecución
- Terminal: `python main.py`
- Interfaz gráfica (tkinter): `python interfaz.py`

## Cómo se juega
Tablero 10x10 (filas y columnas de 0 a 9). Empiezas tú. Si aciertas, repites turno;
si fallas, dispara la máquina. Gana quien hunda antes los 20 casillas de barco del rival.
En terminal escribe `fila,columna` (ej. `3,4`) o `salir`.

## Símbolos
| Símbolo | Significado |
|---|---|
| `~` | Agua sin disparar |
| `o` | Agua disparada |
| `B` | Barco sin tocar |
| `X` | Barco tocado |

En la interfaz gráfica: azul = agua, gris = agua disparada, verde = tu barco, rojo = tocado.

## Estructura
`main.py`, `clases.py` (Tablero), `funciones.py`, `variables.py`, `interfaz.py` (extra).
