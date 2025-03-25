# %% Importacion de librerias
import matplotlib.pyplot as plt
import numpy as np


# %% Creacio de un cuadrado
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])

# %% vector de traslación (dx, dy)
dx, dy = 2, 3
translated_square = square + np.array([dx, dy])

# %% Graficar

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.title("Traslación de un cuadrado")
plt.plot(square[:, 0], square[:, 1], label='Original', linestyle="dotted", color='blue')
plt.plot(translated_square[:, 0], translated_square[:, 1], label='Translated', color='blue')
plt.legend()
plt.show()
