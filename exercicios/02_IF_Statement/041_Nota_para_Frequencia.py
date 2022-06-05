nota_usuario = input('Digite a nota musical: ')

nota = nota_usuario.upper()[0]
oitava = int(nota_usuario[1])

if nota == 'C':
    print(f'A frequência é {216.63 / (2 ** (4 - oitava)):.2f} Hz')
elif nota == 'D':
    print(f'A frequência é {293.66 / (2 ** (4 - oitava)):.2f} Hz')
elif nota == 'E':
    print(f'A frequência é {329.63 / (2 ** (4 - oitava)):.2f} Hz')
elif nota == 'F':
    print(f'A frequência é {349.33 / (2 ** (4 - oitava)):.2f} Hz')
elif nota == 'G':
    print(f'A frequência é {392.00 / (2 ** (4 - oitava)):.2f} Hz')
elif nota == 'A':
    print(f'A frequência é {440.00 / (2 ** (4 - oitava)):.2f} Hz')
else:
    print(f'A frequência é {493.88 / (2 ** (4 - oitava)):.2f} Hz')
