"""
Dicionarios

OBS: e algumas linguagens de programacao, Dicionarios sao conhecidos como mapas.
Dicionarios sao colecoes do tipo chave/valor

Dicionarios sao representados por chaves {}

    print(type({}))

- Chave e valor sao separados por dois pontos

    paises = {'bra': 'Brasil', 'arg': 'Argentina', 'chi': 'Chile'}
    print(paises)

- Tanto chave quanto valor podem ser de qualquer tipo de dado
- Podemos misturar tipos de dados

# Criacao de dicionarios

# Forma 1 (mais comum)

paises = {'bra': 'Brasil', 'arg': 'Argentina', 'chi': 'Chile'}
print(paises)

# Forma 2 (menos comum)

paises_2 = dict(bra='Brasil', arg='Argentina', chi='Chile')
print(paises_2)

# Acessando elementos

paises = {'bra': 'Brasil', 'arg': 'Argentina', 'chi': 'Chile'}

# Forma 1 - acessando via chave entre colchetes

print(paises['bra'])
print(paises['col'])  # Se a chave nao existir, ocorre keyError

# Forma 2 - acessando via get (forma recomendada)

print(paises.get('bra'))
print(paises.get('col'))  # Usando get, nao da KeyError, eh exibido um 'None'

# O tipo de dado 'None' representa o tipo de dado sem tipo

nenhum = None  # especificado sempre com a primeira letra maiuscula
print(nenhum)

# Podemos utilizar None quando queremos iniciar uma variavel mas nao sabemos ainda o seu tipo final
# O tipo None em Python eh sempre considerado como False

    if None:
        print('verdade')
    else:
        print('falso')

# Eh possivel especificar um valor para o caso de nao encontrar a chave com get

# Eh possivel especificar um valor para o caso de nao encontrar a chave com get

paises = {'bra': 'Brasil', 'arg': 'Argentina', 'chi': 'Chile'}
pais = paises.get('col', 'Nao encontrado')
print(pais)

# Eh verificar se uma chave existe no dicionario

paises = {'bra': 'Brasil', 'arg': 'Argentina', 'chi': 'Chile'}
print('bra' in paises)
print('col' in paises)
print('Argentina' in paises) # observe que esse valor existe no dict, mas nao eh chave, eh valor

# Eh interessante utilizar tuplas como chaves de dicionarios, por serem imutaveis

# Adicionar elementos em dicionarios

paises = {'bra': 'Brasil', 'arg': 'Argentina', 'chi': 'Chile'}
print(paises)

# Forma 1

paises['col'] = 'Colombia'  # este caso serve para atualizar o dado de um item do dicionario caso a chave exista
print(paises)

# Forma 2

novo_pais = {'Urg': 'Uruguai'}
paises.update(novo_pais)
print(paises)

# Em dicionarios nao podemos ter chaves repetidas

# Remover dados de um dicionario

# Forma 1
paises = {'bra': 'Brasil', 'arg': 'Argentina', 'chi': 'Chile'}
print(paises)

removido = paises.pop('chi')  # obrigatorio usar a chave, se nao for encontrada, ocorre KeyError
print(removido)  # alem disso, ao remover uma chave seu valor sempre eh retornado
print(paises)

# Forma 2

del paises['arg']  # nesse caso o valor nao eh retornado
print(paises)

# Metodos de Dicionarios

paises = {'bra': 'Brasil', 'arg': 'Argentina', 'chi': 'Chile'}
print(paises)

# Limpar o dicionario

paises.clear()
print(paises)

# Copiando um dicionario para outro

# Forma 1 (deep copy)

copia = paises.copy()
copia['col'] = 'Colombia'
print(paises)
print(copia)

# Forma 2 (shallow copy)

copia_2 = paises
copia_2['urg'] = 'Uruguai'
print(paises)
print(copia_2)
"""
