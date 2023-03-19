from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar')
print('-=-' * 20)
jogador = int(input('em que numero pensei? '))
if jogador == computador:
    print('parabéns você acertou! ')
else:
    print('Ganhei eu pensei em um numero {} e não no {}' .format(computador, jogador))