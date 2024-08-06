n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

total = (n1 + n2)/2 

if total >= 7 and total < 10:
    print('Aprovado')

elif total < 7:
    print('Reprovado')

elif total == 10:
    print('Aprovado com distinção.')