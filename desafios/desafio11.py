altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

soma = altura * largura

print('Sua parede tem {}x{} e a sua area é de {}m².' .format(altura, largura, soma))
tinta = soma /2
print('para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))