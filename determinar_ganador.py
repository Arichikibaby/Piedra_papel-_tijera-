import tkinter as tk
from tkinter import messagebox
import random

class JuegoPiedraPapelTijera:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")
        self.root.geometry("400x400")

        # Inicializar puntuaciones
        self.puntuacion_jugador = 0
        self.puntuacion_computadora = 0

        # Título del juego con color bonito
        self.titulo_label = tk.Label(root, text="Juego Piedra, Papel o Tijera", font=("Arial", 16), fg="blue")
        self.titulo_label.pack(pady=20)

        # Botones para seleccionar opción con colores
        self.boton_piedra = tk.Button(root, text="Piedra", width=15, height=2, command=lambda: self.jugar("Piedra"), bg="yellow", fg="black")
        self.boton_piedra.pack(pady=5)

        self.boton_papel = tk.Button(root, text="Papel", width=15, height=2, command=lambda: self.jugar("Papel"), bg="yellow", fg="black")
        self.boton_papel.pack(pady=5)

        self.boton_tijera = tk.Button(root, text="Tijera", width=15, height=2, command=lambda: self.jugar("Tijera"), bg="yellow", fg="black")
        self.boton_tijera.pack(pady=5)

        # Etiqueta para mostrar el resultado con color bonito
        self.etiqueta_resultado = tk.Label(root, text="Resultado", font=("Arial", 14), fg="green")
        self.etiqueta_resultado.pack(pady=20)

        # Etiqueta para mostrar la selección de la computadora con color bonito
        self.etiqueta_computadora = tk.Label(root, text="Computadora: ", font=("Arial", 12), fg="red")
        self.etiqueta_computadora.pack(pady=5)

        # Etiquetas para mostrar la puntuación con colores llamativos
        self.etiqueta_puntuacion_jugador = tk.Label(root, text="Puntuación Jugador: 0", font=("Arial", 12), fg="purple")
        self.etiqueta_puntuacion_jugador.pack(pady=5)

        self.etiqueta_puntuacion_computadora = tk.Label(root, text="Puntuación Computadora: 0", font=("Arial", 12), fg="purple")
        self.etiqueta_puntuacion_computadora.pack(pady=5)

        # Botón para reiniciar el juego con color verde
        self.boton_reiniciar = tk.Button(root, text="Reiniciar Juego", width=15, height=2, command=self.reiniciar_juego, bg="green", fg="white")
        self.boton_reiniciar.pack(pady=20)

    # Función para determinar el ganador
    def determinar_ganador(self, jugador, computadora):
        if jugador == computadora:
            return "Empate"
        elif (jugador == "Piedra" and computadora == "Tijera") or \
             (jugador == "Tijera" and computadora == "Papel") or \
             (jugador == "Papel" and computadora == "Piedra"):
            return "Ganaste"
        else:
            return "Perdiste"

    # Función para jugar una ronda
    def jugar(self, opcion_jugador):
        opciones = ["Piedra", "Papel", "Tijera"]
        # Elección aleatoria de la computadora
        opcion_computadora = random.choice(opciones)

        # Mostrar la elección de la computadora
        self.etiqueta_computadora.config(text=f"Computadora: {opcion_computadora}")

        # Determinar el resultado
        resultado = self.determinar_ganador(opcion_jugador, opcion_computadora)
        self.etiqueta_resultado.config(text=resultado)

        # Actualizar las puntuaciones
        if resultado == "Ganaste":
            self.puntuacion_jugador += 1
            self.etiqueta_puntuacion_jugador.config(text=f"Puntuación Jugador: {self.puntuacion_jugador}")
            # Mostrar mensaje de ganaste en grande
            self.mensaje_ganaste()
        elif resultado == "Perdiste":
            self.puntuacion_computadora += 1
            self.etiqueta_puntuacion_computadora.config(text=f"Puntuación Computadora: {self.puntuacion_computadora}")

    # Función para mostrar el mensaje grande de "¡Ganaste!"
    def mensaje_ganaste(self):
        messagebox.showinfo("¡Felicidades!", "¡GANASTE ESTA RONDA!", icon="info")

    # Función para reiniciar el juego
    def reiniciar_juego(self):
        self.puntuacion_jugador = 0
        self.puntuacion_computadora = 0
        self.etiqueta_puntuacion_jugador.config(text="Puntuación Jugador: 0")
        self.etiqueta_puntuacion_computadora.config(text="Puntuación Computadora: 0")
        self.etiqueta_resultado.config(text="Resultado")
        self.etiqueta_computadora.config(text="Computadora: ")

# Inicialización de la ventana principal
root = tk.Tk()
juego = JuegoPiedraPapelTijera(root)

# Ejecutar la aplicación
root.mainloop()
