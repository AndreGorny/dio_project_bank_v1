menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while 1:

    opcao = input(menu)

    if opcao == "d":
        pass

    elif opcao == "s":
        pass

    elif opcao == "e":
        pass

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Por favor, selecione novamente a operação "
              "desejada")

opcao = input(menu)
