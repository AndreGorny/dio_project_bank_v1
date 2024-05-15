saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

menu = """

======== TEST BANK V_1 ========

    Selecione a opção desejada:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

===============================

    =>"""

while 1:

    opcao = input(menu)

    if opcao == "d":
        while 1:
            valor_deposito = float(input(
                "Informe o valor a ser depositado: R$"))
            if valor_deposito <= 0:
                print("Valor inválido. O valor deve ser maior que zero. \n")
            else:
                extrato.append(+valor_deposito)
                print("Depósito efetuado com sucesso!")
                saldo += valor_deposito
                print(f"Seu novo saldo é de R${saldo:.2f} \n")
                break

    elif opcao == "s":  # não está limitando a quantidade de saques
        valor_saque = float(input("Informe o valor a ser sacado: R$"))
        if numero_saques >= LIMITE_SAQUES:
            print(f"Seu limite é de {LIMITE_SAQUES} saques. Quantidade "
                  "excedida \n")

        elif valor_saque > limite:
            print(f"O limite máximo é de R${limite:.2f}. Valor excedido \n")

        elif valor_saque > saldo:
            print(f"Saldo insuficiente. Seu saldo atual é de R${saldo:.2f} \n")

        elif valor_saque <= 0:
            print("Valor inválido. O valor deve ser positivo.")

        else:
            saldo -= valor_saque
            extrato.append(-valor_saque)
            numero_saques += 1
            print("Sucesso! Retire o dinheiro! \n")
            if numero_saques == LIMITE_SAQUES:
                print("Você utilizou seu limite diário de saques. \n")
            else:
                print(f"Você ainda tem {LIMITE_SAQUES - numero_saques} saques "
                      "disponíveis \n")
                print(f"Seu novo saldo é de R${saldo:.2f} \n")

    elif opcao == "e":
        print("\n============= EXTRATO =============\n")
        if extrato == []:
            print("Não foram efetuadas movimentações.")
            print("\n===================================")
        else:
            for valor in extrato:
                if valor >= 0:
                    print(f"Depósito  +{valor:.2f}")
                else:
                    print(f"Saque {valor:.2f}")
            print("\n", 30*"-", "\n")
            print(f"Saldo atual: R${saldo:.2f} \n")
            print("===================================")

    elif opcao == "q":
        print("Obrigado por usar o sistema. Até logo! \n")
        break

    else:
        print("Opção inválida. Por favor, selecione novamente a operação "
              "desejada \n")
