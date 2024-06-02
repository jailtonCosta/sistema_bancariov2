def menu ():
    menu = """====== Menu de Opções ===== :

    [1] \tDepositar
    [2] \tSacar
    [3] \tExtrato
    [4] \tSair
    
    Digite sua opção : => """
    return input(menu)

def depositar(saldo,valor, extrato , /):
    if saldo  > 0:
        saldo += valor
        extrato += f"Deposito :\t R${saldo:.2f} \n"
        print("\n===Deposito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou ! O valor informado é invalido !@@@")

    return saldo, extrato
def sacar (*, saldo, valor, extrato,limite, numero_saques, limite_saques):


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = []
    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "3":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "4":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()