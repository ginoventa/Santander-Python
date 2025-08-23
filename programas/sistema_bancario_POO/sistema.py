import textwrap


def menu():
    menu = """\n
    ================ MENU BANCÁRIO ================
    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Cliente
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo_atual, valor, historico, /):
    if valor > 0:
        saldo_atual += valor
        historico += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Valor de depósito inválido. @@@")

    return saldo_atual, historico


def sacar(*, saldo_atual, valor, historico, limite, saques_realizados, limite_saques):
    excedeu_saldo = valor > saldo_atual
    excedeu_limite = valor > limite
    excedeu_saques = saques_realizados >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Saldo insuficiente.")

    elif excedeu_limite:
        print("\nperação falhou! Valor do saque excede o limite permitido.")

    elif excedeu_saques:
        print("\nOperação falhou! Limite diário de saques atingido.")

    elif valor > 0:
        saldo_atual -= valor
        historico += f"Saque:\t\tR$ {valor:.2f}\n"
        saques_realizados += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! Valor de saque inválido. @@@")

    return saldo_atual, historico


def exibir_extrato(saldo_atual, /, *, historico):
    print("\n================ EXTRATO BANCÁRIO ================" )
    print("Nenhuma movimentação registrada." if not historico else historico)
    print(f"\nSaldo atual:\tR$ {saldo_atual:.2f}")
    print("=================================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (apenas números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Cliente cadastrado com sucesso! ===")


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do titular: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n=== Conta bancária criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\n@@@ Cliente não encontrado. Criação de conta cancelada! @@@")


def listar_contas(contas_bancarias):
    for conta in contas_bancarias:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 80)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo_atual = 0
    limite = 500
    historico = ""
    saques_realizados = 0
    clientes = []
    contas_bancarias = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo_atual, historico = depositar(saldo_atual, valor, historico)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo_atual, historico = sacar(
                saldo_atual=saldo_atual,
                valor=valor,
                historico=historico,
                limite=limite,
                saques_realizados=saques_realizados,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo_atual, historico=historico)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas_bancarias) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas_bancarias.append(conta)

        elif opcao == "lc":
            listar_contas(contas_bancarias)

        elif opcao == "q":
            print("Saindo do sistema bancário. Até logo!")
            break

        else:
            print("Operação inválida. Por favor, selecione uma opção válida.")

main()