# %% Importacion de librerias
import matplotlib.pyplot as plt
import numpy as np

# %% Definir un pentagono
pentagon = np.array([
    [0, 1],
    [0.95, 0.31],
    [0.59, -0.81],
    [-0.59, -0.81],
    [-0.95, 0.31],
    [0, 1]
])

# %% Definir angulo de rotación en grados
theta = np.radians(45)

# %% Matriz de rotación
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# %% Aplicar rotación
rotated_pentagon = np.dot(pentagon, rotation_matrix.T)

# %% Graficar

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.title("Rotación de un pentágono")
plt.plot(pentagon[:, 0], pentagon[:, 1], label='Original', linestyle="dotted", color='blue')
plt.plot(rotated_pentagon[:, 0], rotated_pentagon[:, 1], label='Rotated', color='blue')
plt.legend()
plt.show()
