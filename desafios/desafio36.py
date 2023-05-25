casa = float(input('valor da casa: R$ '))
salario = float(input('Digite o valor do seu salario: '))
anos = int(input('quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print('para pagar uma casa de R${:.2f} em {}anos '.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('empréstimo pode ser concedido')
else:
    print('empréstimo negado')
    