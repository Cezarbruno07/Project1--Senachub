class Clientes:
    def __init__(self):
        self.clientes = {}

    def adicionar_cliente(self, codigo, nome, cpf,email, telefone):
        self.clientes[codigo] = {
            'nome': nome,
            'email': email,
            'cpf':cpf,
            'telefone': telefone
        }
        print(f"Cliente {nome} adicionado com sucesso!")

    def listar_clientes(self):
        if self.clientes:
            for codigo, info in self.clientes.items():
                print(f"Código: {codigo}")
                print(f"Nome: {info['nome']}")
                print(f"cpf: {info['cpf']}")
                print(f"Email: {info['email']}")
                print(f"Telefone: {info['telefone']}")
                print("-" * 20)
        else:
            print("Nenhum cliente cadastrado.")

    def atualizar_cliente(self, codigo, nome=None,cpf=None, email=None, telefone=None):
        if codigo in self.clientes:
            if nome:
                self.clientes[codigo]['nome'] = nome
            if email:
                self.clientes[codigo]['Cpf'] = cpf
            if email:
                self.clientes[codigo]['Email'] = email
            if telefone:
                self.clientes[codigo]['telefone'] = telefone
            print(f"Cliente {codigo} atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def excluir_cliente(self, codigo):
        if codigo in self.clientes:
            del self.clientes[codigo]
            print(f"Cliente {codigo} excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

    def menu(self):
        while True:
            print("\nSistema de Cadastro de Clientes")
            print("1. Adicionar Cliente")
            print("2. Listar Clientes")
            print("3. Atualizar Cliente")
            print("4. Excluir Cliente")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                codigo = input("Código do cliente: ")
                nome = input("Nome do cliente: ")
                cpf = input("Cpf do Cliente: ")
                email = input("Email do cliente: ")
                telefone = input("Telefone do cliente: ")
                self.adicionar_cliente(codigo, nome,cpf, email, telefone)
            elif opcao == '2':
                self.listar_clientes()
            elif opcao == '3':
                codigo = input("Código do cliente: ")
                nome = input("Novo nome (deixe em branco se não for alterar): ")
                cpf = input("Novo Cpf (deixe em branco se não for alterar): ")
                email = input("Novo email (deixe em branco se não for alterar): ")
                telefone = input("Novo telefone (deixe em branco se não for alterar): ")
                self.atualizar_cliente(codigo, nome,cpf, email, telefone)
            elif opcao == '4':
                codigo = input("Código do cliente: ")
                self.excluir_cliente(codigo)
            elif opcao == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = Clientes()
    sistema.menu()
