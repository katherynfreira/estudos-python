nome = str(input('Digite seu nome completo: '))
print('Analizando seu nome...')
print('Seu nome em maiúsclo é {}'.format(nome. upper()))
print('Sei nome em minúscolo é {}'.format(nome.lower()))
print('Seu nome tem {} letras '.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))