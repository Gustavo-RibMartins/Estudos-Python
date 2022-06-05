posicao = input('Digite a casa do tabuleiro: ')

linha = int(posicao[1])

if posicao.upper()[0] in ('A', 'C', 'E', 'G'):
    coluna = 1
else:
    coluna = 0

if (linha + coluna) % 2 == 0:
    print('Casa preta')
else:
    print('Casa branca')
