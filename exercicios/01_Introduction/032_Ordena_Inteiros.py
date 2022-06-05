int1 = int(input('digite o primeiro inteiro:'))
int2 = int(input('digite o segundo inteiro:'))
int3 = int(input('digite o terceiro inteiro:'))

a = min(int1, int2, int3)
b = max(int1, int2, int3)
c = int1 + int2 + int3 - a - b

print(f'{a} - {c} - {b}')
