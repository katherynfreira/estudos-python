nome = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer!')
separa = nome.split()
print('seu primeiro nome é {}'.format(separa[0]))
print('Seu ultomo nome é {}'.format(separa[len(separa)-1]))