from time import sleep


dados = {
    "saldo": 0,
    "lista_saldo": [],
    "historico": {
        "saques": [],
        "depositos": []
    }
}

def tela_inicial():
    print("\n* SEJA BEM-VINDO AO BANCO WEILER *")
    print("""
[D] = Depósito 
[S] = Saque
[E] = Extrato
[L] = SAIR
""")
    acao = input("O que iremos fazer? ").upper()
    sleep(0.3)
    return acao

def deposito(dados):
    print("* Depósito *")
    valor = float(input("Valor do depósito (R$): "))
    dados["saldo"] += valor
    dados["lista_saldo"].append(valor)
    dados["historico"]["depositos"].append(valor)
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    print(f"Saldo atual: R${dados['saldo']:.2f}")

def saque(dados):
    print("* Saque *")
    if dados["saldo"] <= 0:
        print("Saldo insuficiente. Faça um depósito primeiro.")
    else:
        valor = float(input("Quanto deseja sacar? R$"))
        if valor > dados["saldo"]:
            print("Saldo insuficiente para realizar o saque.")
        else:
            dados["saldo"] -= valor
            dados["lista_saldo"].append(-valor)
            dados["historico"]["saques"].append(valor)
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            print(f"Saldo atual: R${dados['saldo']:.2f}")

def extrato(dados):
    print("* Extrato *")
    print(f"Saldo atual: R${dados['saldo']:.2f}")
    print("Histórico de transações:")
    for tipo, valores in dados["historico"].items():
        print(f"{tipo.capitalize()}: {', '.join(f'R${v:.2f}' for v in valores)}")
    print("Lista de saldo:", dados["lista_saldo"])

def sair():
    print("Programa finalizado. Obrigado por usar o Banco Weiler!")
    exit()

# Programa principal
while True:
    acao = tela_inicial()

    if acao == "D":
        deposito(dados)
    elif acao == "S":
        saque(dados)
    elif acao == "E":
        extrato(dados)
    elif acao == "L":
        sair()
    else:
        print("Opção inválida. Tente novamente.")