import tkinter as tk
from clases import Tablero
from funciones import elegir_disparo_maquina
from variables import TAMANO_TABLERO, AGUA, AGUA_DISPARADA, BARCO, TOCADO, RES_TOCADO, RES_REPETIDO

COLORES = {AGUA: "#4a90d9", AGUA_DISPARADA: "#b0b8c0", BARCO: "#3c9a5f", TOCADO: "#d9453d"}
PAUSA = 700


class Juego:
    """Ventana del juego con el tablero del jugador y el de la máquina."""

    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Hundir la flota")
        self.jugador = Tablero("jugador")
        self.maquina = Tablero("maquina")
        self.jugador.colocar_barcos()
        self.maquina.colocar_barcos()
        self.turno_jugador = True

        self.mensaje = tk.Label(ventana, text="Tu turno: dispara en el tablero de la máquina")
        self.mensaje.grid(row=0, column=0, columnspan=2, pady=8)
        tk.Label(ventana, text="Tu tablero").grid(row=1, column=0)
        tk.Label(ventana, text="Tablero de la máquina").grid(row=1, column=1)

        self.botones_jugador = self.crear_rejilla(0, False)
        self.botones_maquina = self.crear_rejilla(1, True)
        self.actualizar()

    def crear_rejilla(self, columna_marco, clicable):
        """Crea la rejilla de botones de un tablero."""
        marco = tk.Frame(self.ventana, padx=10, pady=10)
        marco.grid(row=2, column=columna_marco)
        botones = []
        for f in range(TAMANO_TABLERO):
            fila = []
            for c in range(TAMANO_TABLERO):
                boton = tk.Button(marco, width=3)
                if clicable:
                    boton.config(command=lambda f=f, c=c: self.disparar(f, c))
                boton.grid(row=f, column=c)
                fila.append(boton)
            botones.append(fila)
        return botones

    def actualizar(self):
        """Pinta los botones según el estado de los tableros."""
        for f in range(TAMANO_TABLERO):
            for c in range(TAMANO_TABLERO):
                self.botones_jugador[f][c].config(bg=COLORES[self.jugador.tablero[f, c]])
                self.botones_maquina[f][c].config(bg=COLORES[self.maquina.disparos[f, c]])

    def disparar(self, fila, columna):
        """Disparo del jugador al hacer clic en una casilla."""
        if not self.turno_jugador:
            return
        resultado = self.maquina.recibir_disparo(fila, columna)
        if resultado == RES_REPETIDO:
            self.mensaje.config(text="Ya habías disparado ahí. Elige otra casilla.")
            return
        self.actualizar()
        if not self.maquina.quedan_barcos():
            self.terminar("¡Has ganado!")
        elif resultado == RES_TOCADO:
            self.mensaje.config(text="¡Tocado! Vuelve a disparar.")
        else:
            self.mensaje.config(text="Agua. Turno de la máquina...")
            self.turno_jugador = False
            self.ventana.after(PAUSA, self.turno_maquina)

    def turno_maquina(self):
        """Disparo de la máquina."""
        fila, columna = elegir_disparo_maquina(self.jugador)
        resultado = self.jugador.recibir_disparo(fila, columna)
        self.actualizar()
        if not self.jugador.quedan_barcos():
            self.terminar("Has perdido.")
        elif resultado == RES_TOCADO:
            self.mensaje.config(text=f"La máquina toca en ({fila},{columna}) y sigue...")
            self.ventana.after(PAUSA, self.turno_maquina)
        else:
            self.mensaje.config(text=f"La máquina falla en ({fila},{columna}). ¡Tu turno!")
            self.turno_jugador = True

    def terminar(self, texto):
        """Fin de la partida."""
        self.turno_jugador = False
        self.mensaje.config(text=texto + " Cierra la ventana para salir.")


if __name__ == "__main__":
    ventana = tk.Tk()
    Juego(ventana)
    ventana.mainloop()
