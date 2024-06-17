""" import random
for line in open('wordlist.txt', encoding='utf-8'):
    line = list(linha.strip())
    random(str(line))
    result = ''.join(line)
print(result)
 """
""" rt random

a = list(range(1, 11))
random.shuffle(a)
print(a) """

""" def imprimeLinha(numero):
    for n in range(1, numero + 1):
     print(('{}').format(n), end='')
print()
   
def imprimeSequencia(numero):
      for numero in range(numero + 1):
           imprimeLinha(numero)
 """
import random
 def aleatorio(valor):
 y=len(valor)
     x=random.sample(valor,y)
     x=''.join(x)
     print(x)
     aleatorio()