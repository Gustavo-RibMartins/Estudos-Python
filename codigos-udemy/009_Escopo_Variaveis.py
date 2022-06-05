"""
Escopp de variaveis

Dois casos de escopo

1 - Variáveis globais --> são reconhecidas, ou seja, seu escopo compreende todo o programa

2 - Variáveis locais --> são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
está limitado ao bloco onde foi declarada

Python é uma linguagem de tipagem dinâmica, isso significa que ao declararmos uma variável, nós não
colocamos o tipo de dado dela. Esse tipo é inferido ao atribuirmos o valor à mesma
"""
numero = 11  # variavel global
print(numero)

if numero > 10:
    novo = numero + 10  # variavel local
    print(novo)

print(novo)  # não funcionara se numero <= 10
