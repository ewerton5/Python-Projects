nome = input('Digite um nome completo: ').strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
nome = nome.split()
print('Seu nome tem ao todo {} letras'.format(len(''.join(nome))))
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras')