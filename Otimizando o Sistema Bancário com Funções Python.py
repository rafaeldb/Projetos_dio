from typing import TypedDict, Literal, List, Tuple, Optional
import datetime

Usuario = TypedDict("Usuario", {
    "nome": str,
    "cpf": int,
    "data_de_nascimento": datetime.date,
    "endereço": str,
})

Conta = TypedDict("Conta", {
    "agencia": Literal["0001"],
    "numero_da_conta": int,
    "usuario": Usuario,
})

def achar_cpf(usuarios: List[Usuario], cpf: int) -> Optional[int]:
    """Verifica se o CPF já existe."""
    for idx, u in enumerate(usuarios):
        if u["cpf"] == cpf:
            return idx
    return None

def receber_cpf(usuarios: List[Usuario]) -> int:
    while True:
        try:
            cpf = int(input("Digite o CPF:\n"))
            if achar_cpf(usuarios, cpf) is not None:
                print("Já existe uma conta com esse CPF.")
            else:
                return cpf
        except ValueError:
            print("CPF inválido, por favor insira um número válido.")

def novo_usuario(usuarios: List[Usuario]) -> None:
    cpf = receber_cpf(usuarios)
    nome = input("Digite o nome: \n")

    while True:
        try:
            data_str = input("Digite a data de nascimento (AAAA-MM-DD): \n")
            data_de_nascimento = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Data de nascimento no formato incorreto.")

    logradouro = input("Digite o logradouro: \n")
    bairro = input("Digite o bairro: \n")
    cidade = input("Digite a cidade/sigla estado: \n")

    endereco = f"{logradouro}, {bairro}, {cidade}"
    usuarios.append({
        "cpf": cpf,
        "data_de_nascimento": data_de_nascimento,
        "endereço": endereco,
        "nome": nome,
    })

    print("Usuário foi criado!")

def nova_conta(agencia: Literal["0001"], numero_conta: int, usuarios: List[Usuario]) -> Optional[Conta]:
    cpf = int(input("Digite o CPF:\n"))
    usuario_index = achar_cpf(usuarios, cpf)

    if usuario_index is not None:
        usuario = usuarios[usuario_index]
        print("Conta foi criada!")
        return {"agencia": agencia, "numero_da_conta": numero_conta, "usuario": usuario}

    print("Conta não foi criada.")
    return None

def sacar(valor: float, saldo: float, extrato: str, limite: float, numero_saques: int, limite_saques: int) -> Tuple[float, str]:
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato

def depositar(saldo: float, valor: float, extrato: str) -> Tuple[float, str]:
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def visualizar_historico(saldo: float, extrato: str) -> None:
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def listar_contas(contas: List[Conta]) -> None:
    if not contas:
        print("Nenhuma conta encontrada.")
    for conta in contas:
        print(conta)

def main() -> None:
    menu = """
----------------------------------
    | [d] Depositar              |
    | [s] Sacar                  |
    | [e] Extrato                |
    | [nc] Criar conta           |
    | [nu] Criar usuário         |
    | [ls] Listar contas         |
    | [q] Sair                   |
----------------------------------\n"""

    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios: List[Usuario] = []
    contas: List[Conta] = []

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            visualizar_historico(saldo, extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1  # Corrigido para contar a partir de 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "nu":
            novo_usuario(usuarios)

        elif opcao == "ls":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
