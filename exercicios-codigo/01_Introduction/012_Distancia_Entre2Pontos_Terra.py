from math import cos, sin, radians, acos

lon1 = radians(float(input('Digite a longitude do primeiro ponto em graus:\n')))
lat2 = radians(float(input('Digite a latitude do segundo ponto em graus:\n')))
lat1 = radians(float(input('Digite a latitude do primeiro ponto em graus:\n')))
lon2 = radians(float(input('Digite a longitude do segundo ponto em graus:\n')))

distancia = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))

print(f'A distância entre os dois pontos é {distancia:.2f}Km')
