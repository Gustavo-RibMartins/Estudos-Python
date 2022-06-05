a = float(input('Digite o valor do primeiro lado do triangulo:'))
b = float(input('Digite o valor do segundo lado do triangulo:'))
c = float(input('Digite o valor do terceiro lado do triangulo:'))

if a == b == c:
    print('O triângulo é Equilátero')
elif a == b or a == c or b == c:
    print('O triângulo é Isósceles')
else:
    print('O triângulo é Escaleno')
