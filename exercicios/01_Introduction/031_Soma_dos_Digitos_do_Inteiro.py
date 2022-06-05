inteiro = int(input('Digite um inteiro de 4 digitos:\n'))

milhar = inteiro // 1000
centena = (inteiro - milhar * 1000) // 100
dezena = (inteiro - milhar * 1000 - centena * 100) // 10
unidade = inteiro - milhar * 1000 - centena * 100 - dezena * 10

print(f'{milhar} + {centena} + {dezena} + {unidade} = {milhar + centena + dezena + unidade}')
