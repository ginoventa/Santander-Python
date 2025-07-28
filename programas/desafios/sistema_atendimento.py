# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def prioridade(pacientes):
    urgente = []
    idosos_urgente = []
    idosos = [] 
    demais = []

    for paciente in pacientes:
        if paciente[2].lower() == "urgente" and paciente[1] >= 60:
            idosos_urgente.append(paciente)
        elif paciente[2].lower() == "urgente":
            urgente.append(paciente)
        elif paciente[1] >= 60: 
            idosos.append(paciente)
        else:
            demais.append(paciente)

    idosos_urgente = sorted(idosos_urgente, key=lambda x: x[1], reverse=True)
    return idosos_urgente + urgente + idosos + demais 

# TODO: Exiba a ordem de atendimento com título e vírgulas:
ordem = prioridade(pacientes)
print("Ordem de Atendimento: ", end="")
print(", ".join([p[0] for p in ordem]))