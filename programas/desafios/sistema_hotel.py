def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))


    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    confirmadas = []
    recusadas = []

    for quartos in reservas_solicitadas: 
        if quartos in quartos_disponiveis: 
            confirmadas.append(quartos)
        else: 
            recusadas.append(quartos)
    
    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()