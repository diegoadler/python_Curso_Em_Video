vel = int(input('Digite a velocidade do seu carro: '))
if vel > 80:
    print('você foi multado! ')
    multa = (vel -80) * 7
    print('você deve pagar uma multa de R${:.2f}' .format(multa))
print('Tenha um bom dia! Dirija com cuidado!')

     