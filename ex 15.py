hora = int(input('Digite as horas trabalhadas: '))
ganho = int(input('Digite o valor das horas trabalhadas: '))

bruto = ganho * hora

ir = bruto*0.11
inss = bruto*0.08
sind = bruto*0.05
liquido = bruto - ir - inss - sind

print(f'O valor bruto é de: {bruto}')
print(f'O salário liquido é: {liquido}')
print(f'O valor do imposto de renda é de: {ir}')
print(f'O valor do INSS é de : {inss}')
print(f'O valor do sindicato é de: {sind}')