n = 10000
perfeitos = []

while n > 0:
    i = n
    soma = 0
    divisores = []
    while i > 0:
        if n % i == 0 and n != i:
            divisores.append(i)
            i -= 1
        else:
            i -= 1
    for j in range(len(divisores)):
        soma += divisores[j]
    if soma == n:
        perfeitos.append(n)
        n -= 1
    else:
        n -= 1
print(perfeitos)
