"""
A máquina deve retornar a quantidade de notas que devem ser entregues ao usuário
A máquina só possui notas de 2 e 5 reais e moedas de 1 real
"""
saque = int(input('Qual o valor que deseja sacar?\n'))
notas5 = saque // 5
notas2 = (saque - notas5 * 5) // 2
moedas = saque - notas5 * 5 - notas2 * 2

print(f'Retornar {notas5} nota(s) de 5, {notas2} nota(s) de 2 e {moedas} moeda(s) de 1 real')
