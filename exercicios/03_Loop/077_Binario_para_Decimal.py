binario = input("Digite um numero binario: ")
decimal = 0

for digito in range(len(binario)):
    decimal = decimal + int(binario[digito]) * (2 ** digito)
print(decimal)
