# AI_LOG

## Resumen por modulo

| Modulo | Quien lo ha llevado | Apoyo en IA (0-3) |
|---|---|---|
| variables.py | Mireia | 1 |
| clases.py | Mireia | 2 |
| funciones.py | Mireia | 2 |
| main.py | Mireia | 2 |

## Registro de prompts

### Prompt 1 – variables.py
- **Objetivo:** Resolver una duda puntual sobre la organización de las variables del juego.
- **Prompt:** «¿Cómo puedo organizar las variables de un juego de Hundir la Flota para tener más claro el tamaño del tablero, los barcos y los símbolos que se utilizan durante la partida?»
- **Que cambie:** Revisé las variables y adapté sus nombres y valores a lo que necesitaba el juego.
- **Como lo comprobe:** Revisando que los valores fueran correctos y que se utilizaran adecuadamente en el resto del programa.
- **Que decidi yo:** Decidí los valores definitivos de las variables y cuáles necesitaba realmente.

### Prompt 2 – clases.py
- **Objetivo:** Entender mejor la estructura y el funcionamiento del código.
- **Prompt:** «¿Me puedes explicar cómo organizar el código de Hundir la Flota para que sea más fácil de entender y mantener, y cómo guardar la información de los barcos sin complicar demasiado el programa?»
- **Que cambie:** Revisé la estructura propuesta y adapté algunas partes para que encajaran con el resto de archivos.
- **Como lo comprobe:** Revisando cómo se guardaba y utilizaba la información de los barcos durante el juego.
- **Que decidi yo:** Decidí cómo quería representar los barcos y qué información era necesaria guardar.

### Prompt 3 – funciones.py
- **Objetivo:** Mejorar la comprobación de los disparos y la entrada de coordenadas.
- **Prompt:** «¿Cómo puedo comprobar en Python que las coordenadas que introduce el jugador son válidas y detectar si un disparo es un acierto, un fallo o una casilla a la que ya se había disparado?»
- **Que cambie:** Adapté las comprobaciones para controlar mejor las coordenadas y los diferentes resultados de los disparos.
- **Como lo comprobe:** Probando diferentes entradas, como coordenadas con letras, 11,2, un solo número y disparos repetidos, para comprobar cómo reaccionaba el programa.
- **Que decidi yo:** Decidí cómo debía reaccionar el juego ante cada tipo de entrada y qué mensajes debía mostrar.

### Prompt 4 – main.py
- **Objetivo:** Comprender y mejorar el flujo general de la partida.
- **Prompt:** «¿Cómo puedo organizar el archivo main.py de un juego de Hundir la Flota para controlar el inicio de la partida, los turnos de los jugadores, los disparos y la condición de victoria, utilizando las funciones de los otros archivos?»
- **Que cambie:** Revisé el orden de las llamadas y adapté el funcionamiento principal para que estuviera conectado correctamente con el resto del proyecto.
- **Como lo comprobe:** Ejecutando el juego y revisando el flujo de la partida, los turnos y la condición de finalización.
- **Que decidi yo:**  Decidí el orden del juego, cómo se gestionaban los turnos y cuándo debía terminar la partida.