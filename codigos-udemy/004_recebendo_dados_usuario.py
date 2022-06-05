"""
Recebendo dados do usuário

Todo dado recebido via input() é do tipo String

Em Python, string é dudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas.
"""
# 1 - Forma Moderna
"""
# Entrada de dados
print("Qual seu nome?")
nome = input()

# Processamento
nome = nome.title()
print('Seja bem vindo(a) {0}'.format(nome))
print('Qual a sua idade?')

idade = input()

# Saida de dados
print('O {0} tem {1} anos'.format(nome, idade))
"""

# 2 Forma Antiga
"""
# Entrada de dados
print("Qual seu nome?")
nome = input()

# Processamento
nome = nome.title()
print('Seja bem vindo(a) %s' % nome)
print('Qual a sua idade?')

idade = input()

# Saida de dados
print('O %s tem %s anos' %(nome, idade))
"""

# 3 Forma atual

# Entrada de dados

# print("Qual seu nome?")
# nome = input()
nome = input('Qual seu nome? ')  # dá pra simplificar em 1 linha

# Processamento
nome = nome.title()
print(f'Seja bem vindo(a) {nome}')

idade = input('Qual sua idade? ')

# Saida de dados
print(f'O {nome} tem {idade} anos')
print(f'O {nome} nasceu em {2020-int(idade)}')
