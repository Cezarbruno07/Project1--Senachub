import matplotlib.pyplot as plt


rótulos = ['Maçãs', 'Laranjas', 'Bananas', 'Uvas', 'Figos']
valores = [5, 3, 6, 4, 7]


fig, ax = plt.subplots()

ax.bar(rótulos, valores)


ax.set_xlabel('Fruta')
ax.set_ylabel('Quantidade')
ax.set_title('Quantidades de Frutas')


plt.show()