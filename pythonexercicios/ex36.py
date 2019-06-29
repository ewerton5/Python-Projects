v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento? '))
p = v/(a*12)
print(f'Para pagar uma casa de R${v:.2f} em {a} anos, a prestação será de R${p:.2f}.')
if p > s*0.3:
    print('Empréstimo NEGADO!')
else:
    print(f'Empréstimo pode ser CONCEDIDO!')
