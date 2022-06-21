numero = int(input("Digite um número inteiro:"))
lista = []

while numero != 0:
    lista.append(numero)
    numero = int(input('Digite outro número: '))

lista.sort()
lista = lista[::-1]

for elemento in range(len(lista)):
    print(lista[elemento])
