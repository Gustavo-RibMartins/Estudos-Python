entrada = ''
lista = []

while entrada != ' ':
    entrada = input('Digite um texto ou "espaço" para sair: ')
    lista.append(entrada)

lista_nova = []

for i in range(len(lista)):
    if lista[i] not in lista_nova:
        lista_nova.append(lista[i])

for j in range(len(lista_nova)):
    print(lista_nova[j])
