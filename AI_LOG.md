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
- **Objetivo:** Resolver una duda sobre cómo organizar las variables del juego.
- **Prompt:** «¿Cómo puedo organizar las variables de un juego de Hundir la Flota para tener separados el tamaño del tablero, los barcos, sus orientaciones y los símbolos que se utilizan durante la partida?»
- **Que cambie:** Revisé las variables propuestas y adapté los nombres y valores a la estructura de mi juego.
- **Como lo comprobe:** Comprobando que las variables estuvieran definidas correctamente y que el resto de archivos pudieran utilizarlas.
- **Que decidi yo:** Decidí los valores definitivos, los nombres de las variables y cuáles necesitaba utilizar.

### Prompt 2 – clases.py
- **Objetivo:** Entender cómo organizar la clase que gestiona el tablero y el funcionamiento de los barcos.
- **Prompt:**«¿Cómo puedo organizar una clase Tablero en Python para un juego de Hundir la Flota, que tenga una matriz, coloque los barcos aleatoriamente sin que se salgan ni se solapen, y permita registrar los disparos y controlar las vidas? Explícamelo por partes».
- **Que cambie:** Adapté la estructura de la clase a mi código y revisé los métodos para que se ajustaran al funcionamiento del juego.
- **Como lo comprobe:** Revisando cómo se creaba el tablero, cómo se colocaban los barcos y cómo se registraban los disparos.
- **Que decidi yo:** Decidí cómo se gestionaría el tablero y qué información debía guardar para controlar los barcos y los disparos.

### Prompt 3 – funciones.py
- **Objetivo:** Mejorar la validación de las coordenadas y la selección de disparos.
- **Prompt:** «¿Cómo puedo hacer en Python una función que pida al jugador las coordenadas de un disparo en formato fila,columna, compruebe que sean números y estén dentro del tablero 10x10 y vuelva a pedirlas si son incorrectas? ¿Y cómo podría hacer que la máquina escogiera una casilla a la que todavía no ha disparado?».
- **Que cambie:** Adapté las comprobaciones de entrada y la lógica de los disparos para que funcionaran con las características de mi juego.
- **Como lo comprobe:**  Probando entradas incorrectas, como letras, coordenadas fuera del tablero, números incompletos y disparos repetidos.
- **Que decidi yo:** Decidí cómo gestionar las entradas incorrectas y qué comportamiento debía tener la máquina al elegir sus disparos.

### Prompt 4 – main.py
- **Objetivo:** Organizar el funcionamiento general de la partida y los turnos.
- **Prompt:** «¿Cómo puedo organizar el main.py de un juego de Hundir la Flota para que el jugador y la máquina alternen sus turnos, puedan repetir turno cuando aciertan, cambien de turno cuando fallan y la partida termine cuando uno de los dos se quede sin barcos?».
- **Que cambie:** Revisé el orden de las llamadas a las funciones y adapté el flujo de la partida para que encajara con los otros archivos.
- **Como lo comprobe:** Ejecutando el juego y comprobando el funcionamiento de los turnos y la finalización de la partida.
- **Que decidi yo:**  Decidí el funcionamiento de los turnos, el orden de las acciones y las condiciones para terminar el juego.