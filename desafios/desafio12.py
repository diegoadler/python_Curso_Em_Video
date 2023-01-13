preço = float(input('Digite o preço do produto: '))
novo = preço - (preço * 5 / 100)


print('o produto que custava {:.2f}, na promoção com desconto de 5% vai custar {:.2f}'.format(preço, novo))

