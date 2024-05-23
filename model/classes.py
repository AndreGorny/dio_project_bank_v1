class Cliente:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, nome, cpf, nascimento) -> None:
        super().__init__(endereco, contas)
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento


class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = []

    def exibir_saldo(saldo: float):
        return saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.append(valor)
            print("Depósito efetuado com sucesso. O novo saldo é de "
                  f"R$ {self._saldo:.2f}.")


class ContaCorrente(Conta):
    LIMITE_SAQUES = 3
    limite = 500

    def __init__(self, numero, cliente) -> None:
        super().__init__(numero, cliente)
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= ContaCorrente.LIMITE_SAQUES:
            print(f"Seu limite é de {ContaCorrente.LIMITE_SAQUES} saques."
                  "Quantidade de saques excedida.")
        elif valor > ContaCorrente.limite:
            print(f"O limite máximo é de R${ContaCorrente.limite:.2f}. "
                  "Valor excedido")
        elif valor > self._saldo:
            print("Saldo insuficiente. Seu saldo atual é de R$"
                  f"{self._saldo:.2f}")
        elif valor > 0:
            self._saldo -= valor
            self._historico.append(-valor)
            self.numero_saques += 1
            limite_restante = ContaCorrente.LIMITE_SAQUES - self.numero_saques
            print("Sucesso! Retire o dinheiro! \n"
                  f"Você ainda tem {limite_restante} saques disponíveis")
            print(f"Seu novo saldo é de R${self._saldo:.2f}")
        else:
            print("Valor inválido. O valor deve ser maior que zero.")

    def depositar(self, valor):
        super().depositar(valor)


class Historico:
    pass


class Transacao:
    def __init__(self, conta, valor) -> None:
        pass


class Saque(Transacao):
    def __init__(self, conta, valor, ) -> None:
        super().__init__(conta, valor)

    excedeu_saques = numero_saques > limite_saques



class Deposito(Transacao):
    pass