###
# atividade estacionamento
# Aluno: Caio Schaedler
# data 14/06/2024
###
# Dicionário para armazenar os veículos estacionados
estacionamento = {}

# Função para adicionar um veículo ao estacionamento
def estacionar_veiculo():
    placa = input("Digite a placa do veículo: ").upper()
    if placa in estacionamento:
        print("O veículo já está estacionado.")
        return
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    cor = input("Digite a cor do veículo: ")
    proprietario = input("Digite o nome do proprietário do veículo: ")
    veiculo = {"marca": marca, "modelo": modelo, "cor": cor, "proprietario": proprietario}
    estacionamento[placa] = veiculo
    print("O veículo foi estacionado com sucesso")

# Função para remover um veículo do estacionamento
def retirar_veiculo():
    placa = input("Digite a placa do veículo: ").upper()
    if placa not in estacionamento:
        print("O veículo não está estacionado")
        return
    del estacionamento[placa]
    print("O veículo foi retirado do estacionamento")

# Função para listar os veículos estacionados
def listar_veiculos_estacionados():
    if not estacionamento:
        print("Não há veículos estacionados")
        return
    print("Lista de veículos estacionados:")
    for placa, veiculo in estacionamento.items():
        print(f"Placa: {placa}")
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Cor: {veiculo['cor']}")
        print(f"Proprietário: {veiculo['proprietario']}")
        print()

# Estacionar um carro por padrão
estacionamento["ABC1234"] = {
    "marca": "Chevrolet",
    "modelo": "Chevette",
    "cor": "Rosa da Barbie",
    "proprietario": "Caio Schaedler"
}

# Função para verificar se um veículo está estacionado
def esta_estacionado():
    placa = input("Digite a placa do veículo: ").upper()
    if placa in estacionamento:
        print("Sim o veículo está estacionado ")
    else:
        print("Não o veículo não está estacionado")

# Loop principal do menu
while True:
    print("1 - Estacionar veículo")
    print("2 - Retirar veículo")
    print("3 - Veículos estacionados")
    print("4 - Está estacionado?")
    print("0 - Sair")
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida Tente novamente")
        continue

    if opcao == 1:
        estacionar_veiculo()
    elif opcao == 2:
        retirar_veiculo()
    elif opcao == 3:
        listar_veiculos_estacionados()
    elif opcao == 4:
        esta_estacionado()
    elif opcao == 0:
        print("Obrigado por utilizar nosso estacionamento.")
        break
    else:
        print("Opção inválida Tente novamente")
