import math
area = float(input("Digite o TAmanho da aréa "))
area_perda =area *1.1
litros_tinta= area_perda /6
qtd_latas_18=math.ceil(litros_tinta/18)
qtd_latas_36=math.ceil(litros_tinta/36)
preco_lata18=qtd_latas_18 *80
preco_lata36=qtd_latas_18 *25

qtd_latas_mix=qtd_latas_18

qtd_latas_mix = match.ceil((litros_tinta -qtd_latas_18 *18)/3.6)
