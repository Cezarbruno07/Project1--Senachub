kg = int(input('Informe a quantidade de quilos pescados: '))
exc = kg - 50
if kg > 50:
    multa = exc * 4 
    print(f'Multa a pagar {multa}')

elif kg <= 50:
    print('Sem valor adiconal')
    print(f'Quantidade em quilos de peixe: {kg}')



