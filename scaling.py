# %% Importacion de librerias
import matplotlib.pyplot as plt
import numpy as np

# %% Definir un triangulo
triangle = np.array([[0, 0], [2, 0], [1, 2], [0, 0]])

# %% Factor de escala
s = 1.5
scaled_triangle = triangle * s

# %% Graficar
#
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.title("Escalado de un triangulo")
plt.plot(triangle[:, 0], triangle[:, 1], label='Original', linestyle="dotted", color='blue')
plt.plot(scaled_triangle[:, 0], scaled_triangle[:, 1], label='Scaled', color='blue')
plt.legend()
plt.show()
