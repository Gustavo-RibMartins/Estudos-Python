"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas:
1 - Tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis; Isso significa que ao se criar uma tupla, ela nõa muda.
Toda opearação em uma tupla, gera uma nova tupla

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))
print(tupla1)

tupla2 = 1, 2, 3, 4, 5, 6
print(type(tupla2))
print(tupla2)

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla, é um int
print(tupla3)
print(type(tupla3))

tupla4 = 4,  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

# Conclusão: podemos concluir que tuplas são definidas pela vírgula, e não pelo uso do parênteses

# Posso usar o range(inicio,fim,passo) para gerar uma tupla
tupla = tuple(range(0, 11, 2))
print(tupla)

# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla

print(escola)
print(curso)
#OBS.: Gera value error se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem dado o fato das tuplas serem imutáveis

# Soma, Valor máximo, Valor mínimo e Tamanho --> Se os valores forem todos reais, exceto o len()

tupla = 1, 2, 3, 4, 5, 6
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)
print(tupla1 + tupla2)

# Tuplas são imutáveis, mas podemos sobrescrever seus valores

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla1 = tupla1 + tupla2
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)
print(33 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))
print(tupla.count('c'))

escola = tuple('Geek University')  # Converti uma string em tupla
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificando em qual índice um elemento está na tupla

print(meses.index('Junho'))
'''print(meses.index('Playstation'))'''
# OBS.: Caso o elemento não exista, será gerado erro

# Slicing

print(meses[0::2])

# Por quê utilizar tuplas?

# 1 - Tuplas são mais rápidas do que listas
# 2 - Tuplas deixam seu código mais seguro (são imutáveis)

# Trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow Copy
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla)
"""
