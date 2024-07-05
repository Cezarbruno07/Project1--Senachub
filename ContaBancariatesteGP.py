class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso!"
        else:
            return "Valor de depósito inválido!"

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        elif valor > self.saldo:
            return "Saldo insuficiente!"
        else:
            return "Valor de saque inválido!"


# Exemplo de uso
conta = ContaBancaria(input("Digite seu Nome "))

print(conta.verificar_saldo())

print(conta.depositar(500))
print(conta.verificar_saldo())

print(conta.sacar(200))
print(conta.verificar_saldo())

print(conta.sacar(1500))
print(conta.verificar_saldo())
