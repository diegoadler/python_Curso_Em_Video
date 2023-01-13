carteira = float(input('Digite quantos reais você tem? R$ '))
dollar = 3.27
euro = 5.51
iene = 0.040
libra_ester = 6.22
franco_suico = 5.49

dollar1 = carteira / dollar
euro1 = carteira / euro
iene1 = carteira / iene
libra1 = carteira / libra_ester
franc1 = carteira / franco_suico

print('Com R${:.2f} você compra  {:.2f} Dollares' .format(carteira,dollar1))
print('Com R${:.2f} você compra {:.2f} Euros' .format(carteira,euro1))
print('Com R${:.2f} você compra {:.2f} Ienes' .format(carteira,iene1))
print('Com R${:.2f} você compra {:.2f} Libras Esterlina' .format(carteira,libra1))
print('Com R${:.2f} você compra {:.2f} Francos Suíços' .format(carteira,franc1))

