""" lista1 = ["oi",2.0,5,[10,20]]
print (lista1)


lista1 = ["oi",2.0,5,[10,20]]
print (len(lista1))

lista1 = ["oi",2.0,5,[10,20]]
print (len(lista1))
 """

""" #Imprima os itens da lista 
numeros = ["oi",123,87,34,66,8398,44,"Bom dia"]
print(numeros[0])
print(numeros[9-8])
print(numeros[-2])
print(numeros[-4])
print(numeros[5])
print(numeros[7])  """

""" #Selecione numero dentro da lista 
lista1=[3,67,"gato",[56,57,"cachorro"],[],3.14,False]
print(lista1[2][3]) """

""" #Encontre dados dentro das tabelas 
frutas=["maca","laranja","Banana","Cereja"]

print("maca" in frutas)
print("Pera" in frutas) """

""" #Contatenar 
frutas=["maca","laranja","Banana","Cereja"]
print([1,2]+[3,4])
print(frutas + [6,7,8,9])

print(["teste"]*9)
print([1,2,["ola","adeus"]]*2) """

""" # Max-min e sum
a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a))
print(min(a))
print(sum(a)) """

""" #FAtiar uma linha 
lista=["a","b","c","d","e","f"]
print(lista[1:3])
print(lista[:4])
print(lista[3:])
print(lista[:])
print(lista[0:6])
 """
""" # mutable listas replace alterar lista 

frutas= ["banana","maca","cereja"]

frutas[0]="pera"
frutas[-1]="laranja"
print(frutas)
 """


# alterando uma lista pronta 
lista=['a','b','c','d','e','f']

lista[1:3] = ["x","y"]

print (lista)