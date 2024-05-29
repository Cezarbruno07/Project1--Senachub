#Imprima 5 numeros e informe a soma e media dos numeros
numeros=int(input("Quantos numeros: "))

primeiro=int(input("Numero 1: "))

count=1
maior=primeiro
soma=primeiro

while count< numeros:
    count += 1
    temp=int(input("Numero %d: " % count))
    soma += temp
    if temp>maior:
        maior = temp
    
media = soma / numeros
print("Soma:",soma)
print("Maior:", maior)
print("Media: %.2f" % (soma/numeros))


