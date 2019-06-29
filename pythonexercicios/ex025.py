nome = input('Digite seu nome completo: ')
if nome.lower().find('silva') >= 0:
    print('Tem Silva')
if nome.lower().find('silva') == -1:
    print('Não Tem Silva')
