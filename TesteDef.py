def total():
    total = 0
cont = 0
while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        break
    dias = int(input('Digite o número de dias em atraso: '))
    print (valorPagamento(valor, dias))
    total += valorPagamento(valor, dias)
    cont += 1

print('Quantidade total: %d' % cont)
print('Valor total das prestações: %.2f' % total)
    
    