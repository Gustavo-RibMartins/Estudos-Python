"""
- Os conjuntos em python sao chamados de Sets

- Sets (conjuntos) nao possuem valores duplicados ou ordenados

- Elementos nao sao acessados via indice (sets nao sao indexados)

- Conjuntos sao bons para se utilizar quando precisamos armazenar elementos mas nao nos importamos
com a ordenacao deles, quando nao precisamos nos preocupar com chaves ou valores duplicados

- Os conjuntos sao referencias em python con {}

- Diferenca entre conjuntos (Sets) e Mapas (Dicionarios):
    * Dicionario tem chave/valor
    * Um conjunto tem apenas valor
"""

# Definindo um conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

print(s)
print(type(s))
