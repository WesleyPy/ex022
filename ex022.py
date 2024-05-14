import time

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
time.sleep(2)

print('Seu nome em Maiusculas é {}.'.format(nome.upper()))
print('Seu nome em Minusculas é {}.'.format(nome.lower()))
primeiro = nome.split()
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(primeiro[0], len(primeiro[0])))