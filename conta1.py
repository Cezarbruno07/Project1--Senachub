class Conta:

    def __init__(self, numero_conta, nome_titular, saldo_conta, limite_conta):
        self.__numero = numero_conta
        self.__titular = nome_titular
        self.__saldo = saldo_conta
        self.__limite = limite_conta
        self.__codigo_banco = "001"

    def extrato(self):
            print("Olá {}, o seu saldo é R${}" .format(self.__titular, self.__saldo))

    def  deposito(self, deposito):
        self.__saldo = deposito + self.__saldo
        #print("{}, o seu novo saldo é de R${}".format(self.__titular, self.__saldo))


    def __pode_sacar(self, valor_sacar):
        valor_sacar_max = self.__saldo + self.__limite
        return valor_sacar <= valor_sacar_max

    def  saque(self, saque):
        if (self.__pode_sacar(saque)):
            self.__saldo = self.__saldo - saque
            print("O saldo atual é de: {}" .format(self.__saldo))
        else:
            print("O saque excede o limite do saldo permitido")
        #print("{}, o seu novo saldo é de R${}".format(self.__titular, self.__saldo))

    def transfere(self, valor, conta_a, conta_b):
        conta_a.saque(valor)
        conta_b.deposito(valor)
        print("O seu novo saldo é de {}" .format(conta_b.extrato()))

    @staticmethod
    def codigo_banco():
        return "Código banco: 001"


    @staticmethod
    def codigo_bancos():
        codigo_bancos = {"BB":"001", "Caixa":"104", "Bradesco":"237"}
        return codigo_bancos


    @property
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular.title()

    def get_limite(self):
        return self.__limite