"""# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
    desconto = descontos[cupom]
    preco_final = preco * (1 - desconto)
    print(f"{preco_final:.2f}")
else:
    print(f"{preco:.2f}")"""


# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
tamanho_email = len(email)

if email[0] == '@' or email[tamanho_email-1] == '@' or '@' not in email: 
    print("E-mail inválido")
else:
    print("E-mail válido")

