menu = """
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair

>>>"""

LIMITE_SAQUES = 3
MAXIMO_SAQUE = 500.0
saques = 0
saldo = 0.0
extrato = []
        
def opcaoValida(opcao):
    global saques
    global saldo
    
    if opcao == "S" and saldo == 0:
        print("Você não possui saldo em conta!")
        return False
    elif opcao == "S" and saques == LIMITE_SAQUES:
        print("Você atingiu o limite diário de saques!")
        return False
    else:
        return True
    
def depositar():
    global saldo
    global extrato
    
    valor = float(input("Digite o valor do depósito: "))
    
    while valor < 0:
        print("Não é possível depositar  um valor negativo!")
        valor = float(input("Digite o valor do depósito: "))
        
    saldo += valor
    
    extrato.append(f"Depósito de R${valor: .2f}")
    

def sacar():
    global saques
    global saldo
    global extrato
    
    valor = float(input("Digite o valor do saque: "))
        
    while valor > saldo or valor > MAXIMO_SAQUE or valor < 0:
        if valor > saldo:
            print(f"Saldo insuficiente! (Saldo atual: {saldo})")
        elif valor > MAXIMO_SAQUE or valor < 0:
            print(f"O valor do saque deve ser menor que R${MAXIMO_SAQUE} e maior que zero!")
            
        valor = float(input("Digite o valor do saque: "))
        
    saques += 1
    
    saldo -= valor
    
    extrato.append(f"Saque de R${valor: .2f}")
        

def imprimirExtrato():
    global saldo
    global extrato
    
    if not extrato:
        print("Não foram realizadas movimentações!")
        return
    
    print("EXTRATO".center(30, "-"))
    
    impressao = "\n".join(item for item in extrato)
    print(impressao)
    print(f"\nSaldo da conta: {saldo}")
    print("-".center(30, "-"))
    

while True:
    opcao = input(menu)
    opcao = opcao.upper()
    
    if opcao == "D":
        depositar()
    elif opcao == "S":
        if opcaoValida(opcao):
            sacar()
    elif opcao == "E":
        imprimirExtrato()
    elif opcao == "Q":
        break
    else:
        print("Digite uma opção válida!")