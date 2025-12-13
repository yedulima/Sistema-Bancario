LIMITE_SAQUES_DIARIOS: int = 3
saques_realizados: int = 0
extratos: list[float] = []
saldo: float = 0.0

# === Funções ===
def sacar(valor: float) -> None:
    global saques_realizados, saldo

    if saques_realizados == LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diários excedidos")
        return
    
    if valor < 0 or valor > 500:
        print("O valor para saque deve estar entre 1 e 500.")
        return

    if (saldo - valor) < 0:
        print("Não será possível sacar o dinheiro por falta de saldo.")
        return
    
    saques_realizados += 1
    saldo -= valor
    extratos.append(f"[SAQUE] R${valor:.2f}")

def deposito(valor: float) -> None:
    global saldo

    if valor <= 0:
        print("Insira um valor válido para depósito.")
        return
    
    saldo += valor
    extratos.append(f"[DEPÓSITO] R${valor:.2f}")

def extrato() -> None:
    global extratos

    print("Extratos bancários".center(30, "-"))
    print(f"Saldo da conta: R${saldo:.2f}\n")
    for e in extratos:
        print(e)

# === Funcionamento do sistema ===
deposito(100)
sacar(50)
extrato()
