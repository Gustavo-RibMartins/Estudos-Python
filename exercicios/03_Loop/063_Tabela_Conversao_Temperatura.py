celsius = -10
print("Celsius | Fahrenheit")

for incremento in range(0, 110, 10):
    celsius = celsius + 10
    fahrenheit = (celsius * 9 / 5) + 32
    print(f'{celsius:.2f}     {fahrenheit:.2f}')
