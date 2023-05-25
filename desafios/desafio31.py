distancia = float(input('qual a distancia da sua viagem ? '))
print('você está preste a começar uma viagem de {}km.' .format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('e o preço da sua passagem é de R$ {} '.format(preço))