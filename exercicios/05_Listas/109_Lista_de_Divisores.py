n = 496
lista = []
i = n

if n == 0:
    print("Erro! Zero é divisível por qualquer número...")
else:
    while i > 0:
        if n % i == 0 and n != i:
            lista.append(i)
            i -= 1
        else:
            i -= 1
print(lista)
