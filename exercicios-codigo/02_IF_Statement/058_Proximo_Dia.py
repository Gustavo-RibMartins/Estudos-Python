ano = int(input('Digite o ano: '))
mes = int(input('Digite o mes: '))
dia = int(input('Digite o dia: '))

# Flag ano bissexto

if ano % 4 == 0:
    bissexto = 1
else:
    bissexto = 0

if mes in (1, 3, 5, 7, 8, 10):
    if dia == 31:
        mes += 1
        dia = 1
    else:
        dia += 1
elif mes == 12:
    if dia == 31:
        ano += 1
        mes = 1
        dia = 1
    else:
        dia += 1
elif mes in (4, 6, 9, 11):
    if dia == 30:
        mes += 1
        dia = 1
    else:
        dia += 1
else:
    if bissexto == 1:
        if dia == 29:
            mes += 1
            dia = 1
        else:
            dia += 1
    else:
        if dia == 28:
            mes += 1
            dia = 1
        else:
            dia += 1

print(f'A data seguinte será {dia}/{mes}/{ano}')
