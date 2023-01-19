import random
nome1 = str(input('Digite seu nome '))
nome2 = str(input('Digite seu nome '))
nome3 = str(input('Digite seu nome '))
nome4 = str(input('Digite seu nome '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('o sorteado da lista é {}:'.format(escolhido))



