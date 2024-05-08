

vh = float(input('Valor da hora:'))
qh = int(input('Quantidade de horas trabalhadas:'))

salario_bruto = vh * qh
inss = 8/100 * salario_bruto
sindicato = 5/100 * salario_bruto
ir = 11/100 * salario_bruto

salario_liquido = salario_bruto - inss - sindicato - ir

print (' + Salário Bruto: R$ %.2f' %salario_bruto)
print (' - IR: R$ %.2f' %ir)
print (' - INSS: R$ %.2f' %inss)
print (' - Sindicato: R$ %.2f' %sindicato)
print (' = Salário Liquido: R$ %.2f' %salario_liquido)