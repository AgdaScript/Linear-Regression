from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo: temperatura (x) e preço do sorvete (y)
temperatura = np.array([20, 22, 25, 27, 30]).reshape(-1, 1)  # Variável independente (X)
preco = np.array([40, 44, 50, 54, 60])                      # Variável dependente (y)

# Criação do modelo
modelo = LinearRegression()
modelo.fit(temperatura, preco)

# Fazendo uma previsão: quanto custaria com 28 graus?
nova_temp = np.array([[28]])
previsao = modelo.predict(nova_temp)

print(f'Preço previsto para 28°C: {previsao[0]:.2f} unidades')

# Visualização do resultado
plt.scatter(temperatura, preco, color='blue', label='Dados reais')
plt.plot(temperatura, modelo.predict(temperatura), color='red', label='Linha de regressão')
plt.scatter(nova_temp, previsao, color='green', label='Previsão para 28°C')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Preço do Sorvete')
plt.legend()
plt.title('Regressão Linear - Sorvete x Temperatura')
plt.show()
