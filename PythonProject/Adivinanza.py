import pygame
import tkinter as tk
from tkinter import messagebox
import random
import threading

# Inicialización de Pygame
pygame.init()

# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Adivina el número")


# Función para reproducir música de fondo en un hilo separado
def reproducir_musica():
    pygame.mixer.music.load("correcto.mp3")  # Asegúrate de tener este archivo de sonido
    pygame.mixer.music.play()


# Función para jugar el juego
def jugar():
    # Configuración inicial del juego
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 3  # Límite de intentos

    # Función de adivinar
    def adivinar_numero():
        nonlocal intentos
        try:
            numero = int(entry.get())
            intentos += 1

            if numero < numero_secreto:
                label_resultado.config(text="El número es mayor.")
            elif numero > numero_secreto:
                label_resultado.config(text="El número es menor.")
            else:
                label_resultado.config(text=f"¡Correcto! Lo adivinaste en {intentos} intentos.")
                # Reproducir el sonido en un hilo separado
                threading.Thread(target=reproducir_musica).start()
                messagebox.showinfo("¡Felicidades!", f"¡Ganaste en {intentos} intentos!")
                reiniciar_juego()

            if intentos == max_intentos and numero != numero_secreto:
                label_resultado.config(text="¡Se acabaron los intentos!")
                messagebox.showinfo("¡Perdiste!", f"El número era {numero_secreto}. ¡Inténtalo de nuevo!")
                reiniciar_juego()

        except ValueError:
            label_resultado.config(text="Por favor, ingresa un número válido.")

    # Reiniciar juego
    def reiniciar_juego():
        nonlocal intentos
        intentos = 0  # Resetear intentos
        entry.delete(0, tk.END)
        label_resultado.config(text="Intenta adivinar un número entre 1 y 100")
        pygame.mixer.music.stop()

    # Configuración de la interfaz gráfica
    label = tk.Label(root, text="Adivina el número entre 1 y 100", font=("Arial", 14))
    label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack(pady=5)

    boton = tk.Button(root, text="Adivinar", font=("Arial", 14), command=adivinar_numero)
    boton.pack(pady=5)

    label_resultado = tk.Label(root, text="Intenta adivinar un número entre 1 y 100", font=("Arial", 14))
    label_resultado.pack(pady=20)

    # Iniciar el juego cuando se presione el botón de jugar
    reiniciar_juego()

# Crear un botón para iniciar el juego
boton_jugar = tk.Button(root, text="Jugar", font=("Arial", 14), command=jugar)
boton_jugar.pack(pady=20)

# Ejecutar la interfaz gráfica
root.mainloop()
