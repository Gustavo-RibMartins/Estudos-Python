conteiner1 = input('Quantas garrafas com 1L ou menos você está reciclando?\n')
conteiner2 = input('Quantas garrafas com mais de 1L você está reciclando?\n')
deposito = float(conteiner1) * 0.10 + float(conteiner2) * 0.25
print(f'Seu depósito será de R$ {deposito:.2f}')
