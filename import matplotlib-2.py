import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]


# Criar uma figura e um eixo
fig, ax = plt.subplots()

# Plotar os dados com as personalizações
ax.plot(x, y, color='red', linestyle='--', marker='o', label='dados')


# Adicionar rótulos e título
ax.set_xlabel('Rótulo X')
ax.set_ylabel('Rótulo Y')
ax.set_title('Título')

# Incluir uma legenda
ax.legend()

# Mostrar o gráfico
plt.show()