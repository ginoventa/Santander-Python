'''opcao = int(input("1 - Sacar 2 - Depositar 3 - Tela inicial" ))


while opcao != 3: 
    if opcao == 1: 
        print("Sacando...")
        break
    else:
        print("Depositando...")
        break

while opcao != 3: 
    if opcao == 1: 
        print("Sacando...")
        break
    else:
        print("Depositando...")
        break
else: 
    print("Saindo...")'''

i = 0
n = 0
while i < 5:
  i = 1 + i
  if i == 3:
    continue
  n += i
  print(i)
