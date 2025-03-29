import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def schrodinger_solver(L, N, V):
    """
    Resolve a equação de Schrödinger independente do tempo para um potencial unidimensional.

    Args:
        L: Comprimento da caixa.
        N: Número de pontos de grade.
        V: Função potencial.

    Returns:
        Energias e funções de onda.
    """

    # Constantes
    hbar = 1.0
    m = 1.0

    # Grade espacial
    x = np.linspace(0, L, N)
    dx = x[1] - x[0]

    # Matriz Hamiltoniana
    H = np.zeros((N - 2, N - 2))
    for i in range(N - 2):
        H[i, i] = hbar**2 / (m * dx**2) + V(x[i + 1])
        if i > 0:
            H[i, i - 1] = -hbar**2 / (2 * m * dx**2)
            H[i - 1, i] = -hbar**2 / (2 * m * dx**2)

    # Resolve os autovalores e autovetores
    E, psi = la.eigh(H)

    # Adiciona pontos de contorno
    psi = np.vstack((np.zeros(N - 2), psi, np.zeros(N - 2)))

    return E, psi, x

# Parâmetros
L = 1.0
N = 100
V = lambda x: 0.0  # Potencial dentro da caixa

# Resolve a equação de Schrödinger
E, psi, x = schrodinger_solver(L, N, V)

# Plota os resultados
plt.figure(figsize=(10, 6))
for i in range(5):  # Plota os 5 primeiros níveis de energia
    plt.plot(x, psi[i] + E[i], label=f'E{i} = {E[i]:.2f}')
plt.xlabel('x')
plt.ylabel('Energia')
plt.title('Partícula em uma caixa')
plt.legend()
plt.show()

print("Níveis de energia:")
print(E[:5])