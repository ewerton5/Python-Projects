p = []
r = []
nome = input('Olá, meu nome é Ana, qual o seu?\n').strip()
print('Olá,', nome)
np = input('Em que posso ajudar?\n').strip()
while True:
    if np in p:
        print(r[p.index(np)])
    else:
        nr = input('Não sei o que dizer.'
                   '\nVamos fazer uma brincadeira'
                   '\nEu finjo que sou você'
                   '\nE você finge que sou eu'
                   f'\nAgora me responda, {np}\n').strip().lower()
        p.append(np)
        r.append(nr)
        print('Ok! Agora voltamos a ser nós mesmos'
              '\nEu aprendo muito com você')
    np = input().strip()
