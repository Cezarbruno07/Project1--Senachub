# Sistema de Cadastro de Clientes
class clientes():
 clientes = {}

def adicionar_cliente(codigo, nome, email, telefone):
    clientes[codigo] = {
        'nome': nome,
        'email': email,
        'telefone': telefone
    }
    print(f"Cliente {nome} adicionado com sucesso!")

def listar_clientes():
    if clientes:
        for codigo, info in clientes.items():
            print(f"Código: {codigo}")
            print(f"Nome: {info['nome']}")
            print(f"Email: {info['email']}")
            print(f"Telefone: {info['telefone']}")
            print("-" * 20)
    else:
        print("Nenhum cliente cadastrado.")

def atualizar_cliente(codigo, nome=None, email=None, telefone=None):
    if codigo in clientes:
        if nome:
            clientes[codigo]['nome'] = nome
        if email:
            clientes[codigo]['email'] = email
        if telefone:
            clientes[codigo]['telefone'] = telefone
        print(f"Cliente {codigo} atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")

def excluir_cliente(codigo):
    if codigo in clientes:
        del clientes[codigo]
        print(f"Cliente {codigo} excluído com sucesso!")
    else:
        print("Cliente não encontrado.")

def menu():
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
            email = input("Email do cliente: ")
            telefone = input("Telefone do cliente: ")
            adicionar_cliente(codigo, nome, email, telefone)
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            codigo = input("Código do cliente: ")
            nome = input("Novo nome (deixe em branco se não for alterar): ")
            email = input("Novo email (deixe em branco se não for alterar): ")
            telefone = input("Novo telefone (deixe em branco se não for alterar): ")
            atualizar_cliente(codigo, nome, email, telefone)
        elif opcao == '4':
            codigo = input("Código do cliente: ")
            excluir_cliente(codigo)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
