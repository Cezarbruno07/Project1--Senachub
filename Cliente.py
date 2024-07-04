class Pessoa(Pessoa):
    def __init__(self._idade):

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserirconta(self, conta):
        self.conta = conta