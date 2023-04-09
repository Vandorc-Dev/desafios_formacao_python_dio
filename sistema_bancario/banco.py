menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informa o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.f2}\n"

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente")
        elif excedeu_limite: 
            print("Operação falhou! Você não tem limite de saque")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques exceido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.f2}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n============EXTRATO============")
        print("Não foram realizado movimentações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor selecione uma opção válida.")