class Cadarmas:
    def __init__(self):
        self.armas = {}

    def adicionar_arma(self, codigo, tipo, nserie, calibre, valor, fabricacao, marca):
        self.armas[codigo] = {
            'Tipo': tipo,
            'Numero de Serie': nserie,
            'Calibre': calibre,
            'Valor': valor,
            'Fabricacao': fabricacao,
            'Marca': marca
        }
        print(f"Arma {codigo} adicionada com sucesso!")

    def listar_armas(self):
        if self.armas:
            for codigo, info in self.armas.items():
                print(f"Código: {codigo}")
                print(f"Tipo: {info['Tipo']}")
                print(f"Número de Série: {info['Numero de Serie']}")
                print(f"Calibre: {info['Calibre']}")
                print(f"Valor: {info['Valor']}")
                print(f"Fabricação: {info['Fabricacao']}")
                print(f"Marca: {info['Marca']}")
                print("-" * 20)
        else:
            print("Nenhuma arma cadastrada.")

    def atualizar_arma(self, codigo, tipo=None, nserie=None, calibre=None, valor=None, fabricacao=None, marca=None):
        if codigo in self.armas:
            if tipo:
                self.armas[codigo]['Tipo'] = tipo
            if nserie:
                self.armas[codigo]['Numero de Serie'] = nserie
            if calibre:
                self.armas[codigo]['Calibre'] = calibre
            if valor:
                self.armas[codigo]['Valor'] = valor
            if fabricacao:
                self.armas[codigo]['Fabricacao'] = fabricacao
            if marca:
                self.armas[codigo]['Marca'] = marca
            print(f"Arma {codigo} atualizada com sucesso!")
        else:
            print("Arma não encontrada.")

    def excluir_arma(self, codigo):
        if codigo in self.armas:
            del self.armas[codigo]
            print(f"Arma {codigo} excluída com sucesso!")
        else:
            print("Arma não encontrada.")

    def menu(self):
        while True:
            print("\nSistema de Cadastro de Armas")
            print("1. Adicionar Arma")
            print("2. Listar Armas")
            print("3. Atualizar Arma")
            print("4. Excluir Arma")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                codigo = input("Código da arma: ")
                tipo = input("Tipo de arma: ")
                nserie = input("Número de Série: ")
                calibre = input("Calibre da arma: ")
                valor = input("Valor: ")
                fabricacao = input("Ano de fabricação: ")
                marca = input("Marca: ")
                self.adicionar_arma(codigo, tipo, nserie, calibre, valor, fabricacao, marca)
            elif opcao == '2':
                self.listar_armas()
            elif opcao == '3':
                codigo = input("Código da arma: ")
                tipo = input("Novo tipo de arma (deixe em branco se não for alterar): ")
                nserie = input("Novo número de Série (deixe em branco se não for alterar): ")
                calibre = input("Novo calibre (deixe em branco se não for alterar): ")
                valor = input("Novo valor (deixe em branco se não for alterar): ")
                fabricacao = input("Novo ano de fabricação (deixe em branco se não for alterar): ")
                marca = input("Nova marca (deixe em branco se não for alterar): ")
                self.atualizar_arma(codigo, tipo, nserie, calibre, valor, fabricacao, marca)
            elif opcao == '4':
                codigo = input("Código da arma: ")
                self.excluir_arma(codigo)
            elif opcao == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")

def main():
    sistema = Cadarmas()
    sistema.menu()

if __name__ == "__main__":
    main()
