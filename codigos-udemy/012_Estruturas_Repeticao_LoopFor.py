"""
Loop for

Loop é uma estrutura de repetição.
For é uma dessas estruturas

for item in intervalo:
    //execução loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis (Strings, Listas, Ranges)
"""

nome = 'Geek University'

for letra in nome:
    print(letra)

# Enumerate: ((0, 'G'), (1, 'e'), (2,'e'),(3, 'k'), ... ) --> Cria uma Tupla, retorna índice e letra
for i, v in enumerate(nome):
    print(nome[i])

# Se não quiser exibir um valor, há um recurso no python --> underline '_'
for _, v in enumerate(nome):
    print(v)

for valor in enumerate(nome):
    print(valor)

qtde = 5
soma = 0
for n in range(1, qtde + 1):
    soma = soma + n
print(f'A soma das iterações é {soma} --> {n}')

# Para printar na mesma linha --> por default, python insere o \n no print

print(nome, end='')

# Python faz multiplicação de String

nome = 'Guga'
print(f'\n{nome * 3}')

# Imprimindo Emojis - https://apps.timwhitlock.info/emoji/tables/unicode
# Original -- U+1F602
# Modificado -- U0001F602 -- Substitui o '+' por '000' (3 zeros)

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F602' * num)  # A barra é um caracter de escape... ignora o caracter anterior


