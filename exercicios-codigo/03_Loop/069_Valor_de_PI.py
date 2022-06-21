pi = 3

for iteracao in range(1, 16, 1):
    if iteracao == 1:
        print(f'{iteracao}ª aproximação = {pi}')
    else:
        pi = pi + ((-1) ** iteracao) * 4 / ((2 * iteracao - 2) * (2 * iteracao - 1) * (2 * iteracao))
        print(f'{iteracao}° aproximação = {pi}')
