"""
Tipo String
"""
nome = 'Gustavo Ribeiro'
print(nome.split())  # transforma em uma lista de strings

# Também posso acessar a lista da string e retornar somente os caracteres que desejo
# Slice de string é o nome das operações abaixo

print(nome[0:7])  # para retornar da 1ª a 7ª letra (a priemira é representada por zero e o corte ocorre no 7)
print(nome[8:16])  # o ultimo numero do colchetes não é incluido

# Usando o split, a string ocupa uma posição na lista

print(nome.split()[0])

# Inverter a string
# Começamos no primeiro elemento, terminamos no último e -1 para inverter
print(nome[::-1])

# Substituir uma letra por outra
print(nome.replace('o', 'x'))

# Palíndromo
palindromo = 'socorram me subino onibus em marrocos'

print(palindromo)
print(palindromo[::-1])
