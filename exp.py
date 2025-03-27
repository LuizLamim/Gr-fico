
import numpy as np
import matplotlib.pyplot as plt

# Gera valores de x no intervalo desejado
x = np.linspace(-5, 5, 100)  # 100 pontos entre -5 e 5

# Calcula os valores de y usando a função exponencial
y = np.exp(x)

# Cria o gráfico
plt.figure(figsize=(8, 6))  # Define o tamanho da figura
plt.plot(x, y, label='y = e^x')

# Adiciona título e rótulos aos eixos
plt.title('Gráfico da Função Exponencial e^x')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona grade e legenda
plt.grid(True)
plt.legend()

# Exibe o gráfico   a  
plt.show()