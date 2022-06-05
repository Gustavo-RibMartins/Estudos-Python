entrada = float(input("Digite um número: "))
iteracao = 0
soma = 0

if entrada == 0:
    print("Erro! Digite um número diferente de zero.")
else:
    while entrada != 0:
        soma = soma + entrada
        iteracao += 1
        entrada = float(input("Digite outro número: "))
    print(f'A média dos números é: {soma / iteracao :.2f}')
