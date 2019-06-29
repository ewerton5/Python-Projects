d = float(input('Qual a distância da sua viagem? '))
if d > 200:
    p = d*0.45
else:
    p = d*0.5
print(f'Você está prestes a começar uma viagem de {d}Km.\nE o preço da sua passagem será de R${p:.2f}')
