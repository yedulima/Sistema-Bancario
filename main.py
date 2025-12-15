from datetime import datetime, UTC
from inspect import cleandoc

class Cliente:
    """
    Classe que representa um cliente.

    Atributos:
    ----------
    nome: str
        nome do cliente
    """
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self) -> str:
        return f"Cliente:\t{self.nome}"

    def __repr__(self) -> str:
        return f"nome={self.nome}"

class Historico:
    """
    Classe que representa o histórico de transações de uma conta bancária.

    Atributos:
    ----------
    _transacoes: list[dict]
        lista que armazena todas as transações

    Métodos:
    --------
    @property
    transacoes(): list[dict]
        retorna o atributo transações

    @staticmethod
    horario_atual_UTC(): str
        retorna uma string do horário atual baseado no horário padrão global
    
    adicionar_transacao(transacao, valor: float): None
        adiciona uma nova transação a lista de transacoes
    """

    def __init__(self):
        self._transacoes: list[dict] = []

    @property
    def transacoes(self) -> list[dict]:
        return self._transacoes
    
    @staticmethod
    def horario_atual_UTC() -> str:
        "Retorna o horário atual UTC"
        return datetime.now(UTC).strftime('%d/%m/%Y %H:%M:%S')
    
    def adicionar_transacao(self, transacao, valor: float) -> None:
        """
        Adiciona uma nova transação ao histórico
        
        Parâmetros:
        -----------
            transacao
                função chamada na hora da transação

            valor: float
                valor da transação
        """

        self._transacoes.append({
            "tipo": transacao.__name__,
            "valor": valor,
            "data": self.horario_atual_UTC()
        })
    
    def __iter__(self):
        "Itera sobre as transações"
        for t in self._transacoes:
            texto = f"""
                {'---------------------------'.center(33)}
                Tipo:\t{t['tipo'].title()}
                Valor:\tR${t['valor']:.2f}
                Data:\t{t['data']}
                {'---------------------------'.center(33)}
            """

            yield cleandoc(texto)

    def __len__(self) -> int:
        "Retorna o número de transações"
        return len(self._transacoes)

class Conta:
    """
    Classe que representa uma conta bancária.

    Atributos:
    ----------
    _cliente: Cliente (class)
        objeto da classe Cliente

    _numero: int
        número da conta

    _saldo: float
        saldo da conta

    _historico: Historico (class)
        historico de transações da conta
    
    Métodos:
    --------
    @classmethod
    listar_contas(): None
        lista todas as contas já cadastradas

    @classmethod
    numero_de_contas(): int
        retorna o número de contas já cadastradas

    @property
    saldo(): float
        retorna o saldo da conta

    sacar(valor: float): bool
        método que retira saldo da conta

    deposito(valor: float): bool
        método que adiciona saldo a conta

    mostrar_extrato(): bool
        método que mostra o saldo da conta
    """

    contas = []

    def __init__(self, cliente: Cliente):
        """
        Valores necessários para o Constructor da Conta.

        Parâmetros:
        -----------
            cliente: Cliente
                objeto da classe Cliente
        """

        self._cliente = cliente
        self._numero: int = len(Conta.contas) + 1
        self._saldo: float = 0.0
        self._historico = Historico()

        Conta.contas.append(self)

    @classmethod
    def listar_contas(cls) -> None:
        "Lista todos os objetos pertencentes a classe Conta"
        for conta in cls.contas:
            print('---------------------------'.center(60))
            print(conta)
            print('---------------------------'.center(60))

    @classmethod
    def numero_de_contas(cls) -> int:
        "Retorna o número de contas cadastradas"
        return len(cls.contas)

    @property
    def saldo(self) -> float:
        return self._saldo

    def sacar(self, valor: float) -> bool:
        """
        Diminui saldo da conta
        
        Retorna falso caso:
        - Valor seja negativo;
        - Valor seja maior do que saldo da conta.
        """
        if valor <= 0:
            print("=== Valor inválido ===")
            return False

        if (self._saldo - valor) < 0:
            print("=== Saldo insuficiente ===")
            return False
        
        self._saldo -= valor
        self._historico.adicionar_transacao(self.sacar, valor)
        return True

    def deposito(self, valor: float) -> bool:
        """
        Incrementa saldo da conta

        Retorna falso caso:
        - Valor de depósito seja negativo.
        """
        if valor <= 0:
            print("=== Valor inválido ===")
            return False
        
        self._saldo += valor
        self._historico.adicionar_transacao(self.deposito, valor)
        return True

    def mostrar_extrato(self) -> bool:
        "Mostra histórico de transações da conta"
        if not len(self._historico):
            print("=== Nenhuma transação adicionada ===")
            return False

        print("======= TRANSAÇÕES =======".center(33))
        for t in self._historico:
            print(t)
        print(f"\nSaldo atual: R${self._saldo:.2f}")
        
        return True

    def __eq__(self, outra) -> bool:
        "Verifica se saldo de duas contas são iguais"
        if not isinstance(outra, Conta):
            raise NotImplemented

        return self._saldo == outra._saldo
    
    def __lt__(self, outra) -> bool:
        "Verifica se saldo da conta é menor que saldo de outra"
        if not isinstance(outra, Conta):
            raise NotImplemented

        return self._saldo < outra._saldo
    
    def __gt__(self, outra) -> bool:
        "Verifica se saldo da conta é maior que saldo de outra"
        if not isinstance(outra, Conta):
            raise NotImplemented

        return self._saldo > outra._saldo

    def __str__(self) -> str:
        return cleandoc(f"""
            Nome:\t\t\t{self._cliente.nome}
            Conta Nº:\t\t\t{self._numero}
            Saldo:\t\t\tR${self._saldo:.2f}
            Número de transações:\t{len(self._historico)}
        """)
    
    def __repr__(self) -> str:
        return f"nome={self._cliente.nome} | numero={self._numero} | saldo={self._saldo}"

if __name__ == "__main__":
    cliente1 = Cliente("Carlos Eduardo Lima de Sousa")
    cliente2 = Cliente("Miguel Ângelo Lima de Sousa")

    conta1 = Conta(cliente1)
    conta2 = Conta(cliente2)
    conta3 = Conta(cliente2)
    
    conta1.deposito(500)
    conta1.sacar(250)

    conta2.deposito(100)
    conta2.sacar(50)
    conta2.sacar(25)

    conta3.deposito(500)
    conta3.sacar(100)

    Conta.listar_contas()
