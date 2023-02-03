nome = str(input('Digite seu nome: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
prime = nome.split()
title = nome.title()


print('todas as letras em maiusculo {} '.format(maiusculo))
print('todas as letras em minusculas {}'.format(minusculo))
print('quantidade de letras no texto é {}'.format(len(nome)-nome.count(' ')))
print('total de letras no primeiro nome {}'.format(len(prime[0])))
print('seu nome com as iniciais em maiusculo {} '.format(title))
