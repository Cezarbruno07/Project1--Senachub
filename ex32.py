n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

total = (n1 + n2)/2

if total > 9 and total <= 10:
    print(total)
    print('Aprovado')

elif total > 7.5 and total < 9:
    print(total)
    print('Aprovado')

elif total > 6 and total <7.49:
    print(total)
    print('Aprovado')
    
elif total > 4 and total <5.99:
    print(total)
    print('Reprovado')

else:
    print(total)
    print('Reprovado')
    

