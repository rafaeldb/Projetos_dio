def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    menu = """
    -----------------------------------------
    |               MENU                    |
    | "d" - Depósito                        |
    | "s" - Saque                           |
    | "e" - Extrato                         |
    | "q" - Sair                            |
    -----------------------------------------
    """
    print(menu)

def obter_valor(mensagem):
    """Obtém um valor de ponto flutuante do usuário com tratamento de erro e possibilidade de cancelar."""
    while True:
        valor_input = input(mensagem)
        if valor_input.lower() == 'c':
            return None  # Retorna None se o usuário quiser cancelar.

        try:
            valor = float(valor_input)
            if valor <= 0:
                print("Valor deve ser maior que zero. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

def realizar_saque(saldo, max_saque, extrato, quantidade_saques, max_saques):
    """Realiza a operação de saque, atualizando saldo e extrato."""
    print("--------------- SAQUE ---------------")
    val = obter_valor("Digite o valor a sacar ou 'c' para cancelar: R$ ")

    # Verifica se a operação foi cancelada
    if val is None:
        print("Operação de saque cancelada. Voltando ao menu principal.")
        return saldo, quantidade_saques, extrato

    if val > saldo:
        print(f"A operação não foi realizada. Saldo insuficiente! Saldo atual: R$ {saldo:.2f}. Tentativa: R$ {val:.2f}.")
    elif val > max_saque:
        print(f"O valor do saque deve ser menor que R$ {max_saque:.2f}. Tente novamente.")
    elif quantidade_saques >= max_saques:
        print(f"Saque recusado. Você já realizou {max_saques} saques hoje. Limite diário alcançado.")
    else:
        saldo -= val
        quantidade_saques += 1
        extrato += f"Saque: R$ {val:.2f}\n"
        print(f"Saque de R$ {val:.2f} realizado com sucesso! Total de saques hoje: {quantidade_saques} de {max_saques}.")

    print("-------------------------------------")
    return saldo, quantidade_saques, extrato

def realizar_deposito(saldo, extrato):
    """Realiza a operação de depósito, atualizando saldo e extrato."""
    print("++++++++++++ DEPOSITO ++++++++++++")
    val = obter_valor("Digite o valor a depositar ou 'c' para cancelar: R$ ")

    # Verifica se a operação foi cancelada
    if val is None:
        print("Operação de depósito cancelada. Voltando ao menu principal.")
        return saldo, extrato

    saldo += val
    extrato += f"Depósito: R$ {val:.2f}\n"
    print(f"Depósito de R$ {val:.2f} realizado com sucesso! Seu saldo atual é R$ {saldo:.2f}.")
    print("++++++++++++++++++++++++++++++++++")

    return saldo, extrato

def exibir_extrato(extrato, saldo):
    """Exibe o extrato e o saldo atual."""
    print("=============== EXTRATO ================")

    if not extrato:
        print("Nenhuma operação foi realizada até o momento.")
    else:
        print(extrato)

    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=========================================\n")

def main():
    """Função principal que executa o sistema de gerenciamento financeiro."""
    saldo = 0.0
    MAX_SAQUE = 500.0
    extrato = ""
    quantidade_saques = 0
    MAX_QUANTIDADE_SAQUES = 3

    while True:
        exibir_menu()  # Exibe o menu inicialmente
        comando = input("Escolha uma opção: ").strip().lower()

        if comando == "s":  # Saque
            saldo, quantidade_saques, extrato = realizar_saque(saldo, MAX_SAQUE, extrato, quantidade_saques, MAX_QUANTIDADE_SAQUES)

        elif comando == "d":  # Depósito
            saldo, extrato = realizar_deposito(saldo, extrato)

        elif comando == "e":  # Extrato
            exibir_extrato(extrato, saldo)

        elif comando == "q":  # Sair
            print("Você saiu do sistema. Até logo!")
            break

        else:
            print(f'Comando "{comando}" não é reconhecido. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()
