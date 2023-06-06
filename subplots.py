import numpy as np
import matplotlib.pyplot as plt

np.random.seed(6)
x = np.arange(1, 11)
y1 = np.random.randint(1, 400, 10)
y2 = np.random.randint(150, 500, 10)
y3 = np.random.randint(200, 600, 10)

plt.figure(figsize=(15, 5))
plt.suptitle('Figura', fontsize=15)

plt.subplot(1, 3, 1)
plt.plot(x, y1, color='k')
plt.title('subplot 1', pad=10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1, 3, 2)
plt.plot(x, y2, color='r')
plt.title('subplot 2', pad=10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1, 3, 3)
plt.plot(x, y3, color='g')
plt.title('subplot 3', pad=10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Espaçamento
plt.tight_layout(pad=4)
plt.show()
