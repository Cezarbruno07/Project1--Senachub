# o Pescador
LIMITE = 50
MULTA = 4.0

excesso = 0.0
(peso) = input(float("Digite o peso dos peixes: "))

if peso>LIMITE:
    excesso = (float(peso) - LIMITE) * MULTA
    print("O valor da multa eh de R$ %.2f " % excesso)
else:
    excesso = 0
    print("Excesso: %.2f" % excesso)