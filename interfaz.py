"""Interfaz gráfica (tkinter) de Hundir la flota. Se ejecuta con: python interfaz.py"""
import tkinter as tk
from clases import Tablero
from funciones import elegir_disparo_maquina
from variables import (TAMANO_TABLERO, AGUA, AGUA_DISPARADA, BARCO, TOCADO,
                       RES_TOCADO, RES_REPETIDO)

COLORES = {AGUA: "#4a90d9", AGUA_DISPARADA: "#b0b8c0", BARCO: "#3c9a5f", TOCADO: "#d9453d"}
PAUSA_MAQUINA = 700  # milisegundos


class Juego(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hundir la flota")
        self.jugador = Tablero("jugador")
        self.maquina = Tablero("maquina")
        self.jugador.colocar_barcos()
        self.maquina.colocar_barcos()
        self.turno_jugador = True

        self.mensaje = tk.Label(self, text="Tu turno: dispara en el tablero de la máquina",
                                font=("Arial", 12))
        self.mensaje.grid(row=0, column=0, columnspan=2, pady=8)

        tk.Label(self, text="Tu tablero").grid(row=1, column=0)
        tk.Label(self, text="Tablero de la máquina").grid(row=1, column=1)
        self.botones_jugador = self._crear_rejilla(0, clicable=False)
        self.botones_maquina = self._crear_rejilla(1, clicable=True)
        self.refrescar()

    def _crear_rejilla(self, columna_marco, clicable):
        """Crea una rejilla de botones y devuelve la lista de listas."""
        marco = tk.Frame(self, padx=10, pady=10)
        marco.grid(row=2, column=columna_marco)
        botones = []
        for f in range(TAMANO_TABLERO):
            fila = []
            for c in range(TAMANO_TABLERO):
                boton = tk.Button(marco, width=3, height=1, relief="raised")
                if clicable:
                    boton.config(command=lambda f=f, c=c: self.disparar(f, c))
                boton.grid(row=f, column=c)
                fila.append(boton)
            botones.append(fila)
        return botones

    def refrescar(self):
        """Pinta los dos tableros según el estado de los arrays."""
        for f in range(TAMANO_TABLERO):
            for c in range(TAMANO_TABLERO):
                self.botones_jugador[f][c].config(
                    bg=COLORES[self.jugador.tablero[f, c]], state="disabled")
                self.botones_maquina[f][c].config(
                    bg=COLORES[self.maquina.disparos[f, c]])

    def disparar(self, fila, columna):
        """El jugador hace clic en una casilla del tablero de la máquina."""
        if not self.turno_jugador:
            return
        resultado = self.maquina.recibir_disparo(fila, columna)
        if resultado == RES_REPETIDO:
            self.mensaje.config(text="Ya habías disparado ahí. Elige otra casilla.")
            return
        self.refrescar()
        if not self.maquina.quedan_barcos():
            self.terminar("¡Has ganado!")
        elif resultado == RES_TOCADO:
            self.mensaje.config(text="¡Tocado! Vuelve a disparar.")
        else:
            self.mensaje.config(text="Agua. Turno de la máquina...")
            self.turno_jugador = False
            self.after(PAUSA_MAQUINA, self.turno_de_la_maquina)

    def turno_de_la_maquina(self):
        fila, columna = elegir_disparo_maquina(self.jugador)
        resultado = self.jugador.recibir_disparo(fila, columna)
        self.refrescar()
        if not self.jugador.quedan_barcos():
            self.terminar("Has perdido.")
        elif resultado == RES_TOCADO:
            self.mensaje.config(text=f"La máquina toca en ({fila},{columna}) y sigue...")
            self.after(PAUSA_MAQUINA, self.turno_de_la_maquina)
        else:
            self.mensaje.config(text=f"La máquina falla en ({fila},{columna}). ¡Tu turno!")
            self.turno_jugador = True

    def terminar(self, texto):
        self.turno_jugador = False
        self.mensaje.config(text=texto + " Cierra la ventana para salir.")


if __name__ == "__main__":
    Juego().mainloop()
