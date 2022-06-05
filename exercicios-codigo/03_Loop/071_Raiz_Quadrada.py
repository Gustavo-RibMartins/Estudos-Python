x = float(input("Digite o valor de x: "))
raiz = x / 2

while abs(x - raiz * raiz) > 10 ** (-12):
    raiz = (raiz + (x / raiz)) / 2.00
print(f"A raiz aproximada é: {raiz:.16f}")
print(f"A raiz exata é     : {x ** 0.5:.16f}")
