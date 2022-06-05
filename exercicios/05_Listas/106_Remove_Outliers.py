lista_original = input('Digite uma lista de valores: ')
lista_original = lista_original.split(',')

i = 0

while i < len(lista_original):
    lista_original[i] = int(lista_original[i])
    i += 1

lista_nova = lista_original.copy()

if len(lista_original) < 4:
    print('Erro! Quantidade de números insuficiente')
else:
    lista_nova.sort()
    for j in range(2):
        lista_nova.pop(len(lista_nova) - 1)
        lista_nova.pop(0)
    print(lista_original)
    print(lista_nova)
