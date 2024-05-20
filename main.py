from services import depositar, sacar, exibir_extrato, criar_usuario, \
    criar_conta, listar_contas, listar_usuarios

saldo = 0
limite = 500
extrato = []
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"

menu = """

======== TEST BANK V_2 ========

    Selecione a opção desejada:

    [nu] Novo Usuário
    [nc] Nova Conta
    -----------------------
    [d] Depositar
    [s] Sacar
    [e] Extrato
    -----------------------
    [lu] Listar Usuários
    [lc] Listar Contas
    [q] Sair

===============================

    =>"""

while 1:

    print(f"\n    Saldo atual: R${saldo:.2f}")
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: R$"))

        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "s":

        valor = float(input("Informe o valor a ser sacado: R$"))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":

        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":

        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)

        contas.append(nova_conta)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "lu":
        listar_usuarios(usuarios)

    elif opcao == "q":
        print("Obrigado por usar o sistema. Até logo! \n")
        break

    else:
        print("Opção inválida. Por favor, selecione novamente a operação "
              "desejada \n")
