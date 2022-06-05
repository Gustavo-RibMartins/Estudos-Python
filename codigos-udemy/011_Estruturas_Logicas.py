"""
Operadores unários: NOT --> Dependem apenas de um valor

Operadores Binários: AND, OR e IS -- Dependem de dois valores
"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo, Usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if not ativo:
    print('Verifique sua conta no seu e-mail')
else:
    print('Bem-vindo, Usuário!')

if ativo is True:
    print('Ativado')
