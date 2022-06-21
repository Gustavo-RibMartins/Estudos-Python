"""
Mapas --> conhecidos em Python como Dicionarios

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# Iterar sobre Dicionarios

for chave in receita:  # a forma pythonica seria: for chave in receita.keys() nessa linha
    print(chave)

for chave in receita:
    print(receita[chave])

# Acessando as chaves e os valores

print(receita.keys())    # chaves
print(receita.values())  # valores

# Desempacotando itens do dicionario

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave={chave} : Valor={valor}')

# Metricas de agregacao de dicionarios

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))
"""
