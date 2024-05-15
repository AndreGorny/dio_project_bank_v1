saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

menu = """

    Bem vindo! Selecione a opção desejada:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>"""

while 1:

    print(f"\n    Saldo atual: R${saldo:.2f}")
    opcao = input(menu)

    if opcao == "d":
        while 1:
            valor_deposito = float(input(
                "Informe o valor a ser depositado: R$"))
            if valor_deposito <= 0:
                print("Valor inválido. O valor deve ser maior que zero.")
            else:
                extrato.append(+valor_deposito)
                print("Depósito efetuado com sucesso!")
                saldo += valor_deposito
                print(f"Seu novo saldo é de R${saldo:.2f}")
                break

    elif opcao == "s":  # não está limitando a quantidade de saques
        valor_saque = float(input("Informe o valor a ser sacado: R$"))
        if numero_saques > LIMITE_SAQUES:
            print(f"Seu limite é de {LIMITE_SAQUES} saques. Quantidade "
                  "excedida")
            break

        elif valor_saque > limite:
            print(f"O limite máximo é de R${limite:.2f}. Valor excedido")

        elif valor_saque > saldo:
            print(f"Saldo insuficiente. Seu saldo atual é de R${saldo:.2f}")

        else:
            saldo -= valor_saque
            extrato.append(-valor_saque)
            numero_saques += 1
            print("Sucesso! Retire o dinheiro! \n"
                  f"Você ainda tem {LIMITE_SAQUES - numero_saques} saques "
                  "disponíveis")

    elif opcao == "e":
        for valor in extrato:
            if valor >= 0:
                print(f"Depósito  +{valor}")
            else:
                print("Saque", valor)
        print("-*10")
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "q":
        print("Obrigado por usar o sistema. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, selecione novamente a operação "
              "desejada")
