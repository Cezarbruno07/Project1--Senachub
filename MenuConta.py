# Após criar as instâncias das contas, podemos criar um menu simples
print("Escolha uma operação:")
print("1 - Extrato")
print("2 - Depósito")
print("3 - Saque")
print("4 - Transferência")

opcao = int(input("Digite o número da operação desejada: "))

if opcao == 1:
    conta1.extrato()
elif opcao == 2:
    valor_deposito = int(input("Digite o valor a ser depositado: "))
    conta1.deposito(valor_deposito)
elif opcao == 3:
    valor_saque = int(input("Digite o valor a ser sacado: "))
    conta1.saque(valor_saque)
elif opcao == 4:
    valor_transferencia = int(input("Digite o valor a ser transferido: "))
    conta_destino = int(input("Digite o número da conta de destino: "))
    # Aqui, você precisará localizar a conta de destino com base no número da conta informado
    # Suponha que você tenha uma lista de contas chamada 'contas' que armazena todas as contas
    conta_destino = next((c for c in contas if c.__numero == conta_destino), None)
    if conta_destino:
        conta1.transferencia(valor_transferencia, conta_destino)
    else:
        print("Conta de destino não encontrada.")
else:
    print("Opção inválida.")
