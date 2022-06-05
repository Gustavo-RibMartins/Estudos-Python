"""
Tipo float ou real ou decimal

Com casas decimais são delimitadas por "ponto" e não por "vírgula"
A vírgula é usada para declarar Tuplas
"""

# 1 - Podemos fazer dupla atribuição

num1, num2 = 1.1, 0.9
print(num1+num2)

# 2 - Ao converter valores float para inteiro perdemos precisão (há truncamento do float)

num3 = int(num2)
print(num3)

# 3 - Podemos trabalhar com números complexos --> representados pela letra 'j'

complexo1, complexo2 = 3 + 4j, 2 + 1j
print(complexo1+complexo2)
