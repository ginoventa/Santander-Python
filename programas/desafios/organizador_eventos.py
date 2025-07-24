# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()
    posicao_virgula = linha.rfind(", ")
    
    #Pega os nomes do input 
    participante = linha[:posicao_virgula]
    tema = linha[posicao_virgula + 2:]

    ##Verifica se o tema existe
    if tema not in eventos: 
        eventos[tema] = []

    #Adiciona participante à lista
    eventos[tema].append(participante) 

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")