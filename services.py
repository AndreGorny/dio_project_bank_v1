def depositar(saldo, valor, extrato, /):

    if valor > 0:
        extrato.append(valor)
        print("Depósito efetuado com sucesso!")
        saldo += valor
        print(f"Seu novo saldo é de R${saldo:.2f}")

    else:
        print("Valor inválido. O valor deve ser maior que zero.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if numero_saques > limite_saques:
        print(f"Seu limite é de {limite_saques} saques. Quantidade "
              "excedida")

    elif valor > limite:
        print(f"O limite máximo é de R${limite:.2f}. Valor excedido")

    elif valor > saldo:
        print(f"Saldo insuficiente. Seu saldo atual é de R${saldo:.2f}")

    elif valor > 0:
        saldo -= valor
        extrato.append(-valor)
        numero_saques += 1
        print("Sucesso! Retire o dinheiro! \n"
              f"Você ainda tem {limite_saques - numero_saques} saques "
              "disponíveis")

    else:
        print("Valor inválido. O valor deve ser maior que zero.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):

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


def criar_usuario(usuarios):
    cpf = input("Insira o cpf (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nUsuário já cadastrado!")

    else:

        nome = input("Nome completo: ")
        dt_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço (Rua, nº - bairro - cidade/uf): ")

        usuarios.append(
            {"cpf": cpf,
             "nome": nome,
             "dt_nascimento": dt_nascimento,
             "endereco": endereco,
             "contas": []
             }
             )

        print("\nUsuário cadastrado com sucesso!")


def criar_conta(ag, numero_conta, usuarios):
    cpf = input("Insira o cpf (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:

        def encontrar_indice(cpf, usuarios):
            filtro = [(indice, usuario) for indice, usuario in enumerate
                      (usuarios) if usuario['cpf'] == cpf]
            return filtro[0][0] if filtro else None

        usuarios[encontrar_indice(cpf, usuarios)]['contas'].append(
            numero_conta)
        print("\nConta criada com sucesso!")
        return {"agencia": ag, "conta": numero_conta, "usuario": usuario}
    else:
        print("\nUsuário não cadastrado. Crie um usuário antes de criar a "
              "conta")


def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência: {conta['agencia']} "
              f"Conta: {conta['conta']} "
              f"Usuário: {conta['usuario']['nome']}")


def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(50 * "-")
        print(f"CPF: {usuario['cpf']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Data Nascimento: {usuario['dt_nascimento']}")
        print(f"Endereço: {usuario['endereco']}")
        print(f"Contas associadas: {usuario['contas']}")


def filtrar_usuarios(cpf, usuarios):
    filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro[0] if filtro else None
