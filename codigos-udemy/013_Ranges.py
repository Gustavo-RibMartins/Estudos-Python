"""
Ranges são utilizados para gerar sequências numéricas não de forma aleatória
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)
OBS: valor de parada "não inclusive" (início padrão em zero e passo de 1 em 1)

# Forma 2

range(valor_de_inicio, valor_de_parada)
OBS: valor_de_inicio é "inclusive"

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)

# Forma 4 ( igual a #3 mas inversa)
range(valor_de_inicio, valor_de_parada, passo)
"""
# Forma 1

for num in range(11):
    print(num)

# Forma 2

for num in range(1, 11):
    print(num)

# Forma 3

for num in range(1, 10, 2):
    print(num)

# Forma 4
for num in range(10, 0, -1):
    print(num)
