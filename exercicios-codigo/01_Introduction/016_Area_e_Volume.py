from math import pi

r = float(input('Digite o valor do raio:\n'))
area = pi * (r ** 2)
volume = (4 / 3) * pi * (r ** 3)

print(f'A área do circulo de raio {r} é {area:.2f} e o volume da esfera é {volume:.2f}')
