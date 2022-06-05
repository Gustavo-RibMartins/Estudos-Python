"""
Listas

listas em python funcionam como vetores/ matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado

- DINÂMICO: não possui tamanho fixo, criamos a lista e vamos adicionando elementos (enquanto houver memória
disponível, ele adiciona elementos --> podemos inserir valores repetidos);
- QUALQUER tipo: a lista não possui tipo de dado fixo;

As listas em Python são representadas por colchetes []
"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
cores = ['verde', 'amarelo', 'azul', 'branco']

# Podemos facilmente checar se determinado valor está contido na lista
"""
num = 8
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f"Não encontrei o número {num}")
"""
# Podemos facilmente ordenar uma lista com o método sort()
"""
lista1.sort()
print(lista1)
lista5.sort()
print(lista5)
"""
# Podemos facilmente contar o número de ocorrências de um valor em uma lista
"""
print(lista1.count(1))
print(lista5.count('e'))
"""
# Adicionar elementos em listas
""" 
Para adicionar elementos em listas, utilizamos a função append()
Obs.: Com append() só podemos adicionar um elemento por vez 

print(lista1)
lista1.append(100)
print(lista1)

# Erro - lista1.append(1, 2, 3) --> append() só recebe um argumento, mas podemos passar uma outra lista
lista1.append([101, 102, 103])  # colocando uma lista dentro de outra lista
print(lista1)
# extend() só aceita iteráveis: listas, strings
lista1.extend([104, 105, 106])  # Para adicionar os itens da lista, e não incluir a lista como algo único
print(lista1)
"""
# podemos inserir um novo elemento na lista informando a posição do índice
"""
lista1.insert(0, "primeiro")
print(lista1)
"""
# podemos facilmento juntar duas listas
"""
lista6 = lista1 + lista2  # faz a mesma coisa que o lista1.extend(lista2)
print(lista6)
"""
# imprimindo a lista na ordem inversa --> reverse()
"""
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
"""
# podemos reverter fazendo o slice de string
"""
print(lista2[::-1])
"""
# copiar uma lista --> copy()
"""
lista6 = lista2.copy()
print(lista6)
"""
# Para saber quantos elementos tem numa lista --> len()
"""
print(len(lista2))
"""
# podemos remover o último elemento de uma lista --> pop() --> além disso, retorna o último elemento
"""
print(lista5)
print(lista5.pop())
print(lista5)
"""
# podemos remover um item pelo índice --> removendo o índice 2
"""
print(lista5)
lista5.pop(2)
print(lista5)
"""
# Podemos remover todos os elementos --> clear()
"""
print(lista5)
lista5.clear()
print(lista5)
"""
# Podemos facilmente repetir elementos de uma lista
"""
lista4_2 = lista4 * 3
print(lista4)
print(lista4_2)
"""
# Podemos facilmente converter uma string para uma lista
"""
curso = "Prorgmação em Python Essencial"
print(curso)
curso = curso.split()  # por padrão, split() separa os elementos pelo espaço entre eles
print(curso)

curso2 = "Programação,em,Python,Essencial"
print(curso2)
curso2 = curso2.split(',')
print(curso2)

curso3 = ['Programação', 'em', 'Python', 'Essencial']
print(curso3)
curso3 = ' '.join(curso3)  # Pegue cada elemento, inclua espaço entre eles e transforme em string
print(curso3)
"""
# Podemos colocar qualquer tipo de dado em uma lista
"""
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 234723984237502984]
print(lista6)
"""
# iterando sobre listas - Exemplo 1 --> usando for
"""
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)
"""
# iterando sobre listas - Exemplo 2 --> usando while
"""
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""
# Utilizando variáveis em listas
"""
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)
"""
# Fazemos acesso aos elementos de forma indexada
"""
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # posição 0
print(cores[1])
print(cores[2])
print(cores[3])
"""
# Fazer acesso aos elementos de forma indexada inversa
"""
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1])  # acessa o último item
print(cores[-2])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1
"""
# Gerar indices em um for
"""
for indice, cor in enumerate(cores):
    print(indice, cor)
"""
# Outros métodos não tão importantes mas também úteis

# 1 - Encontrar o índice de um elemento na lista
"""
# Obs.: Caso não tenha esse elemento na lista, será apresentado erro
numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(6))  # em qual índice esta o valor 6?
# print(numeros.index(19))  # ValueError

numeros = [5, 6, 7, 5, 8, 9, 10]  # quando há valores repetidos, retorna o primeiro encontrado
print(numeros.index(5))
"""
# 2 - Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
"""
numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(5, 1))  # Começando no índice 1, procure o índice do elemento 5
"""
# 3 - Podemos fazer busca dentro de um range, inicio/ fim
"""
numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(8, 4, 6))  # buscar o índice do valor 8 entre os índices 4 a 6
"""
# Revisão de Slicing
"""
# lista[inicio:fim:passo]

# Trabalhando com slice de lista com o parametro "inicio"
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[1:])  # iniciando no índice 1 e trazendo o restante
# Trabalhando com slice de lista com o parâmetro "fim"
print(lista[1:3])  # iniciando no índice 1 e finalizando no índice 2 (o "fim" é excludente)
# Trabalhando com slice de lista com o parâmetro "passo"
print(lista[0:10:2])  # inica no índice 1, finaliza no 3 e pula de 2 em 2 indices
# Printando a lista na ordem inversa pulando de 2 em 2 indices
print(lista[-1::-2])
"""
# invertendo os valores em uma lista --> Sem utilizar o reverse()
"""
nome = ['Gustavo', 'Ribeiro']
print(nome)
nome[0], nome[1] = nome[1], nome[0]
print(nome)
"""
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho da lista
"""
# * - Se os valores forem numéricos

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # Soma
print(max(lista))  # Maximo
print(min(lista))  # Minimo
print(len(lista))  # Tamanho
"""
# Transformar umas lista em tupla
"""
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
"""
# Desenpacotamento de listas
"""
lista = [1, 2, 3]
num1, num2, num3 = lista
print(lista)
print(f'{num1} - {num2} - {num3}')

# OBS.: Se tivermos um número diferente de variáveis e elementos na lista teremos ValueError
"""
# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
"""
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista mas elas ficaram
# totalmente independentes, ou seja, modificando uma lista não afetamos a outra, isso em Python é
# chamado de Deep Copy (ou Cópia Profunda)
"""
# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(f'lista = {lista}')
print(f'nova = {nova}')

# Veja que utilizamos a copy via atribuição e copiamos os dados da lista para a nova lista, mas após
# realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas
# isso em Python é chamado de Shallow Copy
