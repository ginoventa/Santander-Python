LIMITE = 500
saques = 3 
saldo = 0.0 
movimentações = []

menu = """
[1] Saque 
[2] Depósito
[3] Extrato
[4] Sair
"""

print("Seja bem vindo ao Banco DIO. Selecione uma opção para continuar!")

def saque(): 
    global saldo, saques, movimentações
    if saques > 0: 
        try:
            valor = float(input("Quanto deseja sacar? R$ "))
            if valor <= 0:
                print('Valor deve ser positivo!')
            elif valor > LIMITE:
                print(f'Valor excede o limite de saque de R$ {LIMITE}!')
            elif valor > saldo:
                print('Saldo insuficiente!')
            else:
                print('Saque realizado com sucesso!')
                saldo = saldo - valor
                saques = saques - 1
                movimentações.append(f"Saque - R$ {valor:.2f}")
        except ValueError:
            print('Valor inválido! Digite apenas números.')
    else: 
        print('Número máximo de saques diários excedido!')
def deposito(): 
    global saldo, movimentações
    try:
        deposito = float(input("Quantos reais deseja depositar? R$ "))
        if deposito > 0:
            saldo = saldo + deposito
            movimentações.append(f"Depósito - R$ {deposito:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor de depósito deve ser positivo!")
    except ValueError:
        print('Valor inválido! Digite apenas números.')
def extrato():
    global saldo, saques, movimentações 
    print("\n EXTRATO ")
    if movimentações:
        for movimentacao in movimentações:
            print(movimentacao)
    else:
        print("Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Saques restantes: {saques}")
        print("=============================\n")
def sair(): 
    print("Obrigado por usar o Banco DIO!")

def main(): 
    while True:
        print(menu)
        opcao = input('Digite opção desejada: ')
        
        if opcao not in ['1','2','3','4']:
            print("Escolha uma opção válida!")
        elif opcao == '1': 
            saque()
        elif opcao == '2': 
            deposito()
        elif opcao == '3': 
            extrato()
        elif opcao == '4':
            sair()
            break

main()
