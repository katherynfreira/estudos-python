diasalugados = float(input('Quantos dias alugados? '))
kmrodados = float(input('Quantos km rodados? '))
dias = diasalugados * 60
km = kmrodados * 0.15
total = dias + km
print ('O total a ser pago é R${:.2f}'.format(total))
