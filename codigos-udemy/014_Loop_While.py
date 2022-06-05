"""
Loop while

Forma geral

while expressão-booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso
"""
# Ex1
numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# Ex2
resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou, Gustavo? ')
