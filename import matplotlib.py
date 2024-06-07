import matplotlib.pyplot as plt
# Data
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [500, 75, 1200, 1500, 859, 3200]

# Criar uma figura e um eixo
fig, ax = plt.subplots()

# Plotar os dados
ax.plot(meses, valores)

# Mostrar o gráfico
plt.show()