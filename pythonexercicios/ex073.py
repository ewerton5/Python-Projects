cbf = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético'
       , 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba'
       , 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*15)
print(f'Lista de times do Brasileirão: {cbf}')
print('-='*15)
print(f'Os 5 primeiros são {cbf[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {cbf[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(cbf)}')
print('-='*15)
print(f'O Chapecoense está na {cbf.index("Chapecoense") + 1}ª posição')
