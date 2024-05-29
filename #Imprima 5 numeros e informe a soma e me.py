#Aula 29/5/2024 media e soma de numeros
num=int(input("Quantos numeros: "))

inicial=int(input("Numero 1: "))

count=1
maior=inicial
soma=inicial

while count< num:
    count += 1
    temp=int(input("Numero %d: " % count))
    soma += temp
    if temp>maior:
        maior = temp
    
media = soma / num
print("Soma:",soma)
print("Maior:", maior)
print("Media: %.2f" % (soma/num))


