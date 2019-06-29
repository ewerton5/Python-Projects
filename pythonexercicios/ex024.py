c = input('Qual o nome da sua cidade? ').strip()
if c.split()[0].lower() == 'santo':
    print('Começa com Santo')
if c.split()[0].lower() != 'santo':
    print('Não começa com Santo')
